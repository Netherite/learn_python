print("Welcome to the love calculator!")
name1 = input("What is your name?\n").lower()
name2 = input("What is their name?\n").lower()

#calculate how many times the letters T R U E appear in both names
#calculate how many times the letters L O V E appear in both names 
#Make that the score

combined_names = name1 + name2
#counting true 
instance_of_t = combined_names.count("t")
instance_of_r = combined_names.count("r")
instance_of_u = combined_names.count("u")
instance_of_e = combined_names.count("e")

#counting love 
instance_of_l = combined_names.count("l")
instance_of_o = combined_names.count("o")
instance_of_v = combined_names.count("v")

total_true = instance_of_t + instance_of_r + instance_of_u + instance_of_e
total_love = instance_of_l + instance_of_o + instance_of_v

result = str(total_true) + str(total_love)
int_result = int(result)

if int_result > 90 or int_result < 10:
    print(f"{int_result}%. You go together like coke and mentos")
elif int_result >= 40 or int_result <= 50:
    print(f"{int_result}%. You are alright together")
else: 
    print(f"your score is {int_result}")