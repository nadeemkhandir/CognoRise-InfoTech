#!/usr/bin/env python
# coding: utf-8

# # CognoRise InfoTech Python Development Intership  Task No 1 (Calculator)
# 
# 

# In[1]:


# creating a funtion for addition
def addition(first_number, second_number):
   #initilizing result variable
   result = first_number + second_number
   print(f'The sum of number {first_number} + {second_number} = {result}')

   # creating a funtion for subtraction
def subtraction(first_number, second_number):
   #initilizing result variable
   result = first_number - second_number
   print(f'The subtraction of number {first_number} - {second_number} = {result}')

# creating a funtion for Multiplication
def multiplication(first_number, second_number):
   #initilizing result variable
   result = first_number * second_number
   print(f'The Multiplication of number {first_number} * {second_number} = {result}')

# creating a funtion for division
def division(first_number, second_number):
   #initilizing result variable
   try:

       result = first_number / second_number
       print(f'The division of number {first_number} / {second_number} = {result}')
   except ZeroDivisionError:
       print('ZeroDivisionError Occurred')
       print('You can not divid any number by zero')
       main()


      
def main():
   while True:
       try:

           # Taking input from User 
           first_number = int(input('Enter First Number'))
           second_number = int(input('Enter second Number'))
       except:
           print('Invalid Number')
           continue

       # Show Operation menu 
       print(f'''
             Press 1 for Addition
             Press 2 for Subtraction
             Press 3 for Multiplication
             Press 4 for Division
             Press Q for Exit

             ''')
       # Taking opertion choic from user
       operation = input('Enter Your Choice: ')

       # checking the user choice
       if operation == "1":
           # calling addtion funtion
           addition(first_number,second_number)
       elif operation == "2":
           # calling subtraction funtion
           subtraction(first_number,second_number)
       elif operation == "3":
           # calling multiplication funtion
           multiplication(first_number,second_number)
       elif operation == "4":
           # calling division funtion
           division(first_number,second_number)
       elif operation.upper().strip() == "Q":
           break
       else:
           print("Invalid Selection please selection a valid option")
           continue
   


# In[ ]:


# Calling Main funtion 

main()


# In[ ]:





# In[ ]:




