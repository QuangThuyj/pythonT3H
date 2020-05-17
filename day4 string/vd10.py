text = input('Emter text:')
text = text.strip() #clean o dau va cuoi
print(text)

#clear all:
words = text.split()
result = ''
for word in words:
    result += word.strip() + ' '
print(result)
