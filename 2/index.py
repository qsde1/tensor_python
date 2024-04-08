min = 1
max = 20

while True:
    stringsCount = input('ведите целое число от ' + str(min) + ' до ' + str(max) + '\n')
    try:
        stringsCount = int(stringsCount)
        if(stringsCount < 0 or stringsCount > 20 ):
            print('число должно быть в диапазоне от ' + str(min) + ' до ' + str(max))
        else:            
            for i in range(stringsCount-1,-1, -1):
                print((' '*(i))+'#'*(stringsCount-i))
            break
    except:
        print('разрешается вводить только целые числа')