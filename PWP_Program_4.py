#USER INPUT BASED PROGRAM TO CHECK THE DATATYPES OF VARIABLE

choice='y'

while True:
    user_in=eval(input("Enter a value"))
    data=type(user_in)
    print("The data type of input is:",data)
    choice=input("Do you wish to continue (y/n)?")
