class Employee:
    def __init__(self, name: str, emp_id: int):
        self.__name = name
        self.__id = emp_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Имя не может быть пустым")
        self.__name = value

    @property
    def id(self):
        return self.__id

    def get_info(self):
        return f"Сотрудник: {self.name}, ID: {self.id}"


class Manager(Employee):
    def __init__(self, name: str, emp_id: int, department: str):
        super().__init__(name, emp_id)
        self.department = department

    def manage_project(self, project_name: str):
        return f"Менеджер {self.name} управляет проектом '{project_name}'"


class Technician(Employee):
    def __init__(self, name: str, emp_id: int, specialization: str):
        super().__init__(name, emp_id)
        self.specialization = specialization

    def perform_maintenance(self):
        return f"Техник {self.name} выполняет обслуживание в области '{self.specialization}'"


class TechManager(Manager, Technician):
    def __init__(self, name: str, emp_id: int, department: str, specialization: str):
        Employee.__init__(self, name, emp_id)
        self.department = department
        self.specialization = specialization
        self.team = []

    def get_info(self):
        return (
            f"ТехМенеджер: {self.name}, ID: {self.id}, "
            f"Отдел: {self.department}, Специализация: {self.specialization}"
        )

    def add_employee(self, employee: Employee):
        self.team.append(employee)

    def get_team_info(self):
        if not self.team:
            return "Список подчинённых пуст."

        info = "Подчинённые сотрудники:\n"
        for emp in self.team:
            info += " - " + emp.get_info() + "\n"
        return info


employee = Employee("Иосиф Сталин", 101)
manager = Manager("Nikolas Jackson", 102, "Отдел лучших ударов")
technician = Technician("Субо братик", 103, "Сетевые технологии")
tech_manager = TechManager("Завгороднев Ярослав", 104, "IT-отдел", "Кунилингус")

print(employee.get_info())
print(manager.get_info())
print(manager.manage_project("CRM-система"))
print(technician.get_info())
print(technician.perform_maintenance())
print(tech_manager.get_info())

tech_manager.add_employee(employee)
tech_manager.add_employee(manager)
tech_manager.add_employee(technician)

print("\n" + tech_manager.get_team_info())
print(tech_manager.manage_project("Система безопасности"))
print(tech_manager.perform_maintenance())