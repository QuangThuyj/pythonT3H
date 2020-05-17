def splitText(text):
    return set(text.lower().split())

def calIOU(text1, text2):
    # l1 = text1.split()
    # l2 = text2.split()
    # s1 = set(l1)
    # s2 = set(l2)
    s1 = splitText(text1)
    s2 = splitText(text2)
    i = s1.intersection(s2)
    u = s1.union(s2)
    return len(i)/len(u)


text = input('Text:')
f = open('articles.txt', encoding='utf-8')
texts = f.readlines()
f.close()

scores = []
for i in range(len(texts)):
    score = calIOU(text, texts[i])
    scores.append((score, i))

scores = sorted(scores, reverse=True)
for score, i in scores[:5]:
    print(score, texts[i])

# print(calIOU(text1, text2))
