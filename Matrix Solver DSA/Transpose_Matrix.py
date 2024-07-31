from numpy import array
class Transpose_Matrix(object):
    """description of class"""


    def __init__(self):
        rows = int(input("Enter the Number of rows : " ))
        column = int(input("Enter the Number of Columns: "))

        print("Enter the elements of Matrix:")
        matrix= array([[int(input()) for i in range(column)] for i in range(rows)])

        result =array([[0 for i in range(rows)] for j in range(column)])

        print("Transpose matrix is: ")
        print(array(self.transposeMatrix(matrix, result)))

    def transposeMatrix(self, m, res):

       for r in range(len(m)):
   
            for c in range(len(m[0])):
     
                res[c][r] = m[r][c]
       return res