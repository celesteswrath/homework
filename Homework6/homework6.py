with open("homework.txt", "r", encoding="utf-8") as file, open("output.txt", "x", encoding="utf-8") as output:

    line = file.readline()
    letters = ['a', 'e', 'o', 'u', 'i', 'á', 'é', 'ó', 'ú', 'ö', 'ü', 'ő', 'ű', 'í']
    characters = ['.', ',', '?', '!', '-']
    linecount = 1

    while line:
        if linecount % 3 == 0:
            if line != "\n":
                for character in line:
                    if character.lower() not in letters and character not in characters:
                        output.write(character)
        line = file.readline()
        linecount += 1
