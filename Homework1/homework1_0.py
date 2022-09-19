#get data from user
def getInput():
    s = input("Adjon meg egy mondatot:")
    return s

#count letters
def countLetters(sentence):
    d = {}
    s = sentence
    for i in s:
        n = 0
        for j in s:
            if j == i: n += 1
            d[i] = n
    print("Betűk gyakorisága:", d)

#reverse string
def reverse(sentence):
    s = sentence
    r = ""
    for i in range(len(s), 0, -1):
        r += s[i-1]
    print("Fordítva: ", r)

#separate words into list
def separate(sentence):
    s = sentence
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

if __name__ == "__main__":
    s = getInput()
    countLetters(s)
    reverse(s)
    separate(s)
