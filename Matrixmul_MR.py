from mrjob.job import MRJob
from mrjob.step import MRStep

class MatrixMultiplicationJob(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                   reducer=self.reducer)
        ]

    def mapper(self, _, line):
        matrix1, matrix2 = [list(eval(matrix_str)) for matrix_str in line.split()]
        yield f'Product of {matrix1} and {matrix2}: ', (matrix1, matrix2)

    def reducer(self, key, values):
        matrix1, matrix2 = next(values)
        result_matrix = [[sum(matrix1[i][k] * matrix2[k][j] for k in range(len(matrix2)))
                          for j in range(len(matrix2[0]))] for i in range(len(matrix1))]
        yield key, result_matrix

if __name__ == '__main__':
    MatrixMultiplicationJob.run()