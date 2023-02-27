n = int(input())
book = []
unique=[]

for _ in range(n):
    book.append(input())

for x in book:
    if x not in unique:
        unique.append(x)

count =[book.count(x) for x in unique]
idx = []

for i in range(len(count)):
    if count[i]==max(count):
        idx.append(i)

print(sorted([unique[i] for i in idx])[0])