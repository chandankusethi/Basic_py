#Basic problems in python
#check even odd
num = int(input('Enter a number: '))
if (num % 2) == 0:
     print(num,'is even')
else:
     print(num,'is odd')



     #check positive , negative or 0

num = int(input('Enter a number: '))
if num>0:
     print('Positive')
elif num == 0:
     print('Zero')

else:
     print('Negative')
     
#factorial of a number
num =int(input('Enter a Number:  '))
fact = 1
if num < 0:
     print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
     print("The factorial of 0 is 1")
else:
     for i in range(1, num + 1):
          fact = fact * i
          print('The factorial of', num, 'is', fact)

          #Reversing a number
n = int(input('Enter numbre: '))
rev=0
while n>0:
     dig=n%10
     rev=rev*10+dig
     n=n//10
     print('Reverse of the number:',rev)

     #Check if is a palindrome
n = int(input('Enter number: '))
temp = n
rev=0
while(n>0):
     dig = n % 10
     rev = (rev * 10) + dig
     n = n // 10
     if(temp == rev):
          print("The number is a palindrome")
     
     else:
         print("The number isn't a palindrome")

         #fibonacci - 0 1 1 2 3 5 8......
n = int(input('Enter number: '))
a = 0
b = 1
if n < 0:
     print("Please enter a positive integer.")
elif n == 0:
     print(a)
elif n == 1:
     print(b)
else:
     for i in range(1, n):
          c = a + b
          a = b
          b = c
          print(b)

#10 is total number to print
for num in range(10):
     print(num,end='')#print nmber
     #new line after each row to display pattern correctly
     print('\n')