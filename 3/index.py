import random

min = 1
max = 100

while True:
    userNumber = input('ведите целое число от ' + str(min) + ' до ' + str(max) + '\n')
    try:
        userNumber = int(userNumber)
        if(userNumber < 0 or userNumber > 100):
            print('число должно быть в диапазоне от' + str(min) + 'до ' + str(max))
        else:            
                while True:
                    if(min > max or min == max or min < 1 or max > 100):
                            print('вы меня обманули:(')
                            break

                    number = random.randint(min, max)
                    userAnswer = input('это число: ' + str(number) + "?\n")
                    match userAnswer:
                        case 'больше':
                            min = number + 1
                              
                        case 'меньше':
                            max =  number - 1
                            
                        case 'верно':
                            print(':)')
                            break
                            
                        case _:
                            print('не понимаю что вы пишите')
                break    
    except ValueError:
        print('разрешены только целые числа')
