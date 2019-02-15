def main():

	def band_mem():
		pass

	def bagage(x):
		print()
		airplane_ticket = float(input('Hello band member {} Enter the cost of your airplane ticket: '.format(x)))
		baggage_weight = float(input('Enter the total weight of your baggage: '))
		if baggage_weight > 30:
			baggage_weight = baggage_weight - 30 
		return baggage_weight,airplane_ticket

	baggage_weight_1,airplane_ticket1 = bagage(x = 1)
	baggage_weight_2,airplane_ticket2 = bagage(x = 2 )
	baggage_weight_3,airplane_ticket3 = bagage(x = 3)
	

	def excess_baggage(baggage_weight_1,baggage_weight_2,baggage_weight_3):
		cost_of_baggage1 = baggage_weight_1 * 9
		cost_of_baggage2 = baggage_weight_2 * 9
		cost_of_baggage3 = baggage_weight_3 * 9
		total_cost_of_baggage = cost_of_baggage1 + cost_of_baggage2 + cost_of_baggage3
		#total_cost_of_baggage = (baggage_weight_1 * 9) + (baggage_weight_2) + (baggage_weight_3*())
		return total_cost_of_baggage
	total_cost_of_baggage = excess_baggage(baggage_weight_1,baggage_weight_2,baggage_weight_3)

	#cost function will calculate:
	# total on airplane tickets 
	# total on excess baggage - $9 per each lb over 30 
	# Home rental - $1300 per band member
	# van rental - $450
	# total per diem paid out
	def costs(airplane_ticket1,airplane_ticket2,airplane_ticket3,total_cost_of_baggage):
		Home_rental = 1300
		van_rental = 450
		diem_rate = (85 * 3) * 7
		total_airplane_cost = airplane_ticket1 + airplane_ticket2 + airplane_ticket3
		total_cost = float(total_airplane_cost) + float(total_cost_of_baggage) + float(Home_rental) + float(van_rental) + float(diem_rate)
		return total_airplane_cost, total_cost,Home_rental, van_rental,diem_rate
	total_airplane_cost,total_cost, Home_rental,van_rental,diem_rate = costs(airplane_ticket1,airplane_ticket2,airplane_ticket3,total_cost_of_baggage)
		

	def merch_sold(x):
		items_sold = float(input('Enter the number of {} items sold: '.format(x)))
		return items_sold
	print()
	items_sold_1 = merch_sold(x = "T-shirt") # cost = $25
	items_sold_2 = merch_sold(x = "Beer mug") # cost = $15
	items_sold_3 = merch_sold(x = "Poster") # cost = $11
	items_sold_4 = merch_sold(x = "Coffee") # cost = $16
	items_sold_5 = merch_sold(x = "Bobblehead doll") # cost = $22

	#will be called 3 times
	def calulate_rev(items_sold_1,items_sold_2,items_sold_3,items_sold_4,items_sold_5):
		total_merch = (items_sold_1 * 25) + (items_sold_2*15) + (items_sold_3*11) + (items_sold_4*16) + (items_sold_5*22)
		Honorarium = 1500
		total_rev = total_merch + Honorarium
		return total_merch,Honorarium,total_rev

	total_merch,Honorarium,total_rev = calulate_rev(items_sold_1,items_sold_2,items_sold_3,items_sold_4,items_sold_5)

	def output(total_airplane_cost,total_cost_of_baggage,Home_rental,van_rental,diem_rate,total_cost,total_merch,Honorarium,total_rev):
		print()
		print("====================")
		print("For SXSW your financials look like:")
		print(format("Item","20"),format("Cost","30"))

		#print(format(temp,"<20,.2f"),format(wind,"<30,.2f"),format(wct,"<30,.2f"))

		print(format("Air tickets","20"),format(total_airplane_cost,'<30,.2f'))

		print(format("Baggage","20"),format(total_cost_of_baggage,'<30,.2f'))

		print(format("Home rental","20"),format(Home_rental,'<30,.2f'))
		
		print(format("Van rental","20"),format(van_rental,'<30,.2f'))
		
		print(format("Per diem Total","20"),format(diem_rate,'<30,.2f'))
		
		print(format("Total cost","20"),format(total_cost,'<30,.2f'))

		print()
		print()
		print()
		
		print(format("Item","20"),format("Revenue","30"))
		
		print(format("Merchandise","20"),format(total_merch,'<30,.2f'))
		
		print(format("Honorarium","20"),format(Honorarium,'<30,.2f'))
		
		print(format("Total Revenues","20"),format(total_rev,'<30,.2f'))
	output(total_airplane_cost,total_cost_of_baggage,Home_rental,van_rental,diem_rate,total_cost,total_merch,Honorarium,total_rev)



main()
