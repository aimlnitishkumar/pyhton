
from collections import Counter

s = "leelvtcode"

count = Counter(s)

for i, char in enumerate(s):
    if count[char] == 1:
        print(count[char])
        print(i)
        break
print(count)