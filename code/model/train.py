# -*- coding: utf-8 -*-
"""通过 gensim 训练模型，供后期使用"""

__author__ = "FRANPLK"

import warnings

from gensim.models import word2vec

warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')


class Train(object):

    def __init__(self, data_path, size=50, window=5):
        self.size = size
        self.window = window
        self.data_path = data_path

    def load_data(self):
        print('loading data...')
        sentence = word2vec.Text8Corpus(self.data_path)
        print('loading data done')
        return sentence

    def train(self):
        # Load file
        sentence = self.load_data()
        print("训练中...")
        model = word2vec.Word2Vec(
            sentence, size=self.size, window=self.window, workers=2, sg=0
        )
        # Save model
        model_name = 'model_gensim.bin'
        model.wv.save_word2vec_format(model_name, binary=True)
        print("训练完成，模型已存储到{}".format(model_name))


if __name__ == "__main__":
    file_path = 'E:\\xxx\\zhwiki_segment.txt'
    Train(file_path, window=3).train()
