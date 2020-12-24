class Calc():
#init metodu
    def __init__(self, a, b):
    #atributes
        self.value1 = a
        self.value2 = b
    def Add(self):
        return self.value1 + self.value2 
    def Multiply(self):
        return self.value1 * self.value2
    def Division(self):
        return self.value1 / self.value2
    def Substriction(self):
        return self.value1 - self.value2 
    
print("Choose Add(1), Multiply(2), Division(3), Substriction(4)")
selection = input("select 1 ,2 ,3 ,4 : ")
v1 = int(input("First Value : ", ))
v2 = int(input("Second Value : ", ))
c1 = Calc(v1, v2)
if selection == "1" :
        addresult = c1.Add()
        print("Add = {}".format(addresult))
elif selection == "2" :
    multiplyresult = c1.Multiply()
    print("Multiply = {}".format(multiplyresult))
elif selection == "3" :
        divisionresult = c1.Division()
        print("Division = {}".format(divisionresult)) 
elif selection == "4" :
        substrictionresult = c1.Substriction()
        print("Substriction = {}".format(substrictionresult))
else :
        print("Error")
print("Thank You For Using Calculator")