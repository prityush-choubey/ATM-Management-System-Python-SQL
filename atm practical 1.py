import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="2001",
  database="bank"
)
mycursor = mydb.cursor()
admin_password="admin123"
    
            
def insert():
  account_no=input("enter account no")
  name=input("enter name")
  branch_name=input("enter branch name")
  opening_balance=input("enter opening balance")
  date=input("enter date (dd-mm-yyyy):")
  status=input("enter status")
  sql="insert into account_detail values('"+account_no+"','"+name+"','"+branch_name+"','"+opening_balance+"','"+date+"','"+status+"')"
  mycursor.execute(sql)
  mydb.commit()
  print(" new record inserted")


def delete():
    account_no=input ("enter id")
    sql="delete from account_detail where account_no='"+account_no+"'"
    mycursor.execute(sql)
    mydb .commit()



def admin_menu():
  print("insert 1 to insert")
  print("insert 6 to delete")  
  choice=input("enter choice")
  if choice=="1":
    insert()
  elif choice=="2":
    delete()
  else:
    print("wrong value")



 

def display_account():
    account_no=input("Enter id")
    sql="select * from account_detail where account_no='"+account_no+"'"
    mycursor.execute(sql)
    r=mycursor.fetchall()
    if r!=[]:
        for i in r:
            print(i[0],i[1],i[2],i[3],i[4])
    else:
        print("wrong id")

def deposit():
  account_no=input("enter account no")
  deposit_amt=input("enter value to deposit")
  t_type=input("enter deposit")
  date=input("enter date")
  sql="select * from account_detail where account_no='"+account_no+"'"
  mycursor.execute(sql)
  row=mycursor.fetchone()
  if row:
    current_balance = row[3]
    new_amount = int(current_balance) + int(deposit_amt)
    update_query= "UPDATE account_detail SET opening_balance = '"+ str(new_amount)+"' WHERE account_no ='"+account_no+"'"
    mycursor.execute(update_query)
    data="insert into transaction_detail values('"+account_no+"','"+deposit_amt+"','"+t_type+"','"+date+"')"
    mycursor.execute(data)
    mydb.commit()

    print(" Deposit Successful")
    print("Updated Balance:", new_amount)
  else:
    print("Account not found. Deposit not allowed.")


def withdraw():
  account_no=input("enter account no")
  withdraw_amt= input("enter withdraw amount")
  t_type=input("enter withdraw")
  date=input("enter date")
  sql="select * from account_detail where account_no='"+account_no+"'"
  mycursor.execute(sql)
  row=mycursor.fetchone()
  if row:
     current_balance = row[3]
     if int(withdraw_amt)<=int(current_balance):
        new_amount = int(current_balance) - int(withdraw_amt)
        update_query= "UPDATE account_detail SET opening_balance = '"+ str(new_amount)+"' WHERE account_no ='"+account_no+"'"
        mycursor.execute(update_query)
        data="insert into transaction_detail values('"+account_no+"','"+withdraw_amt+"','"+t_type+"','"+date+"')"
        mycursor.execute(data)
        mydb.commit()
    
  
def display_transaction():
    account_no=input("Enter id")
    sql="select * from transaction_detail where account_no='"+account_no+"'"
    mycursor.execute(sql)
    r=mycursor.fetchall()
    if r!=[]:
        for i in r:
            print(i[0],i[1],i[2],i[3])
    else:
        print("wrong id")


def user(): 

  print("insert 2 to display account")
  print("insert 3 to deposit amount")
  print("insert 4 to withdraw amount")
  print("insert 5 to display transaction")
  choice=input("enter choice")
  if choice=="2":
    display_account()
  elif choice=="3":
    deposit()
  elif choice=="4":
    withdraw()
  elif choice=="5":
    display_transaction()
  else:
    print("wrong value")

while True:
  print("insert 1 for admin")
  print("insert 2 for user")
  
  choice=input("enter choice")
  if choice=="1":
    pasword=input("enter admin pasword")
    
    if pasword==admin_password:
      admin_menu()
  #else:
    #print("wrongpassword")
  elif choice=="2":
    account_no=input("enter account no")
    sql="select * from account_detail where account_no='"+account_no+"'"
    mycursor.execute(sql)
    r= mycursor.fetchall()
    if r!=[]:
      user()
    else:
      print("wrongid")
  
  






  
  
    














