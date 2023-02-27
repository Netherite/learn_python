print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

total_bill = 0 

#small pizza 
if size == "S": 
    total_bill += 15
    if add_pepperoni == "Y":
        total_bill += 2
        if extra_cheese == "Y":
            total_bill += 1 

#medium pizza
if size == "M": 
    total_bill += 20
    if add_pepperoni == "Y":
        total_bill += 3
        if extra_cheese == "Y":
            total_bill += 1 

#large pizza
if size == "L": 
    total_bill += 25
    if add_pepperoni == "Y":
        total_bill += 3
        if extra_cheese == "Y":
            total_bill += 1 
        

print(f"Your final bill is: ${total_bill}")

