# -*- coding:utf-8 -*-
# @author: houqian
# @since: 17/4/29
# @desc: 练习使用gensim

import gensim, logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)  # logging用来输出训练日志

# 分好词的句子，每个句子以词列表的形式输入
sentences = [['first', 'sentence'], ['second', 'sentence']]

# 用以上句子训练词向量模型
model = gensim.models.Word2Vec(sentences=sentences, min_count=1)

print (model['sentence'])  # 输出单词sentence的词向量
