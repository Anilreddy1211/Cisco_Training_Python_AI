class Enrollment:
    name = ''
    dob = ''
    place = ''

    def initialize(self, n, d, p):
        self.name = n
        self.dob = d
        self.place = p
        print(f'Emp {self.name} enrollment is done')

    def display(self):
        print(f'About {self.name} details:-')
        print(f'Name: {self.name} DOB: {self.dob} Place: {self.place}')


obj1 = Enrollment()
obj1.initialize('Arun', '1st Jan', 'Hyd')

obj2 = Enrollment()
obj2.initialize('Leo', '2nd Feb', 'Bnglr')

obj1.display()
obj2.display()

obj3 = Enrollment()
obj3.display()