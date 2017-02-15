class Shaurma:
    def __init__(self, kind, cost, size):
        self.kind = kind
        self.cost = cost
        self.__size = size
    
    def poison(self, eater):
        if self.__size > 0:
            print("{0}, был отравлен {1.kind}ой шаурмой".format(
                eater,self))
            self.__size -= 5 
        else:
            print("Шаурмы больше нет")

    def __str__(self):
        



    @property        
    def size(self):
        return self.__size        

chicken_shaurma = Shaurma("Курин", 70, 15)
print(chicken_shaurma)  
chicken_shaurma.poison("Джавид")    

chicken_shaurma = Shaurma("Мясная в булочке", 70, 15)
print(chicken_shaurma)  
chicken_shaurma.poison("Амин")  
chicken_shaurma.poison("Кадыр")
chicken_shaurma.poison("Гуд")
#
chicken_shaurma.poison("Камал")