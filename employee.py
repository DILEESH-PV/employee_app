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
        empcode=input("Enter the employee code")
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
        sql='SELECT * FROM `employees`'
        mycursor.execute(sql)
        result=mycursor.fetchall()
        for i in result:
            print(i)
        print("selected view all employee")
    elif(ch==3):
        print("selected search employee")
        empcode=input("Enter the employee code for searching the employee")
        sql='SELECT * FROM `employees` WHERE `EmpCode`='+empcode
        mycursor.execute(sql)
        result=mycursor.fetchall()
        print(result)
    elif(ch==4):
        empcode=input("Enter the employee code")
        
        name=input("Enter the name to be updated")
        des=input("Enter designation to be updated")
        salary=input("Enter the salary to be updated")
        cname=input("Enter the company to be updated")
        mob=input("Enter the phone number to be updated")
        email=input("Enter the email id to be updated")
        password=input("Enter the password to be updated")
        sql="UPDATE `employees` SET `Name`='"+name+"',`Designation`='"+des+"',`Salary`='"+salary+"',`CName`='"+cname+"',`PhNo`='"+mob+"',`Email`='"+email+"',`Password`='"+password+"' WHERE `EmpCode`="+empcode
        mycursor.execute(sql)
        mydb.commit()
        print("updated successfully")
    elif(ch==5):
        empcode=input("Enter the empcode for delete an employee")
        sql='DELETE FROM `employees` WHERE `EmpCode`='+empcode
        mycursor.execute(sql)
        mydb.commit()
        print("deleted successfully")   
    elif(ch==6):
        break
        
        
        
        
    
    
   