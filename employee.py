"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""


class Employee:
    def __init__(self, name):
        self.name = name

    def get_pay(self):
        pass

    def __str__(self):
        return self.name


# 1. Workers on an salary contract without commission.
class WorkerSalaryContractNoCommission(Employee):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def get_pay(self):
        return self.salary

    def __str__(self):
        return f"{self.name} works on a monthly salary of {self.salary}.  Their total pay is {self.get_pay()}."

# 2. Workers on an hourly contract without commission.
class WorkerHourlyContractNoCommission(Employee):
    def __init__(self, name, hourlyWage, hours):
        super().__init__(name)
        self.hourlyWage = hourlyWage
        self.hours = hours

    def get_pay(self):
        return self.hourlyWage * self.hours

    def __str__(self):
        return f"{self.name} works on a contract of {self.hours} hours at {self.hourlyWage}/hour.  Their total pay is {self.get_pay()}."

# 3. Workers on an salary contract with a bonus commission.
class WorkerSalaryContractWithBonusCommission(WorkerSalaryContractNoCommission):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def get_pay(self):
        return super().get_pay() + self.bonus

    def __str__(self):
        return f"{self.name} works on a monthly salary of {self.salary} and receives a bonus commission of {self.bonus}.  Their total pay is {self.get_pay()}."

# 4. Workers on an hourly contract with a bonus commission.
class WorkerHourlyContractWithBonusCommission(WorkerHourlyContractNoCommission):
    def __init__(self, name, hourlyWage, hours, bonus):
        super().__init__(name, hourlyWage, hours)
        self.bonus = bonus

    def get_pay(self):
        return super().get_pay() + self.bonus

    def __str__(self):
        return f"{self.name} works on a contract of {self.hours} hours at {self.hourlyWage}/hour and receives a bonus commission of {self.bonus}.  Their total pay is {self.get_pay()}."

# 5. Workers on an salary contract with a contract commission.
class WorkerSalaryContractWithContractCommission(WorkerSalaryContractNoCommission):
    def __init__(self, name, salary, bonusPerContract, numberOfContracts):
        super().__init__(name, salary)
        self.bonusPerContract = bonusPerContract
        self.numberOfContracts = numberOfContracts

    def get_pay(self):
        return super().get_pay() + self.bonusPerContract * self.numberOfContracts

    def __str__(self):
        return f"{self.name} works on a monthly salary of {self.salary} and receives a commission for {self.numberOfContracts} contract(s) at {self.bonusPerContract}/contract.  Their total pay is {self.get_pay()}."

# 6. Workers on an hourly contract with a contract commission.
class WorkerHourlyContractWithContractCommission(WorkerHourlyContractNoCommission):
    def __init__(self, name, hourlyWage, hours, bonusPerContract, numberOfContracts):
        super().__init__(name, hourlyWage, hours)
        self.bonusPerContract = bonusPerContract
        self.numberOfContracts = numberOfContracts

    def get_pay(self):
        return super().get_pay() + self.bonusPerContract * self.numberOfContracts

    def __str__(self):
        return f"{self.name} works on a contract of {self.hours} hours at {self.hourlyWage}/hour and receives a commission for {self.numberOfContracts} contract(s) at {self.bonusPerContract}/contract.  Their total pay is {self.get_pay()}."

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = WorkerSalaryContractNoCommission('Billie', 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = WorkerHourlyContractNoCommission('Charlie', 25, 100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = WorkerSalaryContractWithContractCommission('Renee', 3000, 200, 4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = WorkerHourlyContractWithContractCommission('Jan', 25, 150, 220, 3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = WorkerSalaryContractWithBonusCommission('Robbie', 2000, 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = WorkerHourlyContractWithBonusCommission('Ariel', 30, 120, 600)

