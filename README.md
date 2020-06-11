# NER-命名体识别任务资源总结

## 先列出来代码实现：

1. [NLP实战-中文命名实体识别-MaggicQ的文章-知乎](https://zhuanlan.zhihu.com/p/61227299) ---这个代码很推荐了

本文作者写的前言:
本文章将通过pytorch作为主要工具实现不同的模型（包括HMM，CRF，Bi-LSTM，Bi-LSTM+CRF）来解决中文命名实体识别问题，文章不会涉及过多的数学推导，但会从直观上简单解释模型的原理，主要的内容会集中在代码部分。

上述文章的代码是实现：
[中文命名实体识别-包括多种模型-HMM-CRF-BiLSTM-BiLSTM+CRF的具体实现](https://github.com/luopeixiang/named_entity_recognition)

2. Bert命名体识别代码实现[这里](https://github.com/circlePi/Bert_Chinese_Ner_pytorch)-使用的pytorch框架

用的人民日报数据实现的中文命名体识别

3. [nlp_base](https://github.com/lpty/nlp_base) 

实现了以下算法:
基于HMM的中文分词模型

基于fasttext的情感极性判断模型

基于MaxEnt的中文词性标注模型

基于CRF的中文命名实体识别模型

基于序列标注的中文依存句法分析模型

基于Xgboost的中文疑问句判别模型



## 综述
1. [命名识别综述-1](http://pelhans.com/2019/09/23/kg_paper-note4/)

这篇文章写得比较详细，主要是介绍了NER的评价指标，NER中应用的深度学习算法及其细节（包括词向量的表示(基于词/基于字/混合）），NER任务中的前沿深度学习（包括多任务学习，迁移学习，主动学习，强化学习，对抗学习）


2. [命名实体识别综述-2](https://zekizz.github.io/ML/NER-survey/)

本文比较详细的介绍了NER的各种细节，包括评价指标,监督学习，半监督学习，迁移学习等

3. [A-Survey-on-Deep-Learning-for-Named-Entity-Recognition](  https://arxiv.org/abs/1812.09449)

上面是一个综述论文


4. [NER任务的评测指标](https://blog.csdn.net/ANNILingMo/article/details/80398473)



## 基本模型介绍

### CRF
1. [最通俗易懂的BiLSTM-CRF模型中的CRF层介绍-孙孙的文章-知乎](https://zhuanlan.zhihu.com/p/44042528)

这篇文章非常推荐！！！这是一篇翻译的文章，原文很精彩，值得细细品读，如果英文不好，可以看这个译文。这篇文章花了大量重点，介绍了CRF在BILSTM-CRF模型中的运行过程。

2. [如何用简单易懂的例子解释条件随机场（CRF）模型？它和HMM有什么区别-milter的回答-知乎](https://www.zhihu.com/question/35866596/answer/139485548)

这个文章写的也很好，值得好好看看

3. [如何理解LSTM后接CRF-知乎](https://www.zhihu.com/question/62399257)

这个是我在读完上面两个之后，看到这个答案，尤其是高赞答案，一句简单的话，就点出了CRF在模型中的核心作用。

### 维特比算法
1. [如何通俗地讲解viterbi算法-路生的回答-知乎](https://www.zhihu.com/question/20136144/answer/763021768)

2. [图解Viterbi维特比算法-Yuanche.Sh的文章-知乎](https://zhuanlan.zhihu.com/p/63087935)

维特比算法两个讲的都不错，可以好好看看


## 命名体识别论文


1. [一些关于NER任务调研的小思考](http://kugwzk.info/index.php/archives/3204)
  
  这个文章详细列出了他看过的关于NER的论文，并对每个论文做了一个简单概述


2. [ACL-2018-利用Lattice-LSTM的最优中文命名实体识别方法-机器之心的文章-知乎](https://zhuanlan.zhihu.com/p/38941381)




## 在工作中的实际经验

1. 数据增强
[一文详解深度学习在命名实体识别(NER)中的应用](https://www.jiqizhixin.com/articles/2018-08-31-2)

这篇文章可以看看它的数据增强的部分，就是随机地对各个句子进行bigram、trigram拼接后与原始句子一起作为训练语料；词典随机替换；

[小标注数据量下自然语言处理实战经验](https://www.jiqizhixin.com/articles/2019-08-16-6)

这个文章详细阐述了达观在小标注语料情况下进行算法优化的经验，可以看一看


## 竞赛
1. [命名体识别竞赛之达观杯](https://www.biendata.com/competition/datagrand/leaderboard/)

达观杯的信息抽取竞赛，数据是匿名数据，抽取a/b/c三个字段



