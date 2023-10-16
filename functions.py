class cse:
    def fun(self):
        print("hi")
o=cse()
o.fun()

class cse:
    def __init__(self,a):
        print("hiii",a)
    def fun(s):
        print("hello")
o=cse(2)
o.__init__(5)
o.fun()

class cse:
    def __init__(self,a):
        print("hiii",a)
    def fun(s,b,c):
        print("hello",b,c)
o=cse(2)
o.__init__(5)
o.fun(9,'bye')

class cse:
    def __init__(self,a):
        print("hiii",a)
    def fun(s,b,c):
        print("hello",b,c)
o=cse(2)
o.__init__(5)
o.fun(9,'bye')


class cse:
    def __init__(self,a):
        self.a=0
    def fun(s):
        print("hello",s.a)
o=cse(2)
b=cse(5)
b.fun(5)


