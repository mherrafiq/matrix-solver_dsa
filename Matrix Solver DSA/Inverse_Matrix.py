from numpy import array

class Inverse_Matrix(object):
    """description of class"""

    def __init__(self, *args):
        self.matrix= None
        self.rows= None
        self.cols= None

    def define_matrix(self):
        #ask user rows and columns
        row= int(input("Enter rows: "))
        cols= int(input("Enter columns: "))

        self.matrix= [[0 for i in range(cols)]for j in range(row)]

        if row!=cols:
            print("Inverse can only be applied for square matrix!!")
        else:
            for i in range(row):
              for j in range(cols):
                 k=i+1
                 l=j+1
                 self.matrix[i][j]=int(input("Enter row "+str(k)+" and column "+str(l)+": "))

            print("Inverse of matrix: ")
            print(str(self.getMatrixInverse(self.matrix)))

    def transposeMatrix(self, m):

       res= [[0 for i in range(len(m))] for j in range(len(m[0]))]
       for r in range(len(m)):
   
            for c in range(len(m[0])):
     
                res[c][r] = m[r][c]

       return res

    def getMatrixMinor(self, m,i,j):
        return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

    def getMatrixDeternminant(self, m):
      #base case for 2x2 matrix
      if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

      determinant = 0
      for c in range(len(m)):
                                               #Recursion
        determinant += ((-1)**c)*m[0][c]*self.getMatrixDeternminant(self.getMatrixMinor(m,0,c))
      return determinant

    def getMatrixInverse(self, m):
       
           determinant = self.getMatrixDeternminant(m)
           #special case for 2x2 matrix:
           if len(m) == 2 and determinant!=0:
               return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                [-1*m[1][0]/determinant, m[0][0]/determinant]]
           elif len(m)>2 and determinant!=0:

              #find matrix of cofactors
              cofactors = [0 for i in range(len(m))]
              for r in range(len(m)):
                 cofactorRow = [0 for i in range(len(m))]
                 for c in range(len(m)):
                    minor = self.getMatrixMinor(m,r,c)
                    cofactorRow[c]=(((-1)**(r+c)) * self.getMatrixDeternminant(minor))
                 cofactors[r]=(cofactorRow)
              cofactors = self.transposeMatrix(cofactors)
              for r in range(len(cofactors)):
                 for c in range(len(cofactors)):
                   cofactors[r][c] = cofactors[r][c]/determinant
                   arr= array(cofactors)
              return arr
           else:
              return "Determinant is 0, Inverse can not be calculated!"
      