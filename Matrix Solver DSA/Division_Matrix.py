from numpy import array

class Division_Matrix(object):
    """description of class"""

    def  __init__(self):
        self.row= None
        self.cols= None
        self.matrix= None
        self.divisor= None

    def create_Matrix(self):

        self.row=int(input("Enter rows: "))
        self.cols=int(input("Enter columns: "))

        self.matrix= array([[0 for i in range(self.cols)]for j in range(self.row)])

        self.divisor= int(input("Enter the number to be divided: "))

        print("Enter the elements of Matrix:")
        self.matrix= [[int(input()) for i in range(self.cols)] for i in range(self.row)]

        print(self.divide(self.matrix, self.divisor))

    def divide(self, mat, div):

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                mat[i][j]/= div

        return array(self.matrix)
