class Employee:
    
    @staticmethod
    def calculate_salary(hour_salary,hour_worked):
        return(hour_salary * hour_worked)
    
    @staticmethod
    def calculate_bonus(experience,salary):
        if experience < 1:
            return salary / 100
        elif experience < 3:
            return salary * 5 / 100
        elif experience < 5:
            return salary * 8 / 100
        else:
            return salary * 15 / 100
    
    def __init__(self,fio,experience,hour_salary,hour_worked):
        self.fio = fio
        self.experience = float(experience)
        self.hour_salary =float(hour_salary)
        self.hour_worked =float(hour_worked)
        self.salary = self.calculate_salary(self.hour_salary,self.hour_worked)
        self.bonus = self.calculate_bonus(self.experience,self.salary)
        
        
    def print(self):
        print("FIO = ",self.fio)
        print("Experience = ",self.experience)
        print("Hour salary = ",self.hour_salary)
        print("Hour worked = ",self.hour_worked)
        print("Salary = ",self.salary)
        print("Bonus = ",self.bonus)
        
def create_employee():
    fio = input("FIO : ")
    experience = input("Experience : ")
    hour_salary = input("Hour salary : ")
    hour_worked = input("Hour worked : ")
    person = Employee(fio,experience,hour_salary,hour_worked)
    return person

size = input("How much employees : ")
lst= []

for i in range(0,int(size)):
    lst.append(create_employee())
     
for i in range(0,int(size)):
     lst[i].print()

        



