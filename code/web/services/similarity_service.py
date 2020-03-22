#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date: 2020-03-09
# @Author Franplk

from model import PhraseSimilarity
from web.exception import APIError
from web.www import app


class SimilarityService(object):
    phrase_sim = PhraseSimilarity(app.config.get('MODEL_PATH'))

    @classmethod
    def compare(cls, sen1, sen2):
        """对比两个短语的相似度
        @param sen1: 短语一
        @param sen2: 短语二
        """
        similarity = cls.phrase_sim.compare(sen1, sen2, seg=True)
        return '{:.2f}'.format(similarity)

    @classmethod
    def multi_compare(cls, mode, sens):
        """对比短语列表相似度
        @param mode: 对比模式-矩阵方式和对象方式
        @param sens: 句子列表以英文分开切割
        """
        sen_list = str(sens).split(';')
        if len(sen_list) < 2:
            raise APIError(message='短语个数不能少于两个')
        if mode == 'mat':
            sim_data = cls.phrase_sim.compare_matrix(sen_list)
        else:
            sim_data = cls.phrase_sim.compare_map(sen_list)
        return sim_data
