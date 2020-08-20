print("欢迎大家来到这里")
def printTable(stohhd):

    
   for h in tableData:
        t=h[range(len(tableData)+1)]
        m=t[int(range(len(t)+1))]
        print(m.rjust())

tableData = [['apples','oranges','cherries','banana'],
             ['Alice','Bob','Carol','David'],
             ['dogs','cat','moose','goose']]



printTable(tableData)



             
