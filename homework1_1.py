#get data from user
print("Adjon meg egy számot és egy mértékegységet (cm/inch): ")
n = input()
s = input()

#convert data
if s == "cm":
    print(float(n)*0.3973, " inches")
elif s == "inch":
    print(float(n)*2.54, " cms")
else:
    print("Not correct unit")
