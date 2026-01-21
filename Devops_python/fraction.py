class Fraction:
    def __init__(self,n,d):
        self.num=n
        self.den=d
    def __str__(self):
        return "{}/{}".format(self.num,self.den)
   
    def __add__(self,other):
        new_num=self.num*other.den+other.num*self.den
        new_den=self.den*other.den
        return "{}/{}".format(new_num,new_den)
    def __sub__(self,other):
        new_num=self.num*other.den-other.num*self.den
        new_den=self.den*other.den
        return "{}/{}".format(new_num,new_den)
    def __mul__(self,other):
        new_num=self.num*other.num
        new_den=self.den*other.den
        return "{}/{}".format(new_num,new_den)
    def __truediv__(self,other):
        new_num=self.num*other.den
        new_den=self.den*other.num
        return "{}/{}".format(new_num,new_den)

