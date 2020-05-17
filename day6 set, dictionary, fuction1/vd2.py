text1 = input('text1:')
text2 = input('text2: ')

l1 = text1.lower().split()
l2 = text2.lower().split()

s1 = set(l1)
s2 = set(l2)

u = s1.union(s2)
i = s1.intersection(s2)

iou = len(i)/len(u)
print("IOU = ", iou)

