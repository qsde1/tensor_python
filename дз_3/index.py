class Stack:
    s = []

    # удалить последний элемент из стека и вернуть его
    def pop(self):
        if self.s.__len__() == 0:
            return None
        else:
            last = self.s[-1]
            self.s.pop()
            return last
    
    # добавить новый элемент в конец стека
    def push(self,item):
        self.s.append(item)
    
    def __len__(self):
        return self.s.__len__()
    
def checkBrackets(str):
    s = Stack()
    dict = {
        '(' : ')',
        '{' : '}',
        '[' : ']',
    }
    isValid = True
    index = 0
    for char in str:
        index += 1
        # открывающие скобки помещаются в стек
        if char == '{' or char == '[' or char == '(':
            s.push(char)
        # закрывающие скобки сравниваются с открывающими из стека
        elif char == '}' or char == ']' or char == ')':
            lastItem = s.pop()

            if lastItem == None or dict[lastItem] != char:
                isValid = False
                break
    
    if(len(s) != 0):
        isValid = False
    
    if isValid:
        return 'Success'
    else:
        return index    

while True:
    str = input('введите строку: ')

    if len(str) > 1000:
        print('длина строки не должна превышать 1000 символов')
        continue

    print(checkBrackets(str))
    break