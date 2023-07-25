import random
number = random.randint(1,100)
counter =1
def1=input("Enter your name : ")
while True:
    guess=int(input("Pick a number 1-100: "))
    if guess < number: 
        print("Higher")
        counter+=1
    if guess > number: 
        print("Lower")
        counter+=1
    if guess == number: 
        print("------")
        break

print(def1+" took "+ str(counter)+" Trys")