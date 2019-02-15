class Client:
	def __init__(self,last_name,first_name,street_address,city,zip_code,phone,email,account_number,number_of_accounts,balance):
		self.last_name = last_name
		self.first_name = first_name
		self.street_address =street_address
		self.city = city 
		self.zip_cde = zip_code
		self.phone = phone 
		self.email = email 
		self.account_number = account_number
		self.number_of_accounts = number_of_accounts
		self.balance = balance

	def setLastname(self,last_name):
		self.last_name = last_name

	def setFirstname(self):
		self.first_name= first_name

	def setStreet_address(self,street_address):
		self.street_address = street_address

	def setCity(self,city):
		self.city = city 

	def setZip_code(self,zip_code):
		self.zip_code = zip_code

	def setPhone(self,phone):
		self.phone = phone 

	def setEmail(self,email):
		self.email = email 

	def setAccount_number(self,account_number):
		self.account_number = account_number

	def setNumber_of_accounts(self,number_of_accounts):
		self.number_of_accounts = number_of_accounts

	def setBalance(self,balance):
		self.balance = balance

	def printClient(self):
		print(format(self.first_name,'<20'),format(street_address,'<20' ))

	def printClients(self):
		print(format(self.last_name,'<20'),format(first_name,'<20'),format(street_address,'<20'),format(self.city,'20'),format(self.zip_code,'20'),format(self.phone,'20'),format(self.email,'20'),format(self.account_number,'20'),format(self.balance,'<20'),format(self.number_of_accounts,'<20'))


def menu():
	print('1. Look up and print the client name and address ')
	print('2 Add a new client ')
	#print('3. Change the Last Name of a client ')
	#print('4. Change the account balance of a client ')
	#print('5. Correct a street address ')
	print('3. Search for a client by last name ')
	print('4. Print the data of all the clients in a tabular format ')
	print('5. Get help ')
	print('6. Quit the program ')
	print('To change info about a client enter 1')



#print('10. Balance in primary account')
#last name search last name
def searchClient(clients):
	found = 0 
	look_up = input("Enter the client's name: ")
	for x in clients:
		if (x.last_name == look_up):
			x.printClient()
			found = 1
	if found == 0:
		print('Client not found.')

def showClients(clients):
	for x in clients:
		x.printClients()

#add a new client
def addClient(clients):
	last_name = input("Enter client's last name: ")
	first_name = input("Enter client's first name: ")
	street_address = input("Enter client's street address: ")
	city = input("Enter clients city name: ")
	zip_code = input("Enter clients zip code: ")
	phone = input("Enter clients phone number: ")
	email = input("Enter clients email: ")
	account_number = input("Enter account number: ")
	number_of_accounts = input("How many accounts do they have: ")
	balance = float(input("Enter balance in primary account: "))
	return Clients(last_name,first_name,street_address,city,zip_code,phone,email,account_number,number_of_accounts,balance)

#to change clients info
def ClientMenu(clients):
        print(format("First Name",'<20'),format("ID Number",'<20'),format("Gpa",'<20'),format("Expected Grade",'<20'),format("Full/Part time",'<20'))
        for x in clients:
                x.printClients()
        choice = input("Select Client number or enter 0 for menu : ")
        if choice =='0':
                menu()
        elif(int(choice)-1<len(clients)):
                clientS[int(students)-1].printClient()
                print('1-Change client last name')
                print('2-Change account balance')
                print('3-Correct street address')
                user_choice = int(input('Choose one: '))
                if user_choice == '1':
                        last_name = input('Enter new last name: ')
                        clients[int(choice)-1].setLastname(last_name)
                elif user_choice == '2':
                        changeBal = float(input('Enter new balance: '))
                        clients[int(choice)-1].setBalance(changeBal)
                elif user_choice =='3':
                        correctAddress = input('Enter new address: ')
                        clients[int(choice)-1].setStreet_address(correctAddress)
                else:
                        print('invaild enter a vaild option')
                        menu()

#search client last name
def searchClientLast(clients):
	print()
	client_search = input("Enter clients last name: ")
	error = 0
	for x in clients:
                if (x.last_name==client_search):
                        x.printClients()
                        error = 1
                if error == 0 :
                        print('Student not found')

#show all clients
def showAllClients(clients):
        print(format('Last name ','<20'),format('first Name','<20'),format('street address','<20'),format('City','20'),format('Zip ','20'),format('Phone ','20'),format('Email','20'),format('Account number','20'),format('Number of Accounts','<20'),format('Balance in primary account'))
        for x in clients:
                x.printClients()

def getHelp():
	pass
def clientData(clients):
	clients.append(Client('Campuzano','Angel','Some random street 1','Waco','78574','122-111-2343','someemailaddress@domail.com','7964343','7','12123.90'))
	clients.append(Client('cortez','Clarissa','Some random street 5','San Antiono','73574','122-111-5432','random@somedomain.com','2866558','4','23482.76'))
	clients.append(Client('muller','muller','Some random street 4','Houston','76574','122-890-7832','random2@somedomain.com','4363658','2','10023.23'))
	clients.append(Client('olvier','John','Some random street 3','Dallas','77674','122-891-8932','firstlast@domail.com','364878','2','12312.21'))
	clients.append(Client('vador','Lord','Some random street 2','Austin','78774','122-111-3243','lastfirst@domain.com','7864358','1','65422.56'))

clientData(clients)
choice = '0'
clients = []
while choice != '9':
	print('***************************')
	menu()
	if choice == '1':
		ClientMenu(clients)
	elif choice == '2':
		 clients.append(Client(addClient(clients)))
	elif choice == '3':
		searchClient(clients)
	elif choice =='4':
		showAllClients(clients)
	elif choice =='5':
		getHelp()
	elif choice == '6':
		exit()
