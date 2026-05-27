class Calculator:
    def __init__(self, result=0, function=None): 
        self.result = result
        self.function = function

    def calculate(self):
        if self.function:
            self.result = eval(self.function)
        return self.result
    

    


























        end_user = input("type your function: ")
