# CCL 2022 高考语文阅读理解可解释评测
- 组织者
  - 谭红叶(山西大学)
  - 李  茹(山西大学)
  - 张  虎(山西大学)
  - 王元龙(山西大学)
  - 王智强(山西大学)
- 联系人
  - 孙欣伊(山西大学博士生, 总负责, sxy_sxu@163.com)
  - 赵云肖(山西大学博士生)
  - 闫智超(山西大学硕士生)
  - 冯慧敏(山西大学硕士生)
  - 闫国航(山西大学硕士生)

评测任务详细内容可查看评测网站：[https://github.com/SXUNLP/CCL2022-GCRC](https://github.com/SXUNLP/CCL2022-GCRC)，遇到任何问题请发邮件或在[Issue](https://github.com/SXUNLP/CCL2022-GCRC/issues)中提问，欢迎大家参与。

## 1.任务内容
### 任务简介：
机器阅读理解（Machine Reading Comprehension, MRC）是自然语言处理和人工智能领域的重要前沿课题，对提升机器的智能水平具有重要价值。目前，在众多公开可用数据集的驱动下，机器阅读理解模型取得了令人振奋的进展，但模型所具备的真实语言理解能力与人的期望相差甚远。为了促进机器智能向类人智能迈进，我们提出了“高考语文阅读理解可解释评测”任务(Gaokao Chinese Reading Comprehension, GCRC)。该任务不仅对模型的答题准确率进行评价，而且引入两个子任务“支持句识别”和“错误类型识别”对模型的中间推理能力进行评价，此外还提供了答题所需推理能力信息，帮助诊断模型的不足。具体来说，参赛者需要完成以下3个子任务：
- 子任务1（问题回答）：输出问题答案。
- 子任务2（支持句识别）：输出支持问题解答所需的原文句子，即每个选项对应的原文支持句。
- 子任务3（错误类型识别）：针对错误选项，输出其错误类型。
  - 错误类型具体有7种（括号内为类型标签）：
    - 细节错误（Wrong details，DTL）
    - 时间属性错误(Wrong temporal properties，TEMP)
    - 主谓不一致（Wrong subject-predicate-object triple relationship，SPOT）
    - 充要条件错误（Wrong necessary and sufficient conditions，NAS）
    - 答非所问(Irrelevant to the question，ITQ)
    - 因果错误（Wrong causality，CAUS）
    - 无中生有（Irrelevant to the article，ITA）。

## 2.评测数据
### 数据集规模
本评测使用山西大学提供的GCRC数据集，数据主要来源于高考语文阅读理解题目。数据集相关信息如表1所示。
<p align='center'>表1 GCRC数据集规模</p>
<table align='center'>
<tr align='center'>
<td>     </td>
<td> Training-Set  </td>
<td> Dev-Set </td>
</tr>
<tr align='center'>
<td> 子任务1的篇章数  </td>
<td> 3790 </td>
<td> 683 </td>
</tr>
<tr align='center'>
<td> 子任务1的问题数  </td>
<td> 6994 </td>
<td> 863 </td>
</tr>
<tr align='center'>
<td> 子任务2的问题/选项数  </td>
<td> 2021/8084 </td>
<td> 863/3452 </td>
</tr>
<tr align='center'>
<td> 子任务3的问题/错误选项数  </td>
<td> 2000/3253 </td>
<td> 863/1437 </td>
</tr>
<tr align='center'>
<td> 标注推理能力的问题/选项数  </td>
<td> - </td>
<td> 863/3452 </td>
</tr>
</table>
注：GCRC数据集还提供了答题所需推理能力的标注信息，以指导参评者了解模型缺陷，有针对性地提升模型性能。具体推理能力（括号内为标签标号）为：

- 细节推理（Detail understanding，DTL-R）
- 共指推理（Coreference resolution，CO-REF）
- 演绎推理（Deductive reasoning，DED）
- 数字推理（Mathematical reasoning，MATH）
- 时空推理（Temporal/spatial reasoning，TEM-SPA）
- 因果推理（Cause-effect comprehension，CAUS-R）
- 归纳推理（Inductive reasoning，IND）
- 鉴赏分析（Appreciative analysis，APPREC）。

### 数据样例
每条数据包含以下内容：编号(id）、标题(title)、文章(passage)、问题(question)、选项(options)、选项支持句(evidences)、推理能力(reasoning_ability)、错误类型(error_type)、答案(answer)。具体数据样例如下所示。
Json格式：
~~~
{ "id": "gcrc_4916_8172", 
  "title": "我们需要怎样的科学素养", 
  "passage": "第八次中国公民科学素养调查显示，2010年，我国具备...激励科技创新、促进创新型国家建设，我们任重道远。", 
  "question": "下列对“我们需要怎样的科学素养”的概括，不正确的一项是", 
  "options":  [
    '科学素养是一项基本公民素质，公民科学素养可以从科学知识、科学方法和科学精神三个方面来衡量。',
    '不仅需要掌握足够的科学知识、科学方法，更需要具备学习、理解、表达、参与和决策科学事务的能力。',
    '应该明白科学技术需要控制，期望科学技术解决哪些问题，希望所纳的税费使用于科学技术的哪些方面。', 
    '需要具备科学的思维和科学的精神，对科学技术能持怀疑态度，对于媒体信息具有质疑精神和过滤功能。'
  ],
  "evidences": [
    ['公民科学素养可以从三个方面衡量：科学知识、科学方法和科学精神。', '在“建设创新型国家”的语境中，科学素养作为一项基本公民素质的重要性不言而喻。'],
    ['一个具备科学素养的公民，不仅应该掌握足够的科学知识、科学方法，更需要强调科学的思维、科学的精神，理性认识科技应用到社会中可能产生的影响，进而具备学习、理解、表达、参与和决策科学事务的能力。'], 
    ['西方发达国家不仅测试公众对科学技术与社会、经济、文化等各方面关系的看法，更考察公众对科学技术是否持怀疑态度，是否认为科学技术需要控制，期望科学技术解决哪些问题，希望所纳的税费使用于科学技术的哪些方面等。'], 
    ['甚至还有国家专门测试公众对于媒体信息是否具有质疑精神和过滤功能。', '西方发达国家不仅测试公众对科学技术与社会、经济、文化等各方面关系的看法，更考察公众对科学技术是否持怀疑态度，是否认为科学技术需要控制，期望科学技术解决哪些问题，希望所纳的税费使用于科学技术的哪些方面等。']
   ],
  "reasoning_ability": ["DTL-R","DTL-R","IND","IND"],
  "error_type": ["ITQ", "", "", ""],
  "answer": "A"
}
~~~
注：在数据样例中，字段“answer”、“evidences”和“error_type”分别对应子任务1（问题回答）、子任务2（支持句识别）和子任务3（错误类型识别）的输出。其中“error_type”字段只输出错误选项的错误类型。例如在本例中，“question”字段要求机器选出不正确的选项，本样例只有选项A与原文意思不符，因此“error_type”字段仅输出选项A的错误类型。

## 3.评价标准
> 子任务1(问答任务)：以准确率（Accuracy）作为评价指标，具体定义如下：
$$Task1-ACC=\frac{正确答案个数}{题目总数}$$

> 子任务2（支持句识别）：以F1作为评价指标，计算公式如下：
$$Task2-F1=\frac{\displaystyle\sum_{i=1}^{N} F1_i}{N}$$
$$F1_i=\frac{2 \times precision \times recall}{precision+recall}$$
$$precision=\frac{InterSec(gold,pred)}{Len(pred)}$$
$$recall=\frac{InterSec(gold,pred)}{Len(gold)}$$

其中，gold与pred分别表示真实结果与预测结果，InterSec()表示计算二者共有的token长度，Len()表示计算token长度。
> 子任务三（错误类型识别）：以准确率（Accuracy）作为评价指标。
$$Task3-ACC=\frac{正确预测个数}{错误选项总数}$$

参赛系统的最终得分由上述三个指标综合决定，具体计算公式如下：
$$Score=\frac{Task1-ACC+Task2-F1+Task3-ACC}{3}$$

指标计算脚本eval.py会随训练集一起发布。

## 4.报名方式及评测赛程
报名方式： 
本次评测采用电子邮件进行报名，邮件标题为：“CCL2022-高考语文阅读理解可解释评测-参赛单位”，例如：“CCL2022-高考语文阅读理解可解释评测-山西大学”；附件内容为队伍的参赛报名表，报名表请查看附件1：高考语文阅读理解可解释评测报名表.docx，同时报名表应更名为“参赛队名+参赛队长信息+参赛单位名称”。请参加评测的队伍发送邮件至sxy_sxu@163.com。报名截止前未发送报名邮件者不参与后续的评选。

### 赛程安排：
- 1.报名时间：6月1日-7月31日
- 2.发布训练、验证及测试数据：6月5日

完成报名后，参赛队伍在智源指数平台上获取评测数据。数据集获取链接：http://cuge.baai.ac.cn/#/dataset?id=22&name=GCRC
- 3.提交评测结果及模型代码：8月15日
- 4.审核模型，公布评测结果：8月30日
- 5.提交评测论文：9月25日
- 6.报告及颁奖：10月14日

（以上时间均为暂定，请关注 [CCL 2022](http://cips-cl.org/static/CCL2022/index.html) 官方网站。）

### 结果提交：
本次评测结果在智源指数平台上进行提交和排名。在参赛期间，严禁参赛团队注册其它账号多次提交。

提交规则：

选手登录智源指数平台后，在“提交评测”界面，准确填写“模型名称”、“模型描述”、“参数总数”、“机构”等信息，其中“机构”一项填写“参赛队伍名”。完成填写后，参赛者在界面右下方点击“选择ZIP”，提交具体的评测结果及模型。

提交的压缩包命名为GCRC.zip，其中包含的文件内容为：
- （1）输出结果文件：该文件是以utf-8为编码格式的json文件，其中的内容格式与训练数据集保持一致，结果文件格式不正确不予计算成绩。该文件命名为：GCRC.json;
- （2）模型文件：评测使用的模型，所提交模型必须真实可复现，文件命名为：model.zip。
- 文件夹格式示例如下:

   >--GCRC.zip
   >>----GCRC.json
   >> 
   >>----model.zip

## 5.奖项设置
本次评测将评选出如下奖项。由中国中文信息学会计算语言学专委会（CIPS-CL）为获奖队伍提供荣誉证书。
<table align='center'>
<tr align='center'>
<td> 奖项  </td>
<td> 一等奖 </td>
<td> 二等奖 </td>
<td> 三等奖 </td>
</tr>
<tr align='center'>
<td> 数量 </td>
<td> 1名 </td>
<td> 2名 </td>
<td> 3名 </td>
</tr>
<tr align='center'>
<td> 奖励  </td>
<td> 荣誉证书 </td>
<td> 荣誉证书 </td>
<td> 荣誉证书 </td>
</tr>
</table>

## 6.注意事项
- （1）由于版权保护问题，GCRC数据集只免费提供给用户用于非盈利性科学研究使用，参赛人员不得将数据用于任何商业用途。如果用于商业产品，请联系谭红叶老师，联系邮箱hytan_2006@126.com。
- （2）每名参赛选手只能参加一支队伍，一旦发现某选手以注册多个账号的方式参加多支队伍，将取消相关队伍的参赛资格。
- （3）数据集的具体内容、范围、规模及格式以最终发布的真实数据集为准。针对测试集，参赛人员不允许执行任何人工标注。
- （4）允许使用公开和选手个人/组织内部的代码、工具、外部数据（从其他渠道获得的标注数据）等，但需要保证参赛结果可以复现。
- （5）算法与系统的知识产权归参赛队伍所有。要求最终结果排名前6的队伍提供算法代码与系统报告（包括方法说明、数据处理、参考文献和使用开源工具、外部数据等信息）。评测结果提交完毕，我们会对各个队伍提交的模型进行检验，如果在排行榜上的结果无法复现，将取消获奖资格，获奖团队名单依次顺延。
- （6）参赛团队需保证提交作品的合规性，若出现下列或其他重大违规的情况，将取消参赛团队的参赛资格和成绩，获奖团队名单依次顺延。重大违规情况如下：
  - a.使用小号、串通、剽窃他人代码等涉嫌违规、作弊行为；
  - b.团队提交的材料内容不完整，或提交任何虚假信息；
  - c.参赛团队无法就作品疑议进行足够信服的解释说明；

- （7）本次评测为参赛队伍提供一定数量的算力支持，超过限额后，超出部分需要自行购买。本次评测算力由北京并行科技有限公司赞助。
- （8）如需使用本数据集进行课题研究及论文发表，应公开声明使用了山西大学提供的数据，并进行如下引用：

    TAN H, WANG X, JI Y, et al. GCRC: A New Challenging MRC Dataset from Gaokao Chinese for Explainable Evaluation[C]//Findings of the Association for Computational Linguistics: ACL-IJCNLP 2021. 2021: 1319-1330. 

同时发信给hytan_2006@126.com，说明相关情况。

#### 任务数据集发布地址：
http://cuge.baai.ac.cn/#/dataset?id=22&name=GCRC

#### 评测单位
山西大学
#### 算力赞助单位
北京并行科技有限公司
