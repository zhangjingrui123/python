#(一)if条件控制语句:if-else-elif
num = float(input("输入一个数字："))
if num > 0:        #每个条件后面要使用：,表示接下来是满足条件后要执行的语句块
    print("ture")
elif num == 0:
    print("0")
else:
    print("flase")

#elif=else-if的缩写
num = float(input("输入一个数字："))
if num >=0:
    if num == 0:
        print("0")
    else:
        print("ture")
else:
    print("flase")

#（二）猜拳游戏(石头剪刀布)
import random    #调用random函数，用来生成随机数模块
player1 = int(input("请输入剪刀(1) 石头(2) 布(3):"))  #玩家1输入数字
player2 = int(random.randint(1,3))                   #玩家2取随机数,randint用于生成一个范围内的指定函数
print(player2)
if player1 == 1 :
    print("你出的是剪刀")
elif player1 == 2 :
    print("你出的是石头")
elif player1 == 3 :
    print("你出的是布")

if player2 == 1 :
    print("机器人出的是剪刀")
elif player2 == 2 :
    print("机器人出的是石头")
elif player2 == 3 :
    print("机器人出的是布")

if player1 == player2 :
    print("平手")
elif player1 > player2 :
    print("你赢了")
else :
    print("机器人赢了")

