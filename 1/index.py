min = 0
max = 10*20
while True:
    number = input('ведите целое число от ' + str(min) + ' до 10\u00B2\u00B0:\n')
    try:
        number = int(number)
        if(number < 0 or number > 10**20 ):
            print('число должно быть в диапазоне от ' + str(min) + ' до 10\u00B2\u00B0')
        else:
            evenNumbersSum = 0
            oddNumbersSum = 0
            strNumber = str(number)
            for s in strNumber:
                if(int(s) % 2 == 0):
                    evenNumbersSum += int(s)
                else:
                    oddNumbersSum += int(s)

            print(evenNumbersSum, oddNumbersSum)
            break
    except:
        print('разрешается вводить только целые числа')
