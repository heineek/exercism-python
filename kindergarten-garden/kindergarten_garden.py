class Garden(object):
    plants_dict = {"G": "Grass", "C": "Clover", "R": "Radishes", "V": "Violets"}

    def __init__(self, plants_str, students=["Alice", "Bob", "Charlie", "David",
                                         "Eve", "Fred", "Ginny", "Harriet",
                                         "Ileana", "Joseph", "Kincaid", "Larry"]):
        students.sort()
        self.students_plants = dict.fromkeys(students)

        row_1 = [plant for plant in plants_str.split('\n')[0]]
        row_2 = [plant for plant in plants_str.split('\n')[1]]

        if len(row_1) != len(row_2):
            raise ValueError

        plants_groups = []

        for i in range(0, len(row_1) - 1, 2):
            plants_for_student = row_1[i:i+2]
            plants_for_student.extend(row_2[i:i+2])
            plants_groups.append(plants_for_student)

        if len(students) > len(plants_groups):      # too few of plants for all children
            children_with_plants = students[0:len(plants_groups)]
        else:
            children_with_plants = students.copy()

        for num, name in enumerate(children_with_plants):
            self.students_plants[name] = plants_groups[num]

    def plants(self, name):
        result = [self.plants_dict[plant] for plant in self.students_plants[name]]
        return result