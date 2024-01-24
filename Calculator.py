print(''' 
__________________________________
| simple = calculator             |
| USES To Add +,Subtract -,       |
| Multiply * , Divide /           |
| REGARDS:: Hackerboy             | 
| CHANEL:: https://t.me/h4cker_boy|
|_________________________________|

 we Make first termux tool give feedback on our telegram channel''')

num1  = eval(input("enter the number"))
num2= eval(input("enter the number"))
opr = input ("enter the oprator")
if opr == '+' :
  print(num1+num2)
if opr == '-' :
  print(num1-num2)
if opr == '*' :
  print(num1*num2)
elif opr == '/' :
  print (num1/num2)
else :
  print ("invailed operator")