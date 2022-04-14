# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 22:37:08 2022

@author: 1clas
"""

words = """pig
dog
cat
horse
flower
"""

letter="goasjkdflwovhslawerdpi"

all_valid_words = ()
start = 0
end = 0
found_words = ()
c = ()
d = ""

for i in words:
    if i == "\n":
        all_valid_words += (words[start:end],) #튜플은 튜플끼리 더할 수 있음!
        start = end+1 #i가 \n을 만나면 start는 다음 단어를 위해 넘어감
        end = end+1  #end 도 마찬가지
    else:
        end += 1 #i가 \n을 만날 떄 까지 end는 커짐 
        
for a in all_valid_words:
    for b in a:
        if b in letter:
            d += b  # d는 letter와 words에 있는 알파벳이 같은 것의 총집합
            if a in d: # 만약 a가 총집합 d에 있다면 모든 단어가 있다는 뜻
                found_words += (a, )
print(found_words)