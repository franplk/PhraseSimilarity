# -*- coding: utf-8 -*-

from gensim.corpora import WikiCorpus


class WikiToTxt(object):

    def __init__(self, wiki_data_path, save_text_path):
        self.wiki_data_path = wiki_data_path
        self.save_text_path = save_text_path
        pass

    def set_wiki_to_txt(self):
        wiki_corpus = WikiCorpus(self.wiki_data_path, dictionary={})
        with open(self.save_text_path, 'w', encoding='utf-8') as output:
            for text in wiki_corpus.get_texts():
                output.write(' '.join(text) + '\n')
            print("转档完成!")


if __name__ == "__main__":
    # wiki 语料转换成TXT文件
    xml_path = 'E:\\xxx\\zhwiki-latest-articles.xml.bz2'
    save_path = 'E:\\xxx\\zhwiki-latest.txt'
    wiki_to_txt = WikiToTxt(xml_path, save_path)
    wiki_to_txt.set_wiki_to_txt()
