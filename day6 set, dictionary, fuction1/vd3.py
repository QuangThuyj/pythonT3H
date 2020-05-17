d= {
    'one': 'mot',
    'two': 'hai',
    'Three': 'ba'
}

print(d['two'])

print(d.get('four'))

d.update({'five':'nam', 'six':'sau'})

print('four' in d)

del d['five']

print('five' in d)

print(d)