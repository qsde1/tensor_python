class Stack:
    s = []
    def pop(self):
        if self.s.__len__() == 0:
            return None
        else:
            last = self.s[-1]
            self.s.pop()
            return last
    
    def push(self,item):
        self.s.append(item)
    
    def __len__(self):
        return self.s.__len__()

    def __str__(self):
        return self.s.__str__()
    
s = Stack()

dict = {
    '(' : ')',
    '{' : '}',
    '[' : ']',
}

str = '[][]{}[{{()}}]'
success = True
for char in str:
    # открывающиеся скобки кладутся в стек
    if char == '{' or char == '[' or char == '(':
        s.push(char)
    # закрывающиеся скобки сравниваются с открывающимеся из стека
    elif char == '}' or char == ']' or char == ')':
        lastItem = s.pop()
        if(lastItem == None):
            success = False
            break
        elif dict[lastItem] != char:
            success = False
            break

if(s.__len__() != 0):
    success = False

print(success)


