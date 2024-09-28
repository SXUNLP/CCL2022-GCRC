# -*- coding: utf-8 -*-
"""
@author: yunxiao
@software: PyCharm
@file: eval.py
@email:yunxiaomr@163.com
@time: 2021/12/26 15:40
"""
import sys
import os
import json
import re
import collections


def compute_sentence_exact_match_score(pred_evidences, true_evidences):
    common_evidence = collections.Counter(pred_evidences) & collections.Counter(true_evidences)
    same_cnt = sum(common_evidence.values())
    if len(true_evidences) == 0 or len(pred_evidences) == 0:
        return int(true_evidences == pred_evidences)
    if same_cnt == 0:
        return 0
    precision = 1.0 * same_cnt / len(pred_evidences)
    recall = 1.0 * same_cnt / len(true_evidences)
    f1 = (2 * precision * recall) / (precision + recall)
    return f1


def compute_f1_score(pred_text, gold_text):
    def processing_punctuation(text):
        return re.sub(r"[\s+.!/_,$%^*()<>`={}?\-\"':;\[\]|—！，。？、~@#￥…&（）：；”“【】‘’]+", "", text)

    def get_text_tokens(text):
        text = processing_punctuation(text)
        return list(text)

    gold_tokens = get_text_tokens(gold_text)
    pred_tokens = get_text_tokens(pred_text)

    common_tokens = collections.Counter(gold_tokens) & collections.Counter(pred_tokens)
    same_cnt = sum(common_tokens.values())

    if len(gold_tokens) == 0 or len(pred_tokens) == 0:
        return int(gold_tokens == pred_tokens)
    if same_cnt == 0:
        return 0
    precision = 1.0 * same_cnt / len(pred_tokens)
    recall = 1.0 * same_cnt / len(gold_tokens)
    f1 = (2 * precision * recall) / (precision + recall)
    return f1


def eval_task_one(pred_file, golden_file):
    pred_res, gold_res = [], []
    with open(file=pred_file, mode="r", encoding="utf-8") as fin:
        pred_data = json.load(fin)
        pred_jsons = pred_data['data']
        for data_json in pred_jsons:
            pred_res.append((data_json['id'], data_json['answer']))

    with open(file=golden_file, mode="r", encoding="utf-8") as fin:
        gold_data = json.load(fin)
        gold_jsons = gold_data['data']
        for data_json in gold_jsons:
            gold_res.append((data_json['id'], data_json['answer']))

    pred_res_set, gold_res_set = set(pred_res), set(gold_res)

    correct = len(pred_res_set & gold_res_set)
    acc_task_one = 1.0 * correct / len(gold_res_set)

    # print(json.dumps({"Acc": acc_task_one}))
    return acc_task_one


def eval_task_two(pred_file, golden_file):
    f1 = exact_match = 0

    pred_res_dict, gold_res = {}, []
    with open(file=pred_file, mode="r", encoding="utf-8") as fin:
        pred_data = json.load(fin)
        pred_jsons = pred_data['data']
        for data_json in pred_jsons:
            pred_res_dict[data_json['id']] = data_json['evidences']

    with open(file=golden_file, mode="r", encoding="utf-8") as fin:
        gold_data = json.load(fin)
        gold_jsons = gold_data['data']
        for data_json in gold_jsons:
            gold_res.append((data_json['id'], data_json['evidences']))

    sum_cnt = 0
    for i, simple in enumerate(gold_res):
        simple_id, true_evidences = simple[0], simple[1]

        if simple_id not in pred_res_dict.keys():
            print('can not match id:%s, it will receive score 0.' % simple_id)
            continue
        else:
            for i in range(len(true_evidences)):
                try:
                    exact_match += compute_sentence_exact_match_score(pred_res_dict[simple_id][i], true_evidences[i])
                    f1 += compute_f1_score("".join(pred_res_dict[simple_id][i]), "".join(true_evidences[i]))
                    sum_cnt = sum_cnt + 1
                except IndexError as e:
                    print('can not find useful option, its option will receive score 0.')

    exact_match = 1.0 * exact_match / sum_cnt
    f1_task_two = 1.0 * f1 / sum_cnt

    # print(json.dumps({"F1 ": f1_task_two}))
    return f1_task_two


def eval_task_three(pred_file, golden_file):
    pred_res_dict, gold_res_list = {}, []

    with open(file=pred_file, mode="r", encoding="utf-8") as fin:
        pred_data = json.load(fin)
        pred_jsons = pred_data['data']
        for data_json in pred_jsons:
            pred_res_dict[data_json['id']] = data_json['error_type']

    with open(file=golden_file, mode="r", encoding="utf-8") as fin:
        gold_data = json.load(fin)
        gold_jsons = gold_data['data']
        for data_json in gold_jsons:
            simple_id = data_json['id']
            simple_ans = data_json['answer']
            simple_er = data_json['error_type']

            if (simple_er.count("") == 3):  # select correct
                index_ircorrect = [i for i in range(len(simple_er)) if (simple_er[i] != "")]

            elif (simple_er.count("") == 1):  # select ircorrect
                index_ircorrect = [i for i in range(len(simple_er)) if (simple_er[i] != "")]

            gold_res_list.append((simple_id, index_ircorrect, simple_er))

    sum_cnt = 0
    all_score_cnt = 0
    for i, simple in enumerate(gold_res_list):
        simple_id, true_index_error, true_simple_er = simple[0], simple[1], simple[2]
        simple_score_cnt = 0

        if (simple_id not in pred_res_dict.keys()):
            print('can not match id:%s, it will receive score 0.' % simple_id)
            continue
        else:
            pred_error_type = pred_res_dict[simple_id]
            try:
                for j in true_index_error:
                    simple_score_cnt = simple_score_cnt + 1 if (
                                pred_error_type[j] == true_simple_er[j]) else simple_score_cnt
                    all_score_cnt = all_score_cnt + 1 if (pred_error_type[j] == true_simple_er[j]) else all_score_cnt
            except IndexError as e:
                print('can not find the error reason of useful option, its option will receive score 0.')

        sum_cnt = sum_cnt + (len(true_simple_er) - true_simple_er.count(""))

    Acc_task_three = 1.0 * all_score_cnt / sum_cnt

    # print(json.dumps({"Acc": Acc_task_three}))
    return Acc_task_three


if __name__ == '__main__':
    pred_file = sys.argv[1]
    golden_file = sys.argv[2]

    if not os.path.exists(pred_file) or not os.path.exists(golden_file):
        print("predict File is not existing!" if not os.path.exists(pred_file) else "predict File is existing!")
        print("golden File is not existing!" if not os.path.exists(golden_file) else "golden File is existing!")
        exit(-1)

    acc1 = eval_task_one(pred_file, golden_file)
    acc2 = eval_task_two(pred_file, golden_file)
    acc3 = eval_task_three(pred_file, golden_file)

    print(json.dumps({"Task1_Acc": acc1, "Task2_F1": acc2, "Task3_Acc": acc3}))

''' shell
python eval.py prediction_file test_private_file
eg: python eval.py ./submit/test_submit.json  ./submit/test_private.json
'''
