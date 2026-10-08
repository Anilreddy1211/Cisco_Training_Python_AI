"""
Demonstrates weak aggregation between a Department and a Teacher.

In weak aggregation, the Teacher object is created independently
and then passed to the Department object.
The Department only stores a reference to the Teacher.
"""

class Teacher:
    """Represents a Teacher."""

    def __init__(self, name):
        self.name = name

    def teach(self):
        print(self.name, "is teaching")


class Dept:
    """Represents a Department.

    Dept receives an already-created Teacher object.
    It does not create the Teacher itself.
    """

    def __init__(self, teacher):
        self.teacher = teacher

    def show_teacher(self):
        print("Department Teacher:", self.teacher.name)

    def start_class(self):
        self.teacher.teach()


# --------------------------------------------------
# Teacher object is created independently
# --------------------------------------------------

teacher1 = Teacher("Ram")

# Department object receives the existing Teacher object
dept1 = Dept(teacher1)


# --------------------------------------------------
# Using Department methods
# --------------------------------------------------

dept1.show_teacher()

dept1.start_class()


# --------------------------------------------------
# Teacher can still be used independently
# --------------------------------------------------

teacher1.teach()


# --------------------------------------------------
# Same Teacher can be associated with another Dept
# --------------------------------------------------

dept2 = Dept(teacher1)

dept2.show_teacher()
dept2.start_class()