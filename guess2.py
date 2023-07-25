import random
low = 1
high = 100
mid = (low+high)/2
number = random.randint(low,high)
counter =1
while True:
    if number==mid:
        print("congrats")
        break
    elif number<mid: 
        high=mid-1
        counter+=1
        mid=(low+high)/2
    else:
        low=mid+1
        mid=(low+high)/2
        counter+=1

print("Bot took "+ str(counter)+" Trys")
