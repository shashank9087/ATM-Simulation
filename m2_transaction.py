import json
import os
import common
from datetime import datetime



class Transaction:
    @common.safe_sign_in   
    def cash_deposit_t(account_no,a_mount = None):
        
    
            def create_cash_deposit_file():

            
                data = {}
                balance_data = {}
                important_fields = {
                    "account_number",
                    "account_holder_mobile_number",
                    "account_number_pin",
                    "Balance"
                }


                with open(f"USER_DATA\\{account_no}\\{account_no}.txt", "r") as file:
                    
                        for line in file:
                            key, value = line.strip().split(":", 1)
                            data[key] = value
                        else:
                            data["Balance"] = 0
                        for key, value in data.items():
                            if key in important_fields:
                                balance_data[key] = value
                with open(f"USER_DATA\\{account_no}\\balance.json","w") as file:
                    json.dump(balance_data, file, indent=4)
                cash_deposit(account_n_o = account_no)


                Transaction.backup_balance(account_no)




            @common.safe_sign_in   
            def cash_deposit(account_n_o,a_mount = None):
                if a_mount == None:
                    common.clear()
                    print(common.message.Deposit.page)
                    input("\n Press Enter To Continue !!")
                if a_mount is None:
                    amount = int(input("Enter the Amount: "))
                else:
                    amount = a_mount
                common.clear()
                with open(f"USER_DATA\\{account_n_o}\\balance.json","r") as file:
                    data_1 = json.load(file)
                
                data_1["Balance"] += amount
                with open(f"USER_DATA\\{account_n_o}\\balance.json","w") as file:
                    json.dump(data_1,file,indent=4)

                total_balance = data_1["Balance"]

                common.message.Deposit.sucess(amoun_t=amount,total_balanc_e=total_balance) 
                input("\n Press Enter To Continue !!")
       
                Transaction.backup_balance(account_n_o)
                amoun_t = amount
                balanc_e = total_balance
                Transaction.statement(account_n_o, transaction_type = "Deposit", amount = amoun_t, balance =balanc_e)
                common.clear()
            if os.path.exists(f"USER_DATA\\{account_no}\\balance.json"):
                 cash_deposit(account_n_o = account_no, a_mount=a_mount)
            else:
                create_cash_deposit_file()


    @common.safe_sign_in 
    def cash_withdrawal_t(account_no,a_mount = None):
        
        common.clear()
        print(common.message.Withdrawal.page)
        input("\n Press Enter To Continue !!")
        
        if a_mount is  None:
            amount = int(input("Enter the Amount: "))
        else:
            amount = a_mount
        

        with open(f"USER_DATA\\{account_no}\\balance.json","r") as file:
            data_1 = json.load(file)
        bal_witd_chk = data_1["Balance"] - amount
        if bal_witd_chk > 0:
            try:
                password = int(input("Enter Password: "))           
            except ValueError as e:
                print("Invalid Pin")
            if str(password) == data_1["account_number_pin"]:            
                    data_1["Balance"] -= amount
                    total_balance = data_1["Balance"]
                    common.clear()
                    if a_mount == None:
                        common.message.Withdrawal.success(amoun_t= amount,total_balanc_e= total_balance)    
                        input("\n Press Enter To Continue !!")

                    with open(f"USER_DATA\\{account_no}\\balance.json","w") as file:
                        json.dump(data_1,file,indent=4)
                    total_balance = data_1["Balance"]
                    Transaction.backup_balance(account_no)
                    # input("\n Press Enter To Continue !!")
                    
                    amoun_t = amount
                    balanc_e = total_balance
                    Transaction.statement(account_no, transaction_type = "Withdrawal", amount = amoun_t, balance = balanc_e)
                    common.clear()
                    return True
            else:

                common.clear()
                if a_mount == None:
                    print(common.message.Withdrawal.invalid_pin)
                    input("\n Press Enter To Continue !!")
                return False
        else:
            common.clear()
            if a_mount == None:
                print(common.message.Withdrawal.insufficient)
                input("\n Press Enter To Continue !!")
            with open(f"USER_DATA\\{account_no}\\balance.json","w") as file:
                json.dump(data_1,file,indent=4)


            total_balance = data_1["Balance"]

            Transaction.backup_balance(account_no)
            amoun_t = amount
            balanc_e = total_balance
            Transaction.statement(account_no, transaction_type = "Failed", amount = amoun_t, balance =balanc_e)
            common.clear()
        return False
    
    @common.safe_sign_in 
    def backup_balance(account_no):
         
        with open(f"USER_DATA\\{account_no}\\balance.json","r") as file:
            data = json.load(file)
        data_1 = data["Balance"]
        if not os.path.exists(f"USER_DATA\\{account_no}\\backup_balance.txt"):
            with open(f"USER_DATA\\{account_no}\\backup_balance.txt","w") as txt:
                txt.write(f"Initial Balance: {data_1}\n")
                if not os.path.exists(f"USER_DATA\\{account_no}\\statement.json"):
                    with open(f"USER_DATA\\{account_no}\\statement.json","w") as file:
                        json.dump([],file)
                
        else:
            with open(f"USER_DATA\\{account_no}\\backup_balance.txt","a") as txt:
                txt.write(f"last balance:{data_1}\n")
            
                
    @common.safe_sign_in 
    def statement(account_no, transaction_type, amount, balance):

        path = f"USER_DATA\\{account_no}\\statement.json"
        try:
            with open(path, "r") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []
        transaction = {
            "transaction_id": f"TXN{len(data)+1:06d}",
            "date": datetime.now().strftime("%d-%m-%Y"),
            "time": datetime.now().strftime("%H:%M:%S"),
            "type": transaction_type,
            "amount": amount,
            "balance": balance,
            "message": f"{transaction_type} successful."
        }


        # transaction["transaction_id"] = f"TXN{len(data)+1:06d}"
        data.append(transaction)

        with open(path, "w") as file:
            json.dump(data, file, indent=4)
    @common.safe_sign_in 
    def fund_transfer_t(account_no):

        common.clear()
        print(common.message.FundTransfer.PAGE)
        input("\n Press Enter To Continue !!")
        transfer_account_no = int(input("Enter The Transfer Account No: "))
        transfer_account_no_name = input("Enter Account Holder Name: ").lower()
        common.clear()
        @common.safe_sign_in
        def account_check():
            chances = 3
            while chances > 0:
                if os.path.exists(f"USER_DATA\\{transfer_account_no}"):
                    with open(f"USER_DATA\\{transfer_account_no}\\{transfer_account_no}.json","r") as file:
                        transfer_account_no_data = json.load(file)
                        break
                else:
                    common.clear()
                    print("Enter The Correct Account No: ")
                    chances -= 1
                    print(f"Remaing chances are {chances}")
                    
            while chances > 0:
                if transfer_account_no_name == transfer_account_no_data["a_d"]["account_holder_name"]:
                    common.clear()
                    print(common.message.FundTransfer.VERIFIED)
                    input("\n Press Enter To Continue !!")
                    return True
                else:
                    common.clear()
                    print(common.message.FundTransfer.FAILED)
                    input("\n Press Enter To Continue !!")
                    
                    chances -= 1
                    print(f"Remaing chances are {chances}")
                    
                    return False
        @common.safe_sign_in             
        def fund_transfer():

            common.clear()
            print(common.message.FundTransfer.enter_fund_message)
            fund_amount = int(input("Enter The Amount: "))
            common.time.sleep(.5)
            print("Refering The Request To Cash Withdrawal Service\nPlease Wait...")
            common.time.sleep(2)
            
            # it call auto maticall even inside if

            if Transaction.cash_withdrawal_t(account_no = account_no,a_mount= fund_amount) == True:
                Transaction.cash_deposit_t(account_no= transfer_account_no,a_mount=fund_amount)            
            else:

                print(common.message.FundTransfer.insuficient)
                
        if account_check() == True:
            fund_transfer()


            
            

            

            


        

    

            
                    





                            
                         



# Transaction.backup_balance(1,5654)
