import response
import numpy as np
from konlpy.tag import Twitter 

DATA_PATH = "./data/blood_rain.txt"

def load_data(path):
    with open(path, 'r') as f:
        data = f.read()
    return data


def doc2para(writing):
    paragraphs = []
    splited = writing.split('\n')
    para=""
    
    for token in splited:
        try:
            if token[-1] =='.':
                para += token
                paragraphs.append(para)
                para = ""
            
            else:
                para += token
            
        except:
            continue
            
    return paragraphs


def para2sen(paragraph):
    sentences = []
    sentences = paragraph.split('.')
    
    sentences = np.array([sen.split('?') for sen in sentences])
    sentences = list(sentences.flatten())
    sentences = np.array([sen.split('!') for sen in sentences])
    sentences = list(sentences.flatten())
    sentences = [ sentence.replace('"','') for sentence in sentences]
    return sentences


def sen2words_byspace(sentence):
    words = []
    words = sentence.strip().split(" ")
    return words


def sen2morph(sentence):
    morphs = []
    analyzer = Twitter()
    morphs = analyzer.morphs(sentence)
    return morphs

def analyzing_morphs(sentence):
    twitter=Twitter()
    return twitter.pos(sentence)
    
def main():
    blood_rain = load_data(DATA_PATH)
    paragraphs = doc2para(blood_rain)
    sentences = para2sen(paragraphs[4])
    words_byspace = sen2words_byspace(sentences[3])
    words_bymorphs = sen2morph(sentences[3])
    morphs_analyzed = analyzing_morphs(sentences[3])
    
    # 출력을 통해 토큰화가 잘 되었는지 확인합니다.
    print("띄어쓰기로 구분된 문장: ", words_byspace)
    print("형태소 별로 구분된 문장: ", words_bymorphs)
    print("형태소와 그에 따른 품사로 분류된 문장: ", morphs_analyzed)
    
if __name__=='__main__':
    response.run()
