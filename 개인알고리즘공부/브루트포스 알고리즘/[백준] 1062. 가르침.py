import re
from collections import Counter
n, k = map(int,input().split())
words = []
for _ in range(n):
    tmp = input()
    table = tmp.maketrans({
        'a': '',
        'n': '',
        't': '',
        'i': '',
        'c': '',
    })
    tmp = tmp.translate(table)
    #print(''.join(set(tmp)))
    words.append(''.join(set(tmp)))

#print(words)

def cnt_words(word: str):
    re.sub('')

# 기본적으로 anta, tica를 읽어야 하므로 k는 5이상이어야 한다.
if k < 5: # k가 5미만이면
    print(0) # 읽을 수 있는 단어 수는 0개
else:
    #print(''.join(words))
    alpha_cnt = Counter(''.join(words)).most_common() # 입력받은 단어들에 포함되는 알파벳 종류 집합
    #print(alpha_cnt)
    #print(alpha_cnt.most_common())
    if alpha_cnt[0][1] > alpha_cnt[1][1]:
        print(alpha_cnt[0][1])
    else:   # alpha[0][1] == alpha[1][1] , 즉 최빈값 여러 개 있으면
        for i in range(k - 5):
            #words = list(map(re.sub(alpha_cnt[i][0], ''), words))
            for j, word in enumerate(words):
                new_word = re.sub(alpha_cnt[i][0], '', word)
                words[j] = new_word     # 변경한 문자로 업데이트

        print(words.count(''))

