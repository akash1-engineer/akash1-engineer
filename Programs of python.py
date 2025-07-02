#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Question1   any integer is input by the user. write a program to find out whether it is an odd number or even numver
num=int(input("enter odd number: "))
ans="even number" if num%2==0 else "odd number"
print(ans)


# In[2]:


# Question2 find the absolute value of a number entered by user.
num=float(input("enter the absolute:"))
if num<0:
    absolute_num=-num
else:
    absolute_num=num
print(absolute_num)


# In[3]:


# Question3 write a program to determine whether the seller had made profit or incurred loss . Also determine how much profit he made or loss he incurred. cost price and selling price of an item is input by the user
sell_price=int(input("enter the selling price of item: "))
cost_price=int(input("enter the cost price of item : "))
if sell_price>cost_price:
    print("seller made profit :",sell_price-cost_price)
elif sell_price<cost_price:
    print("seller made loss : ",cost_price-sell_price)
else:
    print("seller not made loss or profit")


# In[4]:


# Question4 if the age of Ram, sulabh and Ajay are input by the user, write a program to deterime the youngest of the three.
ram=int(input("enter the ram age :"))
sulabh=int(input("enter the sulabh age :"))
ajay=int(input("enter the ajay age :"))
if ram==sulabh and ram<ajay and sulabh<ajay :
    print("ram and sulabh are youngest man")
elif sulabh==ajay and sulabh<ram and ajay<ram:
    print("sulabh and ajay are youngest man")
elif ram==ajay and ram<sulabh and ajay<sulabh:
    print("ram and ajay are youngest man")
elif ram <sulabh and ram<ajay:
    print("ram is youngest man")
elif sulabh <ram and sulabh<ajay:
    print("sulabh is youngest man")
else:
    print("ajay is youngest man")


# In[1]:


# question5 wirte a program to chec whether a traingle is valid or not , when the three angles of the triangle are entered by the user. A traingle is valid if the sum of all the three angles is equal to 180 degree.
angle1=int(input("enter angle1:"))
angle2=int(input("enter angle2:"))
angle3=int(input("enter angle3:"))
if (angle1+angle2+angle3)==180:
    print("Traingle is valid")
else:
    print("Traingle is not valid")


# In[2]:


# question7 write a program to calculate the total expenses. Quantity and price per item are input by the user and discount of 10% is offered if the expense is more than 5000.
quantity=int(input("enter number of quentity"))
expense=0
for i in range(1,quantity+1):
    item_price=int(input(f"enter price of  item number {i}"))
    expense=expense+item_price
if expense>5000:
    discount=(expense*10)/100
    print("total expense with 10% discount is :",expense-discount)
else:
    print("total expense is :",expense)
    


# In[3]:


# question7 any year is input by the user. wirte a program to determine whether the year is a leap year or not.
year=int(input("enter any year: "))
if year%4==0:
    if (year%100)!=0 or (year%400==0):
        print("givin number is leap year")
    else:
        print("given year is not leap year")
else:
    print("year is not leap year")
        


# In[4]:


# question8 in a company an employee is paid as under :
# if his basic salary is less than rs 1500, then HRA=10% OF basic salary. and DA =90% of basic salary
# if his salary is either equal to or above rs 1500, then HRA = rs 500  and DA=98%, of basic salary. 
# if the employee's salary is input by the user write a program to find his  gross salary.

basic_salary=float((input("enter the salary")))
if basic_salary<1500 and basic_salary>0:
    hra=(basic_salary*10)/100
    da=(basic_salary*90)/100
    print("Gross salary is ",basic_salary+hra+da)
elif basic_salary>1500:
    hra=500
    da=(basic_salary%98)/100
    print("Gross salary is ",basic_salary+hra+da)
else:
    print("Gross salary is ",basic_salary)
    
    
    
    
    


# In[5]:


# # write9 a program to calculate the monthly telephone bills as per the following rule:
# minimum rs. 200 for upto 100 calls. plus rs 0.60 per call for next 50 calls.
# pluss rs. 0.50 per call for next 50 call
# plus rs. 0.40 per call for any call
# beyond 200 calls.

number_of_calls=int(input("Enter the number of calls :"))
if number_of_calls<=100:
    bill=200
    print(bill)
elif number_of_calls<=150:
    bill=200+(number_of_calls-100)*0.60
    print(bill)
elif number_of_calls<=200:
    bill=200+(50*0.60)+(number_of_calls-150)*0.50
    print(bill)
else:
    bill=200+(50*0.60)+(50*0.50)+(number_of_calls-200)*0.40
    print(bill)
    


# In[6]:


# the mark obtained by a student in 5 different subjects are input by the user . The students gets  a division as per the following rules: perentage above or equal to 60 -first dividion percentage between 50 and 59 second division
#     percentage between 40 and 49 - third division percentage less than 40 fail
#     write a program to calculate division obtained by the student 

sub1=int(input("enter sub1 marks : "))
sub2=int(input("enter sub2 marks : "))
sub3=int(input("enter sub3 marks : "))
sub4=int(input("enter sub4 marks : "))
sub5=int(input("enter sub5 marks : "))
total=sub1+sub2+sub3+sub4+sub5
percentage=(total*100)/500
if percentage>100:
    print("invalid inputs")
elif percentage>=60:
    print("first division")
elif percentage>=50:
    print("second division")
elif percentage>=40:
    print("third division")
else:
    print("fail")











# In[10]:


# question11 any character is entered by the user; write a program to determine whether the character entered is a capital letter. a small case letter, a digit or a pecial symbol. the following tabel show the range of ASCII values for various characters.
char=input("enter any character : ")
ascii_code=ord(char)
if ascii_code>=65 and ascii_code<=90:
    print("this character is a Capital letter")
elif ascii_code>=97 and ascii_code<=122:
    print("this character is a small letter")
elif ascii_code>=48 and ascii_code<=57:
    print("this character is a digit")
else:
    print("this characte is a special symbol")


# In[ ]:





# In[ ]:




