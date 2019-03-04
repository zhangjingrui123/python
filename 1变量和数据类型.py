# （一）整型(int)，浮点型(float)，字符串型(str)
print("hello python")   

# （二）字符串拼接
first_name = "zjr"
last_name = "abc"
full_name = first_name + " " + last_name  
print(full_name)

#（三）换行符:\n\t
print("language:\n\tPython\n\tHtml")  

#（四）元组封装和拆封
data = ("python","china","fibos")
language,counry,name = data

#（五）修改字符串大小写
message = 'my name is zjr'
print(message.upper())   #所有字母大写
print(message.lower())   #所有字母小写
print(message.title())   #所有首个字母大写
print(message.capitalize())#开头首字母大写
print(message.swapcase())#对字符串大小写字母进行转换

#（六）if语句
number = int(input("enter an inter:"))  #input()输入
if number <= 100:
    print("your number is less than or equal to 100")
else:
    print("your number is greater than 100")

#（七）while循环语句
N = 10
sum = 0
count = 0
print("please input 10 numbers:")
while count < N:
    number = float(input())
    sum = sum + number
    count = count + 1
average = sum / N
print("N = {}, sum = {}".format(N,sum))     #format函数    
print("average = {:.2f}".format(average))   #{:.2f}保留小数点后两位
