# 3. WAP to perform following using class and object and multilevel inheritance
# and also use list for different users for deposit,withdraw,check balance for
# banking application
# I. Generate account number of new user and store informationlike
# account number,name,mobile no and initial balance in different list
# II. Assign a fixed value as balance for account
# III. Deposit user defined amount and display updated balance
# IV. Withdraw user defined money if user has sufficient fund otherwise
# shoe insufficient fund
# V. Check for balance
# VI. Maintain a fixed amount 3000 in the account

class Solution:
	l=[]
	AC = 12345678901

	total =0
    
	def __init__(self):
		Solution.AC +=1
		
		print("customer account no = ",Solution.AC)
	def fix(self):
		self.fixAmount = 5000	
class BankData(Solution):
	def UserData(self):
		n=  input("enter your name = ")
		self.l.append(n)
		m =input("enter your mobile no =")
		self.l.append(m)
		A =int(input("Enter your initial amount ="))
		self.l.append(A)
		AcNo=Solution.AC
		self.l.append(AcNo)
		self.total = self.l[2]
		print(self.l)
	def Diposit(self):
		d=int(input("enter the amount of deposit = "))
		self.total +=d
		print ("total balance = ",self.total)
	def withdraw(self):
		w= int(input("enter the amount want to withdraw = "))
		if(self.total - w >= self.fixAmount):
			self.total -=w
			print("total balance left = ",self.total)
		else:
			print("insufficient balance ")
	def check(self):
		print ("total balance = ",self.total)
class BankWork(BankData):
	def __init__(self):
		self.UserData()
		self.fix()
		while(True):
			a = input("Diposit =1 Withdraw = 2 checkbalance = 3 Quit = 4 ")
			if a == "1":
				self.Diposit()
			if a== "2":
				self.withdraw()
			if a == "3":
				self.check()
			if a == "4":
				self.check()
				print("Thank you Visit Again")
				return
		

t = BankWork()




    
	
    
        
		
	
        
		
   
	
