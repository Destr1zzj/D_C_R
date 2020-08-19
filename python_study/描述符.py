class MY1:
    def __get__(self,instance,owner):
        print('geting',self,instance,owner)
    def __set__(self, instance, value):
        print('set..',self, instance, value)
    def __delete__(self, instance):
        print('del..',self, instance)

class Test:
    x = MY1()

class MY:
    def __init__(self,fget = None,fset = None,fdel = None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel

    def __get__(self, instance, owner):
        return self.fget(instance)
    def __set__(self, instance, value):
        return self.fset(instance,value)
    def __delete__(self, instance):
        return self.fdel(instance)



class C:
    def __int__(self):
        self._x = None
    def getx(self):
        return self._x
    def setx(self,value):
        self._x = value
    def delx(self):
        del self._x


        
class Cels:
    def __init__(self,value =26.0):
        self.value = float(value)
    def __get__(self, instance, owner):
        return self.value
    def __set__(self, instance, value):
        self.value = float(value)
class Fa:
    def __get__(self, instance, owner):
        return instance.cel*1.8+32
    def __set__(self, instance, value):
        instance.cel = (float(value)-32)/1.9
class Tem:
    cel = Cels()
    fa = Fa()

class Mydes:
    def __init__(self, value = None):
        self.val = value

    def __get__(self, instance, owner):
        return self.val ** 2

class ccm:
    y = Mydes(3)
    # def __init__(self):
    #     self.x = Mydes(3)
