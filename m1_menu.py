import common
import m2_transaction
import json
import time
import os

common
 

class Menu:

    logged_account = None

    @staticmethod
    def menu(account_no):
        Menu.logged_account = account_no
        while True:
            print(common.message.Menu.page)

            choice = input("Enter your choice: ")

            if choice == "1":
                Menu.account_info_m()
                print(f"Checking balance for {account_no}")
                common.clear()

            elif choice == "2":
                print(f"Deposit to {account_no}")
                Menu.cash_deposit_m()
                common.clear()

            elif choice == "3":
                print(f"Withdraw from {account_no}")
                Menu.cash_withdrawal_m()
                common.clear()
            
            elif choice == "4":
                print(f"Fund Transfer from {account_no}")
                Menu.fund_transfer_m()
                common.clear()

            elif choice == "5":
                print(f"Enter The Account No")
                Menu.change_pin_m()
                common.clear()
            
            elif choice == "6":
                print(f"Statements for {account_no}")
                Menu.statement_call_m()
                common.clear()

            elif choice == "7":
                print("Logged Out Successfully")
                common.clear()
                import _01_Login
                _01_Login.Login
                break

            else:
                print("Invalid Choice")

    @common.safe_sign_in
    def account_info_m():
        logged_account_no = Menu.logged_account
        common.clear()
        print(common.message.Account.info)
        with open(f"USER_DATA\\{logged_account_no}\\{logged_account_no}.json","r") as txt:
            data = json.load(txt)
        try:
            if os.path.exists(f"USER_DATA\\{logged_account_no}\\balance.json"):
                    
                for i,b in data["a_h_d"].items():
                    print(f"{i} : {b}\n")

                with open(f"USER_DATA\\{logged_account_no}\\balance.json","r") as txt:
                    data = json.load(txt)
                    print(f"Balance : {data["Balance"]}")
            else:    
                try:
                    with open(f"USER_DATA\\{logged_account_no}\\balance.json","r") as txt:
                        data = json.load(txt)
                                                
                        for i,b in data["a_h_d"].items():
                            print(f"{i} : {b}\n")
                        print(f"Balance : {data["Balance"]}")
                except FileNotFoundError:
                    for i,b in data["a_h_d"].items():
                        print(f"{i} : {b}\n")
                    print("Your Account Does Not Have Transactional Activity\nDeposit Cash To Check Your Balance")

        except Exception as e:
            print(e ," Something Went Wromg")
        input("\n Press Enter To Continue !!")
        common.clear()        
    


    @common.safe_sign_in
    def cash_deposit_m():
        logged_account_no = Menu.logged_account

        m2_transaction.Transaction.cash_deposit_t(logged_account_no)
    @common.safe_sign_in
    def cash_withdrawal_m():
        logged_account_no = Menu.logged_account
        m2_transaction.Transaction.cash_withdrawal_t(logged_account_no)
    @common.safe_sign_in
    def change_pin_m():
        common.clear()
        import _04_pin_geni
        user =_04_pin_geni.Pin_Geni()
        user.pin_geni()
        exit()
    @common.safe_sign_in
    def statement_call_m():
            common.clear()
        
            try:    
                    call =  int(input("Enter The No Of Last Transaction Statement: "))
                    account_no = Menu.logged_account
                    path = f"USER_DATA\\{account_no}\\statement.json"
                    with open(path,"r") as stm:
                        data = json.load(stm)
                    if len(data) > call:
                        common.clear()
                        print(common.message.Statement.page)
                        for transaction in data[-call:]:
                            print(transaction,"\n")
                        print(common.message.Statement.END)
                        input("\n Press Enter To Continue !!")
                    else:
                        common.clear()
                        print(common.message.Statement.page)
                        for transaction in data:
                            print(transaction,"\n")
                        print(common.message.Statement.END)
                        input("\n Press Enter To Continue !!")

            except Exception as e:
                print(e)
                print("Enter a valid response")
            input("\n Press Enter To Continue !!")
            common.clear()
    @common.safe_sign_in
    def fund_transfer_m():
        logged_account_no = Menu.logged_account
        m2_transaction.Transaction.fund_transfer_t(logged_account_no)





            

# Menu.statement_call_m()

        
    


