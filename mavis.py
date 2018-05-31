'''
Created on 13 Jun 2017

@author: airbook
'''

from register import for_user
#from curses.ascii import isalpha


print("Welcome Friend To Mavis Restaurant")
print("========================================================================================================")

for_user()

#===============================================Lists, Variables and Calculations====================================
menu_list1 = ["Burger: 50USD", "Pizza: 55USD", "Shawama: 45USD", "Chicken: 70USD"]
menu_list = ["burger", "pizza", "shawama", "chicken"]
price_list = [50, 55, 45, 70]

tax = 0.1
tip = 5
total = tax + tip

price_burger = price_list[0] + total
price_chicken = price_list[1] + total
price_pizza = price_list[2] + total
price_shawama = price_list[3] + total

wtip_burger = price_list[0] + tax
wtip_chicken = price_list[1] + tax
wtip_pizza = price_list[2] + tax
wtip_shawama = price_list[3] + tax

#========================================sorting and printing out the menu list alphebetically=============================
print ("Here are what we have on our menu for today: ")
menu_list1.sort()
for meal in menu_list1:
    print (meal)
print ("========================================================================================================")

#=========================================Meal Request Function======================================================================
def meal_request():
    
    user_input = input("What will you like to have today %s? ").lower()
    if user_input == menu_list[0] and user_input.isalpha():
        print ("Your %s is coming right up! " %(menu_list[0]))
        print ("========================================================================================================")
    elif user_input == menu_list[1] and user_input.isalpha():
        print ("Your %s is coming right up! " %(menu_list[1]))
        print ("========================================================================================================")
    elif user_input == menu_list[2] and user_input.isalpha():
        print ("Your %s is coming right up!" %(menu_list[2]))
        print ("========================================================================================================")
    elif user_input == menu_list[3] and user_input.isalpha():
        print ("Your %s is coming right up! " %(menu_list[3]))
        print ("========================================================================================================")
    else:
        print("Invalid Request")
        print("Input a meal on the menu list")
        print ("========================================================================================================")
        meal_request()
   
#==============================================Bill For Meal Function============================================================
def bill_meal():
    bill_request = input("Will you like your Bill now, type 'yes' or 'no'? ").lower()
    if bill_request == 'yes' or bill_request == 'y':
        print ('Alright your bill is coming right up')
        print ("========================================================================================================")
        
    elif bill_request == 'no' or bill_request == 'n':
        print ('Alright when you are ready for your bill call on me.')
        print ("========================================================================================================")
        bill_meal()
    
    else:
        print ('Invalid input.')
        print("Type in 'Yes' or 'No'.")
        
        print ("========================================================================================================")
        bill_meal()
    
    
#======================================Meal Order Function=========================================================

def meal_order():

    meal_requested = input('What meal did you order for? ')
    tip_request = input("Will you like to give a tip of 5USD for our outstanding sevrices? ")
    if tip_request == "no":
        print ("Your bill without tip is coming right up. :( ")
        print ("========================================================================================================")
        
        if meal_requested == menu_list[0] and meal_requested.isalpha():
            print ('%sUSD is your bill for your %s without tip inclusive' %(wtip_burger, menu_list[0]))
        elif meal_requested == menu_list[1] and meal_requested.isalpha():
            print ('%sUSD is your bill for your %s without tip inclusive') %(wtip_chicken, menu_list[1])
        elif meal_requested == menu_list[2]and meal_requested.isalpha():
            print ('%sUSD is your bill for your %s without tip inclusive') %(wtip_pizza, menu_list[2])
        elif meal_requested == menu_list[3] and meal_requested.isalpha():
            print ('%sUSD is your bill for your %s without tip inclusive') %(wtip_shawama, menu_list[3])    
        else:
            print ("Hold on for your Bill.")
               
            print ("========================================================================================================")
            meal_order()
        
    elif tip_request == "yes":
        print ("Your bill with tip inclusive is coming right up. :) ")
        print ("========================================================================================================")
        if meal_requested == menu_list[0]:
            print ('%sUSD is your bill for your %s with tax and tip inclusive') %(price_burger, menu_list[0])
        elif meal_requested == menu_list[1]:
            print ('%sUSD is your bill for your %s with tax and tip inclusive') %(price_chicken, menu_list[1])
        elif meal_requested == menu_list[2]:
            print ('%sUSD is your bill for your %s with tax and tip inclusive') %(price_pizza, menu_list[2])
        elif meal_requested == menu_list[3]:
            print ('%sUSD is your bill for your %s with tax and tip inclusive') %(price_shawama, menu_list[3])    
        else:
            print ("Hold on for your Bill.")
            meal_order()
           
        
    else:
        print ("Invalid Request")
        print("==============================================================================================================")
        user_equiry()

#======================================User Enquiry Function=========================================================

def user_equiry():
    
    usage_question = input("Type 'quit' to exist the app or type 'continue' to go ahead: ")
    if usage_question == "quit":
        print ("You have successfully exist from the app. ")
        print ("Thanks for using Mavis Restaurant App" )
        
        
    elif usage_question == "continue":
        print ("Alright let\'s continue...")
        print ("========================================================================================================")
        meal_request()
        bill_meal()
        meal_order()
        user_equiry()
    else:
        print ("Invalid Request...")
        print ("Please type in a valid meal on the menu list. ")
        print ("========================================================================================================") 
        user_equiry()   
              

meal_request()
bill_meal()
meal_order()
user_equiry()