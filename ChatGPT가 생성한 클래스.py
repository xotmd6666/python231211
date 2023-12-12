class Person:
    def __init__(self, person_id, name, phone_num):
        self.id = person_id
        self.name = name
        self.phone_num = phone_num

    def print_info(self):
        print(f"ID: {self.id}, Name: {self.name}, Phone Number: {self.phone_num}")


class Manager(Person):
    def __init__(self, person_id, name, phone_num, skill):
        super().__init__(person_id, name, phone_num)
        self.skill = skill


class Employee(Person):
    def __init__(self, person_id, name, phone_num, title):
        super().__init__(person_id, name, phone_num)
        self.title = title


class Alba(Person):
    pass


# 샘플 코드
people_list = [
    Manager(1, "Manager1", "123-456-7890", "Leadership"),
    Employee(2, "Employee1", "987-654-3210", "Developer"),
    Alba(3, "Alba1", "111-222-3333"),
    Manager(4, "Manager2", "444-555-6666", "Communication"),
    Employee(5, "Employee2", "777-888-9999", "Designer"),
    Alba(6, "Alba2", "555-444-3333"),
    Manager(7, "Manager3", "111-222-3333", "Problem Solving"),
    Employee(8, "Employee3", "999-888-7777", "Analyst"),
    Alba(9, "Alba3", "777-666-5555"),
    Manager(10, "Manager4", "333-444-5555", "Team Building"),
]

# 출력
for person in people_list:
    person.print_info()
    if isinstance(person, Manager):
        print(f"Skill: {person.skill}")
    elif isinstance(person, Employee):
        print(f"Title: {person.title}")
    print()
