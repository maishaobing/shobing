class Dog():
    """一次模拟小狗的简单尝试"""
    def __init__(self,name,age):#注意这里‘__’是两个‘_’而非一个
        """初始化属性name和age"""
        self.name = name
        self.age = age
        
    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + "is now sitting")
        
    def roll_over(self):
        """命令小狗时打滚"""
        print(self.name.title() + "rolled over!")
        
my_dog = Dog('wille',6)
print('my dog name is ' + my_dog.name.title() + '!')
print('my dog is ' + str(my_dog.age) + ' years old!')