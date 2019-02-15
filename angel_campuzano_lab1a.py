print('HI coin changing Human, please enter the numbers of each coin you would like to chnage?')
half_dollars = int(input('Enter number of half dollars:'))
Quarters = int(input('Enter number of Quarters:'))
Dimes = int(input('Enter number of Dimes:'))
Nickels = int(input('Enter number of Nickels:'))
Pennies = int(input('Enter number of pennies:'))

convert_dollars = half_dollars * .50
convert_Quarters = Quarters * .25
convert_Dimes = Dimes *.10
convert_Nickels = Nickels * .05
Convert_pennies = Pennies * .01


coins_converted = convert_dollars + convert_Quarters + convert_Dimes + convert_Nickels + Convert_pennies
service_fee = coins_converted * .0477
tax = coins_converted * .01
Total = (coins_converted - service_fee) - tax

print("Your total converted to $",format(coins_converted,'.2f'))
print("Your tax is:",format(tax,'.2f'))
print("There's also a service fee which is:",format(service_fee,'.2f'))
print("Thus, the net value of your coins is",format(Total,'.2f'),"Celebrate!!")




