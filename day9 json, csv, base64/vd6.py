import json
with open('result.json', encoding='utf-8') as f:
    obj = json.load(f) #obj json.loads(f.read())
    print(obj['fullTextAnnotation']['text'])