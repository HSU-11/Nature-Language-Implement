import jieba
import jieba.analyse

txt = open("hw1-dataset.txt", encoding="utf-8").read()

#統計前100個高頻的字詞
words  = jieba.lcut(txt)

counts = {}  
for word in words:  
    counts[word] = counts.get(word,0) + 1

items = list(counts.items())  
items.sort(key=lambda x:x[1], reverse=True)

#找出前100個TF-IDF權重高的字詞
#tags = jieba.analyse.extract_tags(txt, 100)

for i in range(100):  
    word, count = items[i]  
    print ("{0:<5}{1:>7}".format(word, count))
    
