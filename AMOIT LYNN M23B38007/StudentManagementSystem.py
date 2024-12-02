def add_student(student_list, student_id, name, age, course):
    """Adds a new student to the student list.

    Args:
        student_list (list): The list to store student data.
        student_id (int): The unique ID of the student.
        name (str): The student's name.
        age (int): The student's age.
        course (str): The student's course.

    Raises:
        ValueError: If a student with the same ID already exists.
    """

    if any(student['id'] == student_id for student in student_list):
        raise ValueError("Error: Student ID already exists!")

    student = {
        'id': student_id,
        'name': name,
        'age': age,
        'course': course
    }
    student_list.append(student)

def find_student_by_id(student_list, student_id):
    """Finds a student by their ID in the student list.

    Args:
        student_list (list): The list containing student data.
        student_id (int): The ID of the student to find.

    Returns:
        dict or None: The student dictionary if found, otherwise None.
    """

    for student in student_list:
        if student['id'] == student_id:
            return student
    return None

def remove_student_by_id(student_list, student_id):
    """Removes a student from the student list by their ID.

    Args:
        student_list (list): The list containing student data.
        student_id (int): The ID of the student to remove.

    Returns:
        bool: True if the student was removed, False otherwise.
    """

    for i, student in enumerate(student_list):
        if student['id'] == student_id:
            del student_list[i]
            return True
    return False

class Person:
    """Base class representing a person with name and age attributes."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        """Returns a string representation of the person."""
        return f"{self.name}, Age: {self.age}"

class Student(Person):
    """Class representing a student inheriting from Person."""

    def __init__(self, name, age, course):
        super().__init__(name, age)  # Call the parent class constructor
        self.course = course

    def study(self):
        """Prints a message indicating the student is studying."""
        print(f"Student {self.name} is studying {self.course}.")

class Instructor(Person):
    """Class representing an instructor inheriting from Person."""

    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def teach(self):
        """Prints a message indicating the instructor is teaching."""
        print(f"Instructor {self.name} is teaching {self.subject}.")

# Example usage
student = Student("Lynn", 23, "Math")
instructor = Instructor("Bob", 35, "Physics")

student.study()
instructor.teach()

def sort_students(student_list, key_function):
    """Sorts the student list based on the provided key function.

    Args:
        student_list (list): The list containing student data.
        key_function (callable): A function that takes a student dictionary
                                  and returns a value to sort by.

    Returns:
        list: A new list containing the sorted students.
    """

    return sorted(student_list, key=key_function)

students = [
    {'id': 1, 'name': 'Charlie', 'age': 22, 'course': 'History'},
    {'id': 2, 'name': 'Alice', 'age': 20, 'course': 'Math'},
    {'id': 3, 'name': 'Eve', 'age': 21, 'course': 'Biology'},
]

# Sorting by age
sorted_by_age = sort_students(students, key_function=lambda x: x['age'])
print("Sorted