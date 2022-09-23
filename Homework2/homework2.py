#get input from user
def getInput():
    print("Adja meg a háromszög három oldalát cm-ben: ")
    a = int(input("a oldal (cm): "))
    b = int(input("b oldal (cm): "))
    c = int(input("c oldal (cm): "))
    l = [a, b, c]
    return l

#check if triangle can be drawn
def isTriangle(list):
    if list[0] + list[1] > list[2]:
        if list[0] + list[2] > list[1]:
            if list[1] + list[2] > list[0]:
                print("A " + str(list[0]) + ", " + str(list[1]) + " és " + str(list[2]) +
                " oldalú háromszög szerkeszthető.")
            else: print("A " + str(list[0]) + ", " + str(list[1]) + " és " + str(list[2]) +
            " oldalú háromszög nem szerkeszthető.")
        else: print("A " + str(list[0]) + ", " + str(list[1]) + " és " + str(list[2]) +
        " oldalú háromszög nem szerkeszthető.")
    else: print("A " + str(list[0]) + ", " + str(list[1]) + " és " + str(list[2]) +
    " oldalú háromszög nem szerkeszthető.")

#main
if __name__ == "__main__":
    l = getInput()
    isTriangle(l)
