f = open('articles.txt', encoding='utf-8')
texts = f.readlines()
f.close()
for text in texts[:10]:
    print(text)