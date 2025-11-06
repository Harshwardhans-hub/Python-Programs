operator = ["+","-","*","/","%","^"]
numerals = ["0","1","2","3","4","5","6","7","8","9"]

# Converts the user-provided expression from string into list with distinct elements
def main_body():
    global user_input
    print("Note: Please enter negative numbers within brackets in expression if any.")
    user_input = input("Input arithmetic expression: ")
    expression = []
    term = ""

    # Handle implicit multiplication when something like 3(-4) is encountered
    user_input = user_input.replace("(-", "(0-")  # Handle expressions like 3(-4) as 3*(0-4)

    for i in user_input:
        if i in operator:
            expression.append(term)
            expression.append(i)
            term = ""
        else:
            term += i
    else:
        expression.append(term)

    return expression

# Checks if the user-provided expression is valid or not
def validation():
    expression = main_body()
    for i in range(len(expression)):
        if i % 2 == 0:
            if not expression[i].replace('-', '').isnumeric():  # Allow negative numbers
                return "Not a valid expression."
        elif i % 2 != 0:
            if expression[i] not in operator:
                return "Not a valid expression."
    return expression

# Stack push and pop operations (Stack Implementation)
class stack:
    def __init__(self):
        self.list_1 = []
        self.min = -1
        self.max = -1

    def status(self):
        print(self.list_1)
        print(self.min)
        print(self.max)

    def push(self, item):
        if self.list_1 == []:
            self.list_1.append(item)
            self.min += 1
            self.max += 1
        else:
            self.list_1.append(item)
            self.max += 1

    def pop(self):
        if self.list_1 == []:
            print("Stack is empty. Pop operation cannot be performed.")
        else:
            result = self.list_1.pop()
            self.max -= 1
        return result

Priority = {'+':1, '-':1, '*':2, '/':2, '^':3}

# Converts the infix to postfix expression
def infix_to_postfix(expression):
    s1 = stack()
    infix_expression = expression
    postfix_expression = []

    for i in infix_expression:
        if i not in operator:
            postfix_expression.append(i)
        else:
            if s1.max == -1:
                s1.push(i)
            else:
                c = s1.list_1[s1.max]
                x = Priority[c]
                y = Priority[i]
                if x >= y:
                    z = s1.pop()
                    postfix_expression.append(z)
                    s1.push(i)
                else:
                    s1.push(i)
    else:
        for j in range(len(s1.list_1)):
            z = s1.pop()
            postfix_expression.append(z)
    return postfix_expression

# Evaluates the postfix expression
def solve(opr_1, opr_2, operator):
    if operator == "+":
        return int(opr_1) + int(opr_2)
    elif operator == "-":
        return int(opr_1) - int(opr_2)
    elif operator == "/":
        return int(opr_1) / int(opr_2)
    elif operator == "*":
        return int(opr_1) * int(opr_2)
    return 0

def solution(postfix_expression):
    s2 = stack()

    for ele in postfix_expression:
        if ele not in operator:
            s2.push(ele)
        else:
            operand_2 = s2.pop()
            operand_1 = s2.pop()
            temp = solve(operand_1, operand_2, ele)
            s2.push(temp)
    result = s2.pop()
    return result

def main():
    arithmatic_expression = validation()

    if arithmatic_expression == "Not a valid expression":
        print("Invalid expression")
    else:    
        print("Infix Expression : ", " ".join(arithmatic_expression))  # prints the infix expression as a string
        postfix_expression = infix_to_postfix(arithmatic_expression)
        print("Postfix Expression : ", " ".join(postfix_expression))    # prints the postfix expression as a string
        result = solution(postfix_expression)
        print("Result : ", result)

main()
