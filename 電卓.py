def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y != 0:
        return x/y
    else:
        return "Error: Division by zero is not allowed."
def triangle(x,y):
    return (x*y)/2
def Cylinder(x,y):
    return (x*x*3.14*y)

print("計算方法を選択:")
print("1.加算","2.減算","3.乗算","4.除算","5.三角形","6.円柱")
choice = input("選択(1-6):")
num1=float(input("１つ目の数字を入力して下さい"))
num2=float(input("２つ目の数字を入力して下さい"))
if choice == "1":
    result = add(num1,num2)
    print("答え:",result)
elif choice == "2":
    result = subtract(num1,num2)
    print("答え:",result)
elif choice == "3":
    result = multiply(num1,num2)
    print("答え:",result)
elif choice == "4":
    result = divide(num1,num2)
    print("答え:",result)
elif choice == "5":
    result = triangle(num1,num2)
    print("答え:",result)
elif choice == "6":
    result = Cylinder(num1,num2)
    print("答え:",result)
else:
    print("やり直せ")