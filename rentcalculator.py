#inputs we need from the user
#total rent
#total foods ordered for snacking
#electricity units spend
#charge per unit
#persons living in room/flat

##output
#total amount you have to pay is

rent= int(input("Enter your flat/house rent = "))
food=int(input("Enter the amount of food ordered = "))
electricity_spend= int(input("Enter the total electricity spend = "))
charge_per_unit= int(input("Enter the charge per unit = "))
persons=int(input("Enter the number of persons living in room/flat = "))

total_bill=electricity_spend * charge_per_unit
output=(food+rent+total_bill)/persons

print("Each person will pay = ",output)

