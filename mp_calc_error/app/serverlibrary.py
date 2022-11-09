def merge(array, byfunc, p,q,r):    # byfunc takes in a function. This function can be in the form of lambda or as the question presents it, the select function.

    # mergesort similar to the cohort question.
    left_array = array[p:q+1]
    right_array = array[q+1:r+1]

    left_index = 0
    right_index = 0 
    dest = p
    
    len_left = q-p + 1 # end of the left array
    len_right = r-q # end of the right array


    #print("left array:", left_array, "right array:", right_array, len_left, len_right)
    while left_index < len_left and right_index < len_right: # checking if both left and right array are both non-empty lists.
        
        if byfunc == None:  # user did not specify a particular function. sorting values as a typical mergesort.

            # compare values of the left and right array according to it's corresponding indexes. 
            if left_array[left_index] <= right_array[right_index]:
                array[dest] = left_array[left_index]
                left_index += 1 # move to the next index for the left array if the left array value is larger than the right. Replaces the destination's (index) value.
            
            else: # move to the next index for the right array if the right array value is larger than the left. Replaces the main array destination's (index) value.
                array[dest] = right_array[right_index]
                right_index += 1
            
            # move the index of the main array to the next position.
            dest += 1            
        
        else:
            #print("case 1", left_index, right_index, dest)
            #print(byfunc(left_array[left_index]),byfunc(right_array[right_index]))

            # The byfunc helps us to select a value. In the case of tuples/question context, if we specify the function as lambda value: value[0], we will be comparing the values of the first position in the tuple.
            if byfunc(left_array[left_index]) <= byfunc(right_array[right_index]):  # left_array[left_index][0] <= right_array[right_index][0]  (following the context of the question, sorting by the first element of a tuple)
                array[dest] = left_array[left_index]
                left_index += 1
                
            
            else:
                #print(byfunc(left_array[left_index]),byfunc(right_array[right_index]) )
                array[dest] = right_array[right_index]
                right_index += 1
        
            dest += 1

    # left array is not empty but right array is empty.
    while left_index < len_left:
        #print(dest, len_left)
        array[dest] = left_array[left_index]
        left_index += 1
        dest += 1

    # right array is not empty but left array is empty.
    while right_index < len_right:
        #print(dest, right_index, len_right)
        array[dest] = right_array[right_index]
        right_index += 1
        dest += 1
    
    return array

# helper function for recursion
def mergesort_recursive(array, byfunc, p, r):
    if r-p > 0:
        q = (r+p)//2
        mergesort_recursive(array,byfunc, p, q)
        mergesort_recursive(array,byfunc, q+1, r)
        merge(array,byfunc, p, q, r)
        
# exists to call the recursive function.
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

    ## Format the expression to make it easier to evaluate ##

    # filter out the empty spaces
    edited_tokens = list(filter(None, tokens)) #remove empty "" from the list in tokens\
    for i in range(len(edited_tokens)):
      # accounting for numbers with more than one digit.
      if len(edited_tokens[i]) > 1:
        new_index = i

        # for a 2 digit number, loop through each digit and append the digit into the edited_tokens list.
        for j in range(len(edited_tokens[i])): 
          char = edited_tokens[i][j]
          new_index += 1
          edited_tokens.insert(new_index, char)
          print(edited_tokens)

        edited_tokens.remove(edited_tokens[i]) #remove the number with more than 1 digit.
        
    #print(edited_tokens)
    #print(operator_stack.view)
    print(edited_tokens)


    ## evaluation process ##

    # note: edited tokens stay constant throughout, no popping/appending. It is a list of the characters of the given expression in the argument of the function.
    for index in range(len(edited_tokens)):
      #print(edited_tokens[index])
      if edited_tokens[index] in self.operands: # check if its a number.

        if index == 1 and edited_tokens[index-1]  == "-": # check for negative value for the first character by checking if the previous index is a minus sign.

          #for the scenario of -2 + 2, remove the - from the operator and push -2 instead
          operand_stack.push("-" + edited_tokens[index])
          operator_stack.pop()

        # account for negative value as the first number inside a bracket.
        elif edited_tokens[index-1]  == "-" and edited_tokens[index-2]  == "(":
          operand_stack.push("-" + edited_tokens[index])
          operator_stack.pop()

        # account for numbers with more than 1 digit eg: 12 or 123
        elif index > 0 and edited_tokens[index-1] in self.operands: 
          new_num = edited_tokens[index] # store the current element in a variable new_num
          char = operand_stack.pop() # remove the previous value from the operand stack.
          new_num = char + new_num # string concatenation.
          operand_stack.push(new_num) # push back into the stack.

        else:
          operand_stack.push(edited_tokens[index]) # just a single number.
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

        operator_stack.push(edited_tokens[index]) # push the current operator in after evaluation.
        #print(operator_stack.view)

      elif edited_tokens[index] == ")":
        while operator_stack.peek() != "(":
          self.process_operator(operand_stack, operator_stack)
        #remove the next "(" in operator_stack

        operator_stack.pop()
        #print(operator_stack.view)

    #print(operand_stack.size, operator_stack.size)
    #immediately check if there is only 1 value in operand_stack but there is an operator    
    if operand_stack.size == 1 and operator_stack.size >= 1: #for the cases of things like (2), 2+, -2, non mathematical equations as ther eis only 1 operand
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





