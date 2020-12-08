sum = 0
num = "0"
while num.isdigit():
    sum += float(num)
    print("entrer un nombre")
    num = input()

print("la somme est", sum)
