
print("Please put your card into the ATM")

entries = 0 #variable for while loop
correctpin = 1234 #set pin for code 


while entries != 3: #asking to input their pin, if false 3 times code ends
  pin = int(input("enter your pin "))  

  if pin != correctpin:
    print("Incorrect pin please try again")
  else:
    break #breaks the while loop
  entries += 1 #ends the while loop


if pin == correctpin: #if pin is correct it will display ATM menu
  print("\t |----------------------|")
  print("\t |\t LCCS BANK LIMITED\t|")
  print("\t |\t ATM MAIN MENU\t\t|")
  print("\t |\t\t\t\t\t\t|")
  print("\t |\t1. Balance Enquiry\t|")
  print("\t |\t2. Cash Lodgement\t|")
  print("\t |\t3. Cash Withdrawal\t|")
  print("\t |\t4. Cash Transfer\t|")
  print("\t |\t5. Change PIN\t\t|")
  print("\t |\t6. Other Services\t|")
  print("\t |\t\t\t\t\t\t|")
  print("\t |\t7. Exit\t\t\t\t|")
  print("\t |----------------------|")
  print("\t |\t\t\t\t\t\t|")
  print("\t | CHOOSE AN OPTION >>\t|")
  print("\t |\t\t\t\t\t\t|")
  print("\t |----------------------|")
  menuexit = 0 #variable for loop
  balance = 100 #current balance of the account
  while menuexit != 1: #while loop will keep going until menuexit is equal to 1
    option2 = int(input("Please input your option: "))

    if option2 == 1:
      print("your balance is", balance)
    elif option2 == 2:
      cashLodge = int(input("How much would you like to lodge? "))
      balance = balance + cashLodge
      print("your balance is", balance)
    elif option2 == 3: 
      cashWith = int(input("How much would you like to withdraw? "))
      balance = balance - cashWith
      print("your balance is", balance)
    elif option2 == 4:
      cashTrans = int(input("How much would you like to transfer "))
      balance = balance - cashTrans
      print("Your money has been sent, your balance is", balance)
    elif option2 == 5:
      newPin = int(input("input your new pin: "))
      correctpin = newPin
      print("your new pin has been changed")
    elif option2 == 6:
      print("Currently there are no other services")
    elif option2 == 7:
      print(" you have exited the ATM please remove your card.")
      menuexit = 1 #ends the loop cause menuexit is now 1
    else:
      print("invalid entry")
else:
  print("invalid pin")


