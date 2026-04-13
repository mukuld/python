'''
Created on Jan 4, 2010

@author: Mukul Dharwadkar
'''
# Attempt to create a program to simulate a checking account

class chk_account(object):
    
    balance = 0
    
    def curr_bal():
        print "The current balance is:", chk_account.balance
        
    curr_bal = staticmethod(curr_bal)    
    """A sample checking account"""
    def __init__(self, name):
        print "A checking account"
        self.name = name
        print "Your account name is:", self.name
        chk_account.balance = input("How much money would you like to put in?: ")
        
    def withdraw(self, amt):
        """Method to withdraw money"""
        if chk_account.balance > expense:
            chk_account.balance = chk_account.balance - amt
        else:
            print "Not enough money, Guv"
            
#main
account1 = chk_account("CheckSave")
# print "Your account name is:" chk_account.name
chk_account.curr_bal()
#print "Your balance is:", chk_account.curr_bal()
expense = input("\nHow much money you need? " )
txn1 = account1.withdraw(expense)

chk_account.curr_bal()
