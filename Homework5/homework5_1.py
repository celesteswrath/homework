def pal():
    word = input("Adjon meg egy szót: ")
    word2 = ""
    for i in word:
        word2 = i + word2;
    if word == word2:
        print("A szó palindróma")
    else:
        print("A szó nem palindróma")
    return
if __name__ == "__main__":
    pal()
