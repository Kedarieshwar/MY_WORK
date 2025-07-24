print("Select the operation you want to use")
print("""1.Addition
2.Subtraction
3.Multiplication
4.Division
5.Square root""")
oper=int(input("Select operation from above:"))

class scientificcalc:
    def add(self,a,b):
        return a+b

    def sub(self,a,b):
        return a-b

    def mult(self,a,b):
        return a*b

    def div(self,a,b):
        return a/b

    def sqrt(self,a):
        return a*a
 

calc = scientificcalc()

if oper == 5:
    inp1 = float(input("Enter number to find the square root of: "))
    print("Result:", calc.sqrt(inp1))

inp1 = float(input("Enter first number: "))
inp2 = float(input("Enter second number: "))

if oper == 1:
    print("Result:", calc.add(inp1, inp2))
elif oper == 2:
    print("Result:", calc.sub(inp1, inp2))
elif oper == 3:
    print("Result:", calc.mult(inp1, inp2))
elif oper == 4:
    print("Result:", calc.div(inp1, inp2))

else:
    print("Invalid operation selected.")