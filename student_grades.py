from sorting import random_numbers


class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

    def get_grade(self, index):
        score = self.get_by_index(index)

        if score > 90:
            return "A"
        elif score > 80:
            return "B"
        elif score > 70:
            return "C"
        elif score > 60:
            return "D"
        else:
            return "F"

    def find(self, points):
        indexes = []
        for i, score in enumerate(self.scores):
            if score == points:
                indexes.append(i)
        return indexes

    def get_sorted(self):
        values = self.scores.copy()
        n = 1
        while n < len(values):
            for i in range(len(values) - n):
                if values[i] > values[i + 1]:
                    values[i], values[i + 1] = values[i + 1], values[i]
            n += 1
        return values

    def main(self):
        students_number = self.count()
        print(f"Test počítalo: {students_number} studnetů")

        for i in range(students_number):
            result = self.get_by_index(i)
            znamka = self.get_grade(i)
            print(f"Studen {i}: {result} bodů - {znamka} známka")

        max_points = self.find(100)
        print(f"Idexy studentů, kteří měli 100 bodů: {max_points}")

        serazene_vysledky = self.get_sorted()
        print(f"Výsledky seřezené od nejhoršího po njelepšího: {serazene_vysledky}")




if __name__ == "__main__":
#     results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])
#
#     print(results.count())          # 9
#     print(results.get_by_index(2))  # 91
#     print(results.scores)           # [85, 42, 91, 67, 50, 73, 100, 38, 58]
#
#     print(results.get_grade(2))  # A (91 bodů)
#     print(results.get_grade(6))  # A (100 bodů)
#     print(results.get_grade(7))  # F (38 bodů)
#
#     print(results.find(100))  # [6]
#     print(results.find(50))  # [4]
#     print(results.find(77))  # []
#
#     print(results.get_sorted())  # [38, 42, 50, 58, 67, 73, 85, 91, 100]
#     print(results.scores)  # [85, 42, 91, 67, 50, 73, 100, 38, 58]  ← beze změny
# #____________________________________________
#     results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])
#     students_number = results.count()
#     print(f"Test počítalo: {students_number} studnetů")
#
#     for i in range(students_number):
#         result = results.get_by_index(i)
#         znamka = results.get_grade(i)
#         print()
#     results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])
#     results.main()

    random_results = StudentsGrades(random_numbers(30, 0, 100))
    print(random_results.count())
    print(random_results.get_sorted())
    random_results.main()



