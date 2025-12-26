class Employee:
   def __init__(self, name, id):
       self.name = name
       self.id = id
   def get_info(self): 
       return f'Сотрудник: {self.name}, ID: {self.id}'

class Manager(Employee):
   def __init__(self, name, id, department):
        Employee.__init__(self, name, id)
        self.department = department
   def manage_project(self):
        return f"{self.name} управляет проектом в отделе '{self.department}'"
   def get_info(self):
        return f'Менеджер: {self.name}, ID: {self.id}, Отдел: {self.department}'

class Technician(Employee):
   def __init__(self, name, id, specialization):
       Employee.__init__(self, name, id)
       self.specialization = specialization
   def perform_maintenance(self):
       return f'{self.name} выполняет обслуживание: {self.specialization}'
   def get_info(self):
       return f'Техник: {self.name}, ID: {self.id}, Специализация: {self.specialization}'

class TechManager(Manager, Technician):
    def __init__(self, name, id, department, specialization):
        Manager.__init__(self, name, id, department)
        Technician.__init__(self, name, id, specialization)
        self.__team = [] 
    def add_employee(self, employee):
        self.__team.append(employee)
    def get_team_info(self):
        if not self.__team:
            return f'У {self.name} нет подчинённых.'
        result = f'Подчинённые {self.name}:\n'
        for emp in self.__team:
            result += f'- {emp.get_info()}\n'
        return result.strip()
    def get_info(self):
        return (f'Технический менеджер: {self.name}, ID: {self.id}, '
                f'Отдел: {self.department}, Специализация: {self.specialization}')

emp = Employee('Иван Ермаков', 10)
mgr = Manager('Мария Балюра', 11, 'Разработка')
tech = Technician('Андрей Симонов', 12, 'Электрика')

tech_mgr = TechManager('Сергей Кузнецов', 20, 'ИТ', 'Сети и связи')
tech_mgr.add_employee(emp)
tech_mgr.add_employee(mgr)
tech_mgr.add_employee(tech)

print(emp.get_info())
print(mgr.get_info())
print(tech.get_info())
print(tech_mgr.get_info())
print(tech_mgr.manage_project())
print(tech_mgr.perform_maintenance())
print(tech_mgr.get_team_info())