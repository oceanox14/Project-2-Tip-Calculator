#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

print("WELCOME TO TIP CALCULATOR")
bill = float(input("What was the total bill? $"))
tip_rate = int(input("what percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("how many people to split the bill? "))

total_bill=bill*(tip_rate)/100 + bill
splitted_bill=total_bill/people
final_amount = "{:.2f}".format(splitted_bill)
print(f'Per person should pay ${final_amount}')