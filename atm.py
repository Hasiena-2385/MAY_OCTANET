class ATM:
    def __init__(self,user_id,password):
        self.user_id= user_id
        self.password= password
        self.balance=0
        self.transactions=[]
        
    def login(self, user_id, password):
        return self.user_id == user_id and self.password== password
    
    def deposit(self, amount):
        self.balance+=amount
        self.transactions.append(f"Deposited ${amount}")
        print(f"Balance = {self.balance}")
    
    def withdraw(self, amount ):
        if self.balance >= amount:
            self.balance-=amount
            self.transactions.append(f"Withdraw ${amount}")
            print(f"Balance = {self.balance}")
        else:
            print("\n----------Insufficient Funds!-------------")
    
    def transfer(self, amount, recipient_id):
        if self.balance>= amount:
            self.balance -= amount
            self.transactions.append(f"Transferred ${amount} to {recipient_id}")
            print(f"Balance = {self.balance}")
        else:
            print("\n-------Insufficient Funds!------")
    
    def show_transactions(self):
        print("Transaction History:")
        for transaction in self.transactions:
            print(transaction)
            
def main():
        user_id = input("Enter User ID: ")
        password= input("Enter Password: ")
        atm=ATM(user_id= "atmuser", password="12345atm")
        
        if atm.login(user_id, password):
            while(True):
                print("\n1. Deposit\n2. Withdraw\n3. Transfer\n4. Transaction History\n5. Exit\n")
                choice= int(input("Enter Choice: "))
                
                if choice== 1:
                    amount = float(input("Enter amount to Deposit: "))
                    atm.deposit(amount)
                elif choice==2:
                    amount = float(input("Enter amount to Withdraw: "))
                    atm.withdraw(amount)
                elif choice==3:
                    amount = float(input("Enter amount to Transfer: "))
                    recipient_id = input("Enter Recipient's User ID: ")
                    atm.transfer(amount, recipient_id)
                elif choice== 4:
                    atm.show_transactions()
                elif choice==5:
                    print("----- THANK YOU for using the ATM. -----")
                    break
                else:
                    print("Invalid choice! Please try again")
                    
        else:
            print("*******Incorrect User ID or Password.***********")
            
if __name__ =="__main__":
    print("===============================================================")
    print("\n________________________ATM INTERFACE__________________________\n")
    print("===============================================================\n")
    main()
