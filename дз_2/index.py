import copy



#функция выполняющая одну итерацию
def makeIteration(state: list):
    newState = []

    for rowIndex, rowList in enumerate(state):
        rowNewState = []
        for colIndex, item in enumerate(rowList):
            neighboursCount = 0
            #проверка по часовой оси, начинаю элемента над проверяемым
            
            #проверить элемент сверху
            if(rowIndex == 0):
                i = len(state)-1
            else:
                i = rowIndex-1                
            j=colIndex
            if(state[i][j] == 1):
                neighboursCount += 1

            #проверить элемент справа сверху
            if(colIndex == len(rowList)-1):
                j = 0            
            else:
                j = colIndex+1
            if(state[i][j] == 1):
                neighboursCount += 1

            #получить элемент справа    
            i = rowIndex
            if(state[i][j] == 1):
                neighboursCount += 1

            #получить элемет справа снизу
            if(rowIndex == len(state)-1):
                i = 0
            else:
                i = rowIndex+1                
            if(state[i][j] == 1):
                neighboursCount += 1

            #получить элемент снизу
            j = colIndex
            if(state[i][j] == 1):
                neighboursCount += 1

            #получить элемент слева снизу
            if(colIndex == 0):
                j = len(rowList)-1           
            else:
                j = colIndex-1
            if(state[i][j] == 1):
                neighboursCount += 1

            #получить элемент слева
            i = rowIndex
            if(state[i][j] == 1):
                neighboursCount += 1

            #получить элемен слева сверху
            if(rowIndex == 0):
                i = len(state)-1
            else:
                i = rowIndex-1
            if(state[i][j] == 1):
                neighboursCount += 1

            if(neighboursCount == 3 and state[rowIndex][colIndex] == 0):
                rowNewState.append(1)
            elif(neighboursCount < 2 or neighboursCount > 3):
                rowNewState.append(0)
            else:
                rowNewState.append(state[rowIndex][colIndex])
            
        newState.append(rowNewState)
    return newState



#инициализация игры
iterationsCount = 0
currentState = []
historyIterations = []
with open('input.txt') as file:
    for index, line in enumerate(file):
        data = line.strip()
        if(index == 0):            
            iterationsCount = int(data)
        else:
            row = []            
            for item in data.split():
                row.append(int(item))
            currentState.append(row)
    historyIterations.append(currentState)

if(iterationsCount > 20 or iterationsCount < 1):
    print('количество шагов должно быть от 1 до 20')
    exit()

if(len(currentState) != len(currentState[0]) or len(currentState) < 1 or len(currentState) > 20 or len(currentState[0]) < 1 or len(currentState[0]) > 20):
    print('количество строк и столбцов должно быть равно и не превышать 20 ')
    exit()

#выполнить указанное количество утераций
for iter in range(iterationsCount):
    currentState = makeIteration(currentState)
    historyIterations.append(currentState)

with open('output.txt', 'w') as file:
    result = []
    for line in currentState:
        result.append(' '.join(str(item) for item in line))
    file.write('\n'.join(result))