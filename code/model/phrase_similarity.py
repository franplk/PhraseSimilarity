#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date: 2020-03-04
# @Author Franplk

import jieba
import numpy as np
from gensim.models import KeyedVectors

from model import utils


def levenshtein_distance(sentence1, sentence2):
    """
    Return the Levenshtein distance between two strings.
    Based on:
        http://rosettacode.org/wiki/Levenshtein_distance#Python
    """
    first = utils.any2utf8(sentence1).decode('utf-8', 'ignore')
    second = utils.any2utf8(sentence2).decode('utf-8', 'ignore')
    sentence1_len, sentence2_len = len(first), len(second)
    maxlen = max(sentence1_len, sentence2_len)
    if sentence1_len > sentence2_len:
        first, second = second, first
    distances = range(len(first) + 1)
    for index2, char2 in enumerate(second):
        new_distances = [index2 + 1]
        for index1, char1 in enumerate(first):
            if char1 == char2:
                new_distances.append(distances[index1])
            else:
                new_distances.append(1 + min((distances[index1], distances[index1 + 1], new_distances[-1])))
        distances = new_distances
    levenshtein = distances[-1]
    d = float((maxlen - levenshtein) / maxlen)
    # smoothing
    return (utils.sigmoid(d * 6) - 0.5) * 2


class PhraseSimilarity(object):
    
    def __init__(self, model_path='E:\\TestFiles\\work2vec\\model\\model_50_3_sg1.bin'):
        self.model_path = model_path
        self.word_vectors = KeyedVectors.load_word2vec_format(model_path, binary=True)

    def compare(self, sentence1, sentence2, seg=True):
        if seg:
            sentence1 = [x for x in jieba.cut(sentence1, cut_all=False, HMM=False)]
            sentence2 = [x for x in jieba.cut(sentence2, cut_all=False, HMM=False)]
        else:
            sentence1 = sentence1.split()
            sentence2 = sentence2.split()
        sentence_vec_1 = self.get_sentence_vec(sentence1)
        sentence_vec_2 = self.get_sentence_vec(sentence2)
        sentence_vec_1 = np.sum(sentence_vec_1, axis=0)
        sentence_vec_2 = np.sum(sentence_vec_2, axis=0)

        cosine_value = utils.cosine(sentence_vec_1, sentence_vec_2)

        distance = self.edit_distance(sentence1, sentence2)

        if distance >= 0.99:
            r = 1.0
        elif distance > 0.9:
            r = utils.similarity_smooth(cosine_value, 0.05, distance, 0.05)
        elif distance > 0.8:
            r = utils.similarity_smooth(cosine_value, 0.1, distance, 0.2)
        elif distance > 0.4:
            r = utils.similarity_smooth(cosine_value, 0.2, distance, 0.15)
        elif distance > 0.2:
            r = utils.similarity_smooth(cosine_value, 0.3, distance, 0.1)
        else:
            r = utils.similarity_smooth(cosine_value, 0.4, distance, 0)
        if r < 0:
            r = abs(r)
        r = min(r, 1.0)
        return float("%.3f" % r)

    def get_sentence_vec(self, sentence, normalize=False):
        vectors = []
        for word in sentence:
            try:
                vector = self.word_vectors.word_vec(word, use_norm=normalize)
            except KeyError:
                continue
            sim_vectors = [vector]
            word_sim_list = self.word_vectors.similar_by_word(word, 10)
            for word_sim in word_sim_list[:10]:
                sim_vector = self.word_vectors.word_vec(word_sim[0], use_norm=normalize)
                sim_vectors.append(sim_vector)
            vectors.append(np.average(sim_vectors, axis=0))
        return vectors

    def edit_distance(self, s1, s2):
        """使用空间距离近的词汇优化编辑距离计算"""
        s1_len, s2_len = len(s1), len(s2)
        maxlen = s1_len
        if s1_len == s2_len:
            first, second = sorted([s1, s2])
        elif s1_len < s2_len:
            first = s1
            second = s2
            maxlen = s2_len
        else:
            first = s2
            second = s1
        ft = set()  # all related words with first sentence
        for x in first:
            ft.add(x)
            word_sim_list = self.word_vectors.similar_by_word(x, 10)
            for o in word_sim_list[:10]:
                ft.add(o[0])
        scores = []
        for x in second:
            choices = [levenshtein_distance(x, y) for y in ft]
            if len(choices) > 0:
                scores.append(max(choices))
        return np.sum(scores) / maxlen if len(scores) > 0 else 0


if __name__ == '__main__':
    p_sim = PhraseSimilarity()
    while True:
        sens = input('输入两个短语:')
        sen_list = sens.split(';')
        sim = p_sim.compare(sen_list[0], sen_list[1], seg=True)
        print('{}|{}:={}'.format(sen_list[0], sen_list[1], sim))
