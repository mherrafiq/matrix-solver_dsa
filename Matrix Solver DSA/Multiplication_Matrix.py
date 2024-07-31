from numpy import array

class Matrix_Node:

    def __init__(self, mat):
        self.matrix= mat
        self.next= None


class Multiplication_Matrix(object):
    """description of class"""


    #Aim: to implement matrix using linked list
    #this will help us to make matrices according to user input

    def __init__(self):
        self.head= None
        self.temp= None
        self.actual_result= None
        self.temp_res= None


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
                self.temp.next= mymat
                self.temp=self.temp.next

            #Recursion
            self.Create_Matrix(usr, i+1)
        else:
            print(self.Matr_Mul(self.head, usr, None))

    def Matr_Mul(self, head, usr, temp):
        
        if temp== None:
            temp= head

        while temp.next!=None:

            if len(temp.matrix)!= len(temp.next.matrix[0]) and len(temp.next.matrix)!= len(temp.matrix[0]):
                return("Can not be multiplied")

            #first check which order is equal
                  #1st mat row              2nd mat col            1st mat col         !=         2nd mat row
            if (len(temp.matrix) == len(temp.next.matrix[0])) and (len(temp.matrix[0]) != len(temp.next.matrix)):
                #initialize the result matrix only when the pointer is at the start node                                                              
                
                                                               #2nd mat row = col                  1st mat col =row
                self.temp_res= array([[0 for i in range(len(temp.next.matrix))] for j in range(len(temp.matrix[0]))])

                #now multiplying the matrices
                for i in range(len(temp.matrix[0])):
                   for j in range(len(temp.next.matrix)):
                       sum=0
                       for k in range(len(temp.next.matrix[0])):
                           sum+=(temp.matrix[k][i]*temp.next.matrix[j][k])
                       self.temp_res[i][j]= sum

                    #1st mat col          2nd mat row                1st mat row            2nd mat col
            if len(temp.matrix[0]) == len(temp.next.matrix) and (len(temp.matrix) != len(temp.next.matrix[0])):
                   #initialize the result matrix only when the pointer is at the start node   
                                                              #2nd mat col = col                  1st mat row =row
                self.temp_res= array([[0 for i in range(len(temp.next.matrix[0]))] for j in range(len(temp.matrix))])
                #now multiplying the matrices
                for i in range(len(temp.matrix)):
                   for j in range(len(temp.next.matrix[0])):
                       sum=0
                       for k in range(len(temp.next.matrix)):
                           sum+=(temp.matrix[i][k]*temp.next.matrix[k][j])
                       self.temp_res[i][j]= sum

            if len(temp.matrix[0]) == len(temp.next.matrix) and (len(temp.matrix) == len(temp.next.matrix[0])):
                   #initialize the result matrix only when the pointer is at the start node   
                                                              #2nd mat col = col                  1st mat row =row
                self.temp_res= array([[0 for i in range(len(temp.next.matrix[0]))] for j in range(len(temp.matrix))])
                #now multiplying the matrices
                for i in range(len(temp.matrix)):
                   for j in range(len(temp.next.matrix[0])):
                       sum=0
                       for k in range(len(temp.next.matrix)):
                           sum+=(temp.matrix[i][k]*temp.next.matrix[k][j])
                       self.temp_res[i][j]= sum

            temp.next.matrix= self.temp_res
            temp=temp.next

        return temp.matrix
