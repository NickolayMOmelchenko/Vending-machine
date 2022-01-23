'''
Program: VENDING MACHINE PROGRAM
Date: 11/1/2021
Name: Mykola (Nick) Omelchenko
Purpose: wending machine that asks the user what snacks the user want. Then it prompts the amount of money that must be paid. If the user pays for the snacks, the program will output the amount of change. It will also, print out what kind of change it is. ex: Quarters 0, dimes 1, pennies 3.
''' 
#function prints out the menu
def menu():
  print ("Welcome to My Vending Machine")
  print ("1. Dr. Pepper - 1.75")
  print ("2. Doritios - 2.00")
  print ("3. Kitkat Bar - .50")
  print ("4. Pop-tarts - 1.00")
  print ("5. Gum - .25")
#function calculates the change
def changecalc(total):
  print ("Your change is:")
  total = abs(total)
  total = float(total)
  dollars = total / 1
  total = total % 1
  quarters = total / .25
  total = total % .25
  dimes = (total) / .10
  total = total % .10
  total = round(total, 2)
  nickels = (total % .25 % .10) / .05
  total = total % .05
  total = round(total, 2)
  pennies = (total % .35 % .10 % .05) / .01
  total = total % .01
  total = round(total, 2)

  print('Dollars:\t' + str(int(dollars)))
  print('Quarters:\t' + str(int(quarters)))
  print('Dimes:\t\t' + str(int(dimes)))
  print('Nickels:\t' + str(int(nickels)))
  print('Pennies:\t' + str(int(pennies)))

  

total = 0  
n = 1
while(n != 0):
  menu()
  #assigning the price of the items. 
  drPepper = 1.75
  doritios = 2.00
  kitkatBar = 0.50
  poptarts = 1.00
  Gum = 0.25
  #Shows what the user bought and adds it to the total
  n = float(input("Please enter the number of your item or 0 to quit: "))
  if n <= 5 and n > 0:
    if n == 1:
      print ("You bought one can of Dr. Pepper for $1.75")
      total += drPepper
    if n == 2:
      print ("You bought one bag of Doritios for $2.00")
      total += doritios
    if n == 3:
      print ("You bought one Kitkat Bar for $0.50")
      total += kitkatBar
    if n == 4:
      print ("You bought one Pop-tart for $1.00")
      total += poptarts
    if n == 5:
      print ("You bought one pack of Gum for $0.25")
      total += Gum
  #ensures the user entered the correct menu item
  elif n > 5 or n < 0 or n != 0:
    print("Invalid entery!")
  #ensures the user doesn't have change
  elif n == 0:
    print ("Thank you! Standby for your total.")
    if total == 0:
      print("You didn't order anything!")
      exit(0)
    if total != 0: 
      print ("Your total is $" + str(total) + "!")
    #Change calculator
    paymentAmount = float(input("Enter your payment: "))
    total -= paymentAmount
    while (total >= 0):
      paymentAmount = float(input("Not Enough! Enter more money: "))
      total -= paymentAmount
    if (total == 0):
      print ("Thank you for your purchase. You don't have any chnage left.")
    else:
      changecalc(total)
      



      
