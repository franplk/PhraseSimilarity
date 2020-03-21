# -*- coding: utf-8 -*-

import jieba


class Segmentation(object):

    def __init__(self, txt_path, seg_path, stop_word_path=None):
        self.stopwordset = set()
        self.txt_path = txt_path
        self.seg_path = seg_path
        if stop_word_path:
            self.set_stop_word(stop_word_path)

    def set_stop_word(self, stop_word_path):
        """读取停用词"""
        with open(stop_word_path, "r", encoding="utf-8") as stopwords:
            for word in stopwords:
                self.stopwordset.add(word.strip('\n'))
        print("停用词读取完成")

    def do_seg(self):
        print("结巴分词中...")
        seg_txt_file = open(self.seg_path, "w", encoding="utf-8")
        with open(self.txt_path, "r", encoding="utf-8") as Corpus:
            for sentence in Corpus:
                terms = jieba.cut(sentence.strip("\n"), cut_all=False)
                terms_no_stop = filter(lambda t: t not in self.stopwordset, terms)
                seg_txt_file.write(" ".join(terms_no_stop))
        print("jieba分词完成!")
        seg_txt_file.close()


if __name__ == "__main__":
    txt_file_path = 'E:\\xxx\\zhwiki-latest.txt'
    seg_file_path = 'E:\\xxx\\zhwiki_segment.txt'
    Segmentation(txt_file_path, seg_file_path).do_seg()
