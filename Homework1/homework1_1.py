#get data from user
def getInput():
    print("Adjon meg egy számot és egy mértékegységet (cm/inch): ")
    n = input()
    s = input()
    l = [n, s]
    return l

#convert data
def convert(n, s):
    if s == "cm":
        print(float(n)*0.3973, " inches")
    elif s == "inch":
        print(float(n)*2.54, " cms")
    else:
        print("Not correct unit")

if __name__ == "__main__":
    l = getInput()
    convert(l[0], l[1])
