import string

def check(value):  
    for letter in value:  
        if letter not in string.digits:  
            return False
    return True

while True:
    number = input('Input a large whole number: ')
    split = input('Input the split (whole number): ')

    if (not check(number) or not check(split)):
        print('Input positive integer')
        continue
    elif (len(number)%int(split)):
        print('Not divisible')
        continue
    else:
        split = int(split)

    liste = [number[i:i+split] for i in range(0, len(number), split)]

    print(liste)

    a = -1
    result = 'Sequence is increasing'
    for i in liste:
        if int(i) <= a:
            result = 'Sequence is not increasing'
            break
        else:
            a = int(i)

    print(result)

    option = input("Want to continue? [y,n] ")
    if option == 'n':
        break

