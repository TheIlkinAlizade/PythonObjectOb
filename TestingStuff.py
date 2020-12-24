# %% attribute
class Programmers(object):
    name = 'Aliesso'
    age = 30
    projects = "Python"
Pr1 = Programmers()
print(Pr1.age)
#%% section
class Square(object):
    edge = 5
    area = 0
    def Area(self):
        self.area = self.edge * self.edge
        print("cavab", self.area)
S = Square()
print(S.Area())
