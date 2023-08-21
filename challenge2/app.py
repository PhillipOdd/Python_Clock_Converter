def checker (a,b,c):
    positive = 0


    if a > 0:
        positive += 1
    if b > 0:5
    2
    positive += 1
    if c > 0:
        positive += 1

    return positive >= 2


a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if checker(a, b, c):
    print("True")
else:
    print("False")