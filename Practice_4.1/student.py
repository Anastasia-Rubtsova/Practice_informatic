class Student:
    def __init__(self, name):
        self.name = name
        self._grades = {}

    def add_grade(self, subject, grade):
        if grade not in (2, 3, 4, 5):
            raise ValueError("Оценка должна быть от 2 до 5")
        if subject not in self._grades:
            self._grades[subject] = []
        self._grades[subject].append(grade)

    def average(self, subject=None):
        if subject is not None:
            if subject not in self._grades:
                raise KeyError("Предмет не найден")
            grades = self._grades[subject]
        else:
            grades = []
            for subj in self._grades:
                for g in self._grades[subj]:
                    grades.append(g)
        if len(grades) == 0:
            return 0.0
        return sum(grades) / len(grades)

    def subjects(self):
        result = list(self._grades.keys())
        result.sort()
        return result

    def debts(self):
        result = []
        for subj in self._grades:
            grades = self._grades[subj]
            avg = sum(grades) / len(grades)
            if avg < 3:
                result.append(subj)
        result.sort()
        return result

    def __lt__(self, other):
        return self.average() < other.average()

    def __repr__(self):
        avg = self.average()
        return f"Student('{self.name}', {avg:.2f})"


class Group:
    def __init__(self, name):
        self.name = name
        self._students = []

    def add(self, student):
        if isinstance(student, Student) == False:
            raise TypeError("Должен быть студент")
        for s in self._students:
            if s.name == student.name:
                raise ValueError("Студент с таким именем уже есть")
        self._students.append(student)

    def __len__(self):
        return len(self._students)

    def __contains__(self, name):
        for s in self._students:
            if s.name == name:
                return True
        return False

    def ranking(self):
        result = list(self._students)
        result.sort(key=lambda s: (-s.average(), s.name))
        return result

    def with_debts(self):
        result = []
        for s in self._students:
            if len(s.debts()) > 0:
                result.append(s.name)
        result.sort()
        return result
