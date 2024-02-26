import bs4 as bs
from urllib import request
import re
import nltk
import heapq

class Info:
    def __init__(self):
        pass

    def data_collection(self):
        info = request.urlopen('https://en.wikipedia.org/wiki/MS_Dhoni')
        data = info.read()

        parse_data = bs.BeautifulSoup(data, 'lxml')
        para = parse_data.find_all('p')

        text = ""
        for p in para:
            text += p.text
        return text


    def data_preprocessing(self,text):
        orginal_text = re.sub(r'\[[0-9]*\]', ' ', text)
        orginal_text = re.sub(r'\s+', ' ', orginal_text)

        formmated_text = re.sub('[^a-zA-Z]', ' ', text)
        formmated_text = re.sub(r'\s+', ' ', formmated_text)
        return orginal_text, formmated_text

    def sentence_freq(self,orgi_text, form_text):
        sent_list = nltk.sent_tokenize(orgi_text)
        stop_words = nltk.corpus.stopwords.words('english')

        word_freq = {}
        for word in nltk.word_tokenize(form_text):
            if word not in stop_words:
                if word not in word_freq.keys():
                    word_freq[word] = 1
                else:
                    word_freq[word] += 1
        max_freq = max(word_freq.values())

        for word in word_freq.keys():
            word_freq[word] = (word_freq[word]/max_freq)

        sent_score = {}
        for par in sent_list:
            for word in nltk.word_tokenize(par.lower()):
                if word in word_freq.keys():
                    if len(par.split(' ')) < 10:
                        if par not in sent_score.keys():
                            sent_score[par] = word_freq[word]
                        else:
                            sent_score[par] += word_freq[word]
        return sent_score

    def stark_info_provider(self,score):
        imp_info = heapq.nlargest(10, score, key=score.get)
        for i in imp_info:
            print("->", i)


if __name__ == '__main__':
    obj= Info()
    text = obj.data_collection()
    orgi_text, form_text = obj.data_preprocessing(text)
    score = obj.sentence_freq(orgi_text, form_text)
    obj.stark_info_provider(score)
