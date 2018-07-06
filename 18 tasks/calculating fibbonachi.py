digit = input('Vvedite chislo ') #количесвто выводимых цифр
numbers = [str(i) for i in range(10)]

for index in range(len(digit)):
    if digit[index] not in numbers:
        print("Wrong input!")
        exit(404)

digit = int(digit)
if digit == 0:
    print('Wrong')
    exit(405)
fibbonachi=[0, 1]
for index in range(digit-1):
    fibbonachi.append(fibbonachi[index]+fibbonachi[index+1])
print(fibbonachi)

