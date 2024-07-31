from numpy import array

class Matrix_Node:

    def __init__(self, mat):
        self.next=None
        self.matrix= mat


class Subtraction_Matrix(object):
    """description of class"""

    #Aim: to implement matrix using linked list
    #this will help us to make matrices according to user input

    def __init__(self):
        self.head= None
        self.temp= None

    def Ask_User(self):
        usr=int(input("How many matrices you want: "))
        self.Create_Matrix(usr, 0)

    def Create_Matrix(self, usr, i):

        if i<usr:

            #ask user rows and columns
            row= int(input("Enter rows: "))
            cols= int(input("Enter columns: "))

            #create matrix
            self.mat= array([[0 for i in range(cols)] for j in range(row)])
            self.res= array([[0 for i in range(cols)] for j in range(row)])

            for a in range(row):
                for j in range(cols):

                    k=a+1
                    l=j+1
                    self.mat[a][j]= int(input("Enter row "+str(k)+" and column "+str(l)+" of MATRIX "+str(i)+": "))

            #linked list creation
            mymat= Matrix_Node(self.mat)
            if self.head== None:
                self.head= mymat
                self.temp= self.head
            else:
                self.temp.next=mymat
                self.temp=self.temp.next

            #Recursion
            self.Create_Matrix(usr, i+1)
        else:
            print(self.Matr_Sub(self.head, usr, None))

    def Matr_Sub(self, head, usr, temp):
        
        if temp == None:
            temp=head
            self.res= temp.matrix

            
        try:
        
          while temp.next!=None:
            if len(temp.matrix)!=len(self.res) and len(temp.matrix[0])!= len(self.res[0]):
                print("Can not be solved!!")
                break
            else:
                for i in range(len(temp.matrix)):
                    for j in range(len(temp.matrix[0])):
                        self.res[i][j] -= (temp.next.matrix[i][j])

            temp=temp.next

          return self.res
        except:
            return "Can not be subtracted"

       
