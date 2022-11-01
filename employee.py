import mysql.connector

mydb=mysql.connector.connect(host='localhost',user='root',password='',database='employeedb')

mycursor=mydb.cursor()

while True:
    print("\nSelect an option")
    print("1 add an employee")
    print("2 view all employee")
    print("3 search an employee")
    print("4 update the employee")
    print("5 delete an employee")
    print("6 exit")
    
    ch=int(input("select an option  : \n"))
    if (ch==1):
        emcode=input("Enter the employee code")
        name=input("Enter the name")
        des=input("Enter designation")
        salary=input("Enter the salary")
        cname=input("Enter the company")
        mob=input("Enter the phone number")
        email=input("Enter the email id")
        password=input("Enter the password")
        sql='INSERT INTO `employees`(`EmpCode`, `Name`, `Designation`, `Salary`, `CName`, `PhNo`, `Email`, `Password`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'
        data=(emcode,name,des,salary,cname,mob,email,password)
        mycursor.execute(sql,data)
        mydb.commit()        
        print("inserted success")
    elif(ch==2):
         print("selected view all employee")
    elif(ch==3):
        print("selected search employee")
    elif(ch==4):
        print("selected update the employee")
    elif(ch==5):
        print("selected delete employee")
    elif(ch==6):
        break
        
        
        
        
    
    
   