intro_message = "Welcome to the tip calculator."

print(intro_message)
total_bill = input("What was the total bill? $")
tip_percent = input("What percentage tip would you like to give? 10, 12, or 15? ")
people_split = input("How many people to split the bill? ")

user_bill_float = float(total_bill)
user_tip_percent = int(tip_percent) / 100 + 1
user_people_split = int(people_split)

final_price = (user_bill_float / user_people_split) * user_tip_percent

round_final_price = round(final_price, 2)

format_final_price = "{:.2f}".format(round_final_price)

print(f"Each person should pay: ${format_final_price}")
