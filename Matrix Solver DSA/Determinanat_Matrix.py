
class Determinanat_Matrix(object):
    """description of class"""

    def __init__(self):
        self.matrix= None
        self.diag1= 0
        self.diag2= 0

    def getMinor(self, m, i, j):
        return [row[: j] + row[j+1:] for row in (m[: i] + m[i+1:])]

    def determinantOfMatrix(self, mat):
 
        # if given matrix is of order
        # 2*2 then simply return det
        # value by cross multiplying
        # elements of matrix.
        if(len(mat) == 2):
           value = mat[0][0] * mat[1][1] - mat[1][0] * mat[0][1]
           return value
 
        # initialize Sum to zero
        Sum = 0
 
        # loop to traverse each column
        # of matrix a.
        for current_column in range(len(mat)):
 
           # calculating the sign corresponding
           # to co-factor of that sub matrix.
           sign = (-1) ** (current_column)
 
           # calling the function recursily to
           # get determinant value of
           # sub matrix obtained.
                              #Recursion
           sub_det = self.determinantOfMatrix(self.getMinor(mat, 0, current_column))
 
           # adding the calculated determinant
           # value of particular column
           # matrix to total Sum.
           Sum += (sign * mat[0][current_column] * sub_det)
 
        # returning the final Sum
        return Sum


    def define_matrix(self):
        #ask user rows and columns
        row= int(input("Enter rows: "))
        cols= int(input("Enter columns: "))

        self.matrix= [[0 for i in range(cols)]for j in range(row)]

        if row!=cols:
            print("Determinant can only be applied for square matrix!!")
        else:
            for i in range(row):
              for j in range(cols):
                 k=i+1
                 l=j+1
                 self.matrix[i][j]=int(input("Enter row "+str(k)+" and column "+str(l)+": "))

            print("Determinant of matrix: "+str(self.determinantOfMatrix(self.matrix)))