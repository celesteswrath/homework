#get data from user
s = input("Adjon meg egy mondatot:")

#count letters
d = {}
for i in s:
    n = 0
    for j in s:
        if j == i: n += 1
    d[i] = n
print("Betűk gyakorisága:", d)

#reverse string
r = ""
for i in range(len(s), 0, -1):
    r += s[i-1]
print("Fordítva: ", r)

#separate words into list
l = []
t = ""
for i in s:
    if i != " ":
        t = t + i
    else:
        l.append(t)
        t = ""
l.append(t)
print("Listába rendezve szavanként: ", l)
