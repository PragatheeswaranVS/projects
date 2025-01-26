import mysql.connector
from tabulate import tabulate
connect = mysql.connector.connect(user = "root",password = "Pragathees@2004",host = "localhost",database = "projects")
cursor =connect.cursor()
def sql(name,register_no,dob,tamil_mark,english_mark,maths_mark,science_mark,social_mark):
    query = f"insert into student_mark (name,register_no,dob,tamil_mark,english_mark,maths_mark,science_mark,social_mark) values ('{name}',{register_no},'{dob}',{tamil_mark},{english_mark},{maths_mark},{science_mark},{social_mark})"
    cursor.execute(query)
    connect.commit()
    print("success")
def view(register_no,dob):
    query = f"select * from student_mark where register_no = {register_no} and dob = '{dob}'"
    cursor.execute(query)
    show = cursor.fetchall()
    for data in show:
        si = data[0]
        name = data[1]
        register_no = data[2]
        dob = data[3]   
        tamil_mark = data[4]
        english_mark = data[5]  
        maths_mark = data[6]
        science_mark = data[7]
        social_mark = data[8]
        total_mark = tamil_mark + english_mark + maths_mark + science_mark + social_mark
        print("____________________________________________________________")
        print(f"NAME : {name}\nREGISTER NO : {register_no}\nDOB : {dob}")
        print("____________________________________________________________")
        print("SUBJECTS \t\t\tMARKS")
        print("____________________________________________________________")
        print(f"TAMIL\t\t- \t\t{tamil_mark}\nENGLISH\t\t- \t\t{english_mark}\nMATHS\t\t- \t\t{maths_mark}\nSCIENCE\t\t- \t\t{science_mark}\nSOCIAL SCIENCE\t- \t\t{social_mark}")
        print("__________________________________________________________")
        print(f"\tTOTAL\t- \t\t{total_mark}")
        print("__________________________________________________________")
def update(regno,mark):
    query = f"update student_mark set science_mark ={mark} where register_no = '{regno}'"
    cursor.execute(query)
    connect.commit()
    print("update success")
    
while(True): 
    print()
    print("\n1.FOR INSERT THE DATA \n2.FOR GET RESULT \n3.update data \n4.EXIT")
    print()
    ch =int(input("enter choice: "))
    if ch == 1: 
       name = input("enter name : ")  
       register_no = int(input("enter register no : "))
       dob = input("enter dob (for example:(yyyy-mm-dd)) : ")
       tamil_mark = int(input("enter tamil mark : "))
       english_mark = int(input("enter english mark : "))
       maths_mark = int(input("enter maths mark : "))
       science_mark = int(input("enter science mark : "))
       social_mark = int(input("enter soccial mark : "))
       sql(name,register_no,dob,tamil_mark,english_mark,maths_mark,science_mark,social_mark)
    elif ch == 2:
        # name = input("enter name : ") 
        register_no = int(input("enter register no : "))
        dob = input("enter dob (for example:(yyyy-mm-dd)) : ")
        view(register_no,dob)
    elif ch == 3:
        regno = input("enter regno : ") 
        mark = int(input("enter the mark : "))
        update(regno,mark)
    elif ch == 4:
        break
    else:
        print("INVALID VALID")
    