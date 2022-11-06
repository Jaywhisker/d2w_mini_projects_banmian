def merge(array, byfunc, p,q,r):
    left_array = array[p:q+1]
    right_array = array[q+1:r+1]

    left_index = 0
    right_index = 0
    dest = p
    
    len_left = q-p + 1
    len_right = r-q


    #print("left array:", left_array, "right array:", right_array, len_left, len_right)
    while left_index < len_left and right_index < len_right:
        
        if byfunc == None:
            if left_array[left_index] <= right_array[right_index]:
                array[dest] = left_array[left_index]
                left_index += 1
            
            else:
                array[dest] = right_array[right_index]
                right_index += 1
            
            dest += 1            
        
        else:
            #print("case 1", left_index, right_index, dest)
            #print(byfunc(left_array[left_index]),byfunc(right_array[right_index]) )
            if byfunc(left_array[left_index]) <= byfunc(right_array[right_index]):
                array[dest] = left_array[left_index]
                left_index += 1
                
            
            else:
                #print(byfunc(left_array[left_index]),byfunc(right_array[right_index]) )
                array[dest] = right_array[right_index]
                right_index += 1
        
            dest += 1
    
    while left_index < len_left:
        #print(dest, len_left)
        array[dest] = left_array[left_index]
        left_index += 1
        dest += 1

    while right_index < len_right:
        #print(dest, right_index, len_right)
        array[dest] = right_array[right_index]
        right_index += 1
        dest += 1
    
    return array

def mergesort_recursive(array, byfunc, p, r):
    if r-p > 0:
        q = (r+p)//2
        mergesort_recursive(array,byfunc, p, q)
        mergesort_recursive(array,byfunc, q+1, r)
        merge(array,byfunc, p, q, r)
        

def mergesort(array, byfunc=None):
    mergesort_recursive(array, byfunc, 0, len(array)-1)
        

class Stack:
  def __init__(self):
    self.__items = []

  def push(self, item):
    self.__items.append(item)

  def pop(self):
    if self.is_empty == True:
      return None

    else:
      top_var = self.__items[-1]
      self.__items = self.__items[:-1]
      return top_var

  def peek(self):
    if self.is_empty == True:
      return None
    else: 
      return self.__items[-1]

  @property
  def is_empty(self):
    return not self.__items 
  
  @property
  def size(self):
    return len(self.__items)

  @property
  def view(self):
    return self.__items

class EvaluateExpression:
  valid_char = '0123456789+-*/() '
  operators = '+-*/()'
  operands = '0123456789'

  def __init__(self, string=""):
    self.expression = string


  @property
  def expression(self):
    return self._expression


  @expression.setter
  def expression(self, new_expr):
    
    valid = True
    for i in range(len(new_expr)):
      if new_expr[i] in self.valid_char: #valid string
        continue
    
      else: #invalid string
        valid = False

    if valid == True:
      self._expression = new_expr
    
    else:
      self._expression = ""


  def insert_space(self):
    edited_string = ""
    for char in self.expression:
      if char in self.operators:
        edited_string = edited_string + " " + char + " "
      
      elif char in self.operands:
        edited_string = edited_string + char
      
      else:
        continue
      
    return edited_string
    

  def process_operator(self, operand_stack, operator_stack):
    operator = operator_stack.pop()
    operand_1 = int(operand_stack.pop())
    operand_2 = int(operand_stack.pop())

    if operator == "+":
      operand_stack.push(operand_2+operand_1)
    
    elif operator == "-":
      operand_stack.push(operand_2-operand_1)

    elif operator == "*":
      operand_stack.push(operand_2 * operand_1)
    
    elif operator == "/":
      operand_stack.push(operand_2 // operand_1)

    else:
      raise AttributeError
    #print("size:", operand_stack.size)
    

    
  def evaluate(self):
    operand_stack = Stack()
    operator_stack = Stack()
    expression = self.insert_space()
    tokens = expression.split(" ")
    print(tokens)
    edited_tokens = list(filter(None, tokens)) #remove empty "" from the list in tokens\
    for i in range(len(edited_tokens)):
      if len(edited_tokens[i]) > 1:
        new_index = i
        for j in range(len(edited_tokens[i])): #backwards because we are inserting instead of appending, need reverse
          char = edited_tokens[i][j]
          new_index += 1
          edited_tokens.insert(new_index, char)
          print(edited_tokens)

        edited_tokens.remove(edited_tokens[i]) #remove the conjoint values
        
    #print(edited_tokens)
    #print(operator_stack.view)
    print(edited_tokens)

    for index in range(len(edited_tokens)):
      #print(edited_tokens[index])
      if edited_tokens[index] in self.operands:
        if index == 1 and edited_tokens[index-1]  == "-":
          #for the scenario of -2 + 2, remove the - from the operator and push -2 instead
          operand_stack.push("-" + edited_tokens[index])
          operator_stack.pop()

        elif index >0 and edited_tokens[index-1] in self.operands: #multiple digits
          a=1
          new_num = edited_tokens[index]
          while edited_tokens[index-a] in self.operands: #for as many digit values as possible
            char = operand_stack.pop() #remove the previous value
            new_num = char + new_num
            a+=1

          operand_stack.push(new_num)

        else:
          operand_stack.push(edited_tokens[index])
        #print(operator_stack.view)
      
      elif edited_tokens[index] == "(":
        if edited_tokens[index-1] == ")" and index !=0: 
          #for the scenario of (1+1)(1+1), index != 0 to prevent (1+2)*(2+3) to become *(1+2)*(2+3)
          operator_stack.push("*")
        
        elif edited_tokens[index-1] in self.operands and index != 0:
          #for the scenario of 5(4+2) to become 5*(4+2)
          operator_stack.push("*")
          
        operator_stack.push("(")
        #print(operator_stack.view)

      elif edited_tokens[index] == "+" or edited_tokens[index] == "-":
        while operator_stack.peek() != None and operator_stack.peek()!= "(": 
          #if the + is not the first operator and it is not the first thing inside the bracket
          #eg. (2+3), nothing will happen but (2+3+5) = (2+8) as process_operator is called
          self.process_operator(operand_stack, operator_stack)

        operator_stack.push(edited_tokens[index]) #add the operator as the things before were added but not this
        #print(operator_stack.view)

      elif edited_tokens[index] == "*" or edited_tokens[index] == "/":
        
        while operator_stack.peek() != None and (operator_stack.peek() == '*' or operator_stack.peek() == '/'):
          #if there is a * or / immediately before, have to process that operator first due to the rule of left to right
          self.process_operator(operand_stack, operator_stack)

        operator_stack.push(edited_tokens[index])
        #print(operator_stack.view)

      elif edited_tokens[index] == ")":
        while operator_stack.peek() != "(":
          self.process_operator(operand_stack, operator_stack)
        #remove the next "(" in operator_stack

        operator_stack.pop()
        #print(operator_stack.view)

    #print(operand_stack.size, operator_stack.size)
    #immediately check if there is only 1 value in operand_stack but there is an operator    
    if operand_stack.size == 1 and operator_stack.size >= 1: #for the cases of things like 2+, -2, non mathematical equations as ther eis only 1 operand
      raise AttributeError

    while operand_stack.size != 1: 
        self.process_operator(operand_stack, operator_stack)
        #print(operator_stack.view)

    return operand_stack.pop()
    

def get_smallest_three(challenge):
  records = challenge.records
  times = [r for r in records]
  mergesort(times, lambda x: x.elapsed_time)
  return times[:3]





