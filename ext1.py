import mysql.connector

try:
    db = mysql.connector.connect(host="localhost",
      user="root",
      password="admin", database="bank")
    handler = db.cursor()
except mysql.connector.Error as e:
    print(f"Error connecting to MySQL Database: {e}")
    exit(1)

enp = int(input('''
  𝗔𝗠𝗘𝗥𝗜𝗖𝗔𝗡 𝗘𝗫𝗣𝗥𝗘𝗦𝗦 𝗖𝗨𝗦𝗧𝗢𝗠𝗘𝗥 𝗠𝗔𝗡𝗔𝗚𝗘𝗠𝗘𝗡𝗧 𝗣𝗢𝗥𝗧𝗔𝗟
  -> To Open A New Account Press: 1
  -> To Update A Account Press: 2
  -> To Check Balance Of A Account Press: 3
  -> To Deposit Into A Account: 4
  -> To Withdraw From A Account: 5
  -> To Close A Account Press: 6
  -> To View All Accounts Press: 7
  -> Exit: 0
''')) 


def close():
    print()
    return

def open_account():
        name = input("Enter Account Holder Name: ")
        typeacc = input("Enter Type Of Account [C/S]: ")
        balance = float(input("Enter Deposit Amount: $"))
        ph = input("Enter Account Holder Phone Number: ")
        address = input("Enter Account Holder Address: ")
        age = int(input("Enter Account Holder Age: "))
        pan = input("Enter Account Holder PAN: ")
        nominee = input("Enter Nominee Name: ")
        accountno = "AMX" + ph[6:10]
        handler.execute("INSERT INTO accounts (account, name, account_type, balance, phonenumber, address, age, pan, nominee) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);", (accountno, name, typeacc, balance, ph, address, age, pan, nominee))
        db.commit()
        print("Account is successfully created, ACCOUNT NO:", accountno, " happy banking :)")
        return

def update_account():
      acc = input("Enter Account Number: ")
      opt = int(input('''
      -> To Update Account Holder Age Press: 1
      -> To Update Account Holder PhoneNumber Press: 2
      -> To Update Account Holder Address Press: 3
      -> To Change Nominee Name Press: 4
      '''))
      if(opt == 1):
            upage = int(input("Enter New Age: "))
            handler.execute("UPDATE accounts SET age = %s WHERE account = %s;", (upage, acc))
            db.commit()
      elif(opt == 2):
            upph = input("Enter New PhoneNumber: ")
            handler.execute("UPDATE accounts SET phonenumber = %s WHERE account = %s;", (upph, acc))
            db.commit()
      elif(opt == 3):
            upadd = input("Enter New Address: ")
            handler.execute("UPDATE accounts SET address = %s WHERE account = %s;", (upadd, acc))
            db.commit()
      elif(opt == 4):
            upnom = input("Enter New Nominee Name: ")
            handler.execute("UPDATE accounts SET nominee = %s WHERE account = %s;", (upnom, acc))
            db.commit()
      print("Updated Successfully")
      return

def check_balance():
    acc = input("Enter Account Number: ")
    handler.execute("SELECT balance FROM accounts WHERE account = %s;", (acc,))
    result = handler.fetchone()
    if result:
        print("Your Account Balance is: $", result[0])
    else:
        print("Account not found.")

def deposit_amt():
    acc = input("Enter Account Number: ")
    amt = float(input("Enter Amount To Deposit: $"))
    handler.execute("UPDATE accounts SET balance = balance + %s WHERE account = %s;", (amt, acc,))
    db.commit()
    handler.execute("SELECT balance FROM accounts WHERE account = %s;", (acc,))
    result = handler.fetchone()
    print("Amount of $", result[0], " Is Successfully Credited In ACOUNT NO:", acc)

def withdraw_amt():
    acc = input("Enter Account Number: ")
    amt = float(input("Enter Amount To Withdraw: $"))
    handler.execute("SELECT balance FROM accounts WHERE account = %s;", (acc,))
    result = handler.fetchone()
    if result and result[0] >= amt:
        handler.execute("UPDATE accounts SET balance = balance - %s WHERE account = %s;", (amt, acc,))
        db.commit()
        print("Amount of $", result[0], " Is Successfully Debited From ACOUNT NO:", acc)
    else:
        print("Insufficient Balance or Account not found.")

def close_acc():
    acc = input("Enter Account Number: ")
    handler.execute("DELETE FROM accounts WHERE account = %s;", (acc,))
    db.commit()
    print("Account Closed Successfully.")

def view_acc():
    handler.execute("SELECT * FROM accounts;")
    results = handler.fetchall()
    if results:
        print(f"{'ID':<5}{'Account No':<20}{'Name':<30}{'Account Type':<20}{'Balance':<20}{'Phone Number':<20}{'Address':<50}{'Age':<30}{'Nominee':<30}")
        for row in results:
            print(f"{row[0]:<5}{row[1]:<20}{row[2]:<30}{row[3]:<20}{row[4]:<20}{row[5]:<20}{row[6]:<50}{row[7]:<30}{row[9]:<30}")
    else:
        print("No Accounts found.")
     

      
if(enp == 0):
      close()
elif(enp == 1):
      open_account()
elif(enp == 2):
      update_account()
elif(enp == 3):
      check_balance()
elif(enp == 4):
      deposit_amt()
elif(enp == 5):
      withdraw_amt()
elif(enp == 6):
      close_acc()
elif(enp ==7):
     view_acc()
