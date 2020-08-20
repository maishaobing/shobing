#方案一
def collatz(number):
    """奇偶判断"""

    if number % 2 == 0:
        number1=number // 2
        return number1
        
    else:
         number2 = 3*number + 1
         return number2
print('输入一个数:')
Inputnumber = int(input())
      
while Inputnumber != 1:
    
    #collatz(Inputnumber)
    
    Inputnumber = collatz(Inputnumber)
    print(Inputnumber)
    if Inputnumber == 1:
        print(Inputnumber)
        break
#方案二

def collatz(number):
    """奇偶判断"""

    if number % 2 == 0:
        number1=number // 2
        return number1
        
    else:
         number2 = 3*number + 1
         return number2
print('输入一个数:')
Inputnumber = int(input())
      
while Inputnumber != 1:
    
    print(collatz(Inputnumber))
    Inputnumber = collatz(Inputnumber)
    
    if Inputnumber == 1:
        print(Inputnumber)
        break


#烧脑分析：方案一“collatz(Inputnumber)”函数被调用却没有输出，接着执行print(),因此可以删除“collatz(Inputnumber)”
        #也可以用print(collatz(Inputnumber)输出，如方案二。
      
    
