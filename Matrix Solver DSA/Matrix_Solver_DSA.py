import numpy as np
import Addition_Matrix as am
import Subtraction_Matrix as sm
import Multiplication_Matrix as mm
import Inverse_Matrix as im
import Determinanat_Matrix as dm
import Transpose_Matrix as tm
import Division_Matrix as div
import sys


#making the decorative title of our console app
for i in range(80):
    print("-", end="")
print()
print("\t\tWELCOME TO MATRIX SOLVER APP")
for i in range(80):
    print("-", end="")
print()

def myOpt():
    #giving options to the user
    print("choose either of the following for matrix operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Inverse")
    print("5. Determinant")
    print("6. Transpose Matrix")
    print("7. Divide Matrix")
    print("8. Exit")

    #user input choice
    choice=int(input("Enter choice here: "))
    return choice

#checking if the user option matches with the option list
def opening_Options(choice, opt_Arr):

        if choice>8:
            print("Please input valid number!!")

            #Recursion
            myCh=int(input("Enter choice here: "))
            opening_Options(myCh, opt_Arr)

        if opt_Arr[0]==choice:
            #open addition option
            am.Addition_Matrix().Ask_User()
            myOpt()
        elif opt_Arr[1]==choice:
            #open subtraction option
            sm.Subtraction_Matrix().Ask_User()
            myOpt()
        elif opt_Arr[2]==choice:
            #open multiplication option
            mm.Multiplication_Matrix().Ask_User()
            myOpt()
        elif opt_Arr[3]==choice:
            #open inverse option
            im.Inverse_Matrix().define_matrix()

        elif opt_Arr[4]==choice:
            #open determinant option
            dm.Determinanat_Matrix().define_matrix()
            myOpt()
        elif opt_Arr[5]==choice:
            #open transpose option
            tm.Transpose_Matrix()
            myOpt()
        elif opt_Arr[6]==choice:
            div.Division_Matrix().create_Matrix()
            myOpt()
        else:
            sys.exit(0)
choice= myOpt()
options= np.array([1,2,3,4,5,6,7,8])
opening_Options(choice, options)


