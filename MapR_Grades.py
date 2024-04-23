from mrjob.job import MRJob
from mrjob.step import MRStep

class CalculateGrades(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                   reducer=self.reducer)
        ]

    def mapper(self, _, line):
        if line.startswith('id'):
            return
        _, name, math, english = line.split(',')
        total_marks = int(math) + int(english)
        percentage = (total_marks / 200) * 100
        yield None, {'name': name, 'percentage': percentage}

    def reducer(self, _, values):
        for student_info in values:
            percentage = student_info['percentage']
            grade = self.assign_grade(percentage)
            yield student_info['name'], grade

    def assign_grade(self, percentage):
        if percentage < 40:
            return 'Fail'
        return 'A+' if percentage >= 90 else 'A' if percentage >= 80 else 'B' if percentage >= 70 else 'C' if percentage >= 60 else 'D'

if __name__ == "__main__":
    CalculateGrades.run()
