
print("\n=========String print===========")
var_string = "hello world"
print(var_string)
var_num1 = 25
var_num2 = 10


print("\n================IF ELSE condition===============")

print("Num1 = " + str(var_num1))
print("Num2 = " + str(var_num2))
var_sum = var_num1 + var_num2;
print("Sum of Nun1 and Nun2 = " + str(var_sum))

if var_num1 < var_num2:
    print("Num1 is less than Num2")
elif var_num1 == var_num2:
    print("Num1 and Num2 are same")
else:
    print("Num1 is greater than Num2")


print("\n================Loop syntax===============")

i = 1;
while  i <= 5 :
    print("The value of i = " + str(i))
    i = i + 1


print("\n================Function syntax===============")


def addition(a, b, c = 25):     #c is default paramter
    print("a =" + str(a))
    print("b = " + str(b))
    print("c = " + str(c))
    sum_ab = a + b
    print("Sum of a and b = " + str(sum_ab))


addition(10, 40)

msg_global = "I am a global variable. Wish you a happy birthday. "
# How to access global varibale inside function


def birthday_greeting(name, msg = "Happy birthday to "):
    global msg_global
    print(msg + name)
    print(msg_global + name)


birthday_greeting("sanat")

birthday_greeting("sanat", "Wish you a very happy birthday ")

