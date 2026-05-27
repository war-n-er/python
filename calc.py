class Calculator:
    def __init__(self, result=0, function=None): 
        self.result = result
        self.function = function

    def add(self, num):
        self.result += num
        return self.result
    
    def subtract(self, num):
        self.result -= num
        return self.result
    
    def multiply(self, num): 
        self.result *= num
        return self.result
    
    def divide(self, num):
        if num != 0:
            self.result /= num
            return self.result
        else:
            return "ERROR: a ÷ 0 is undefined for any a ≠ 0"
        
end_user = input("type your function: ")
result = eval(end_user)
print(result)
#MAY 26 NATALIE WARNER
