class School(object):

    def __init__(self, school_name):
        self.school_name = school_name
        self.students = []

    def add(self, name, grade):
        self.students.append((name, grade))

    def grade(self, grade):
        result = [student[0] for student in self.students if student[1] == grade]
        return tuple(result)

    def sort(self):
        def take_name(item):
            return(item[0])

        def take_grade(item):
            return(item[1])

        # firstly sort by grade, than by name
        self.students.sort(key=take_grade)
        grouped_by_grade = []
        for current_grade in range(1, 11):
            current_grade_list = [student for student in self.students if take_grade(student) == current_grade]
            if current_grade_list:
                grouped_by_grade.append(current_grade_list)

        for list_ in grouped_by_grade:
            list_.sort(key=take_name)

        self.students.clear()
        for list_ in grouped_by_grade:
            for item in list_:
                self.students.append(item)