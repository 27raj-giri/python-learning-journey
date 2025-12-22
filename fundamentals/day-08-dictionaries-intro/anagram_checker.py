text1 = "listen"
text2 = "silent"
t1 = {}
t2 = {}

for char in text1:
    t1[char] = t1.get(char, 0) + 1 

for char in text2:
    t2[char] = t2.get(char, 0) + 1

print(t1 == t2)
