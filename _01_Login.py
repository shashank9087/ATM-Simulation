import _02_user_data as _02_user_data
import _03_Ac_no_geni as _03_Ac_no_geni
import _04_pin_geni as _04_pin_geni
import _05_account_info
import time
import common
common
import message
message
import os
print(os.getcwd())
import m1_menu
class Login:
    @staticmethod
    def login_page():

        chances = 3
        Login.chance = chances

        while chances > 0:

            common.clear()
            print(message.Login.PAGE)

            try:
                account_no = int(input("Enter Account Number: "))
                password = int(input("Enter Password: "))

            except ValueError:
                print("Please enter only numbers.")
                input("\nPress Enter To Continue !!")
                continue

            # PIN validation
            if not (1000 <= password <= 9999):
                print(common.message.Withdrawal.invalid_pin)
                chances -= 1
                print(f"Remaining chances: {chances}")
                input("\nPress Enter To Continue !!")
                continue

            try:
                with open(
                    f"USER_DATA\\{account_no}\\{account_no}.txt", "r"
                ) as file:
                    data = file.read()

            except FileNotFoundError:
                common.message.Login.failed(chances)
                chances -= 1
                print(f"Remaining chances: {chances}")
                input("\nPress Enter To Continue !!")
                continue

            # Login Verification
            if (
                f"account_number:{account_no}" in data
                and f"account_number_pin:{password}" in data
            ):

                common.clear()
                print(common.message.Login.success)

                input("\nPress Enter To Continue !!")
                common.clear()

                m1_menu.Menu.menu(account_no)

                return account_no

            else:

                print(common.message.Withdrawal.invalid_pin)

                chances -= 1

                print(f"Remaining chances: {chances}")

                input("\nPress Enter To Continue !!")

        # Account Locked
        common.clear()
        print(common.message.Login.locked)
        input("\nPress Enter To Continue !!")

        return None
        
    @common.safe_sign_in
    def sign_in():
            common.clear()
            print(message.Account.REGISTRATION)
            input("\n Press Enter To Continue !!")
            user = _02_user_data.New_User_Data()
            user.user_data_input()
            user.save_to_file()
            # print(message.Login.AADHAR_INPUT)
            use_r = _03_Ac_no_geni.Ac_No_Geni()
            use_r.ac_no_geni()







            # print(message.Account.CREATED)

            
            # print(message.Account.PIN_GENERATION_ACCOUNT)
            





            time.sleep(2)
            _04_pin_geni.Pin_Geni().pin_geni()





            # print(message.Account.CREATED)
            print(message.Account.account_finalization)
            account_no = int(input("Enter The Account Number: "))
            user1 = _05_account_info.Account_Info()
            user1.account_info(account_no)
            common.clear()
    
    @common.safe_sign_in
    def pending_sign_in():
        common.clear()
        chances = 3
        while chances > 0:
            
            # print(message.Pending_sign_in.Account_setup_menu)
            
            print(message.Pending_sign_in.Account_setup_menu)
            input("\n Press Enter To Continue !!")
            choice = int(input("Enter The Choice: "))
            common.clear()
            if choice == 1:
                aadhar_no = int(input("Enter The Aadhar No: "))
                print("\nVerifying Aadhaar number...")
                print("Please wait...\n")
                if str(aadhar_no) in os.listdir("USER_DATA"):
                    print("Verification Successful.")
                    print("Proceeding to account number generation...\n")
                    user = _03_Ac_no_geni.Ac_No_Geni()
                    user.ac_no_geni()
                    break
                else:
                    chances -= 1
                    print("Verification Failed.")
                    print("No customer record found for the entered Aadhaar number.")
                    print("Please contact your bank branch if the issue persists.")

            elif choice == 2:
                accounnt_no = int(input("Enter The Account No: "))
                print("\nVerifying account number...")
                print("Please wait...\n")
                if str(accounnt_no) in os.listdir("USER_DATA"):
                    print("Verification Successful.")
                    print("Proceeding to PIN generation...\n")
                    user = _04_pin_geni.Pin_Geni()
                    user.pin_geni()
                    break
                else:
                    chances -= 1
                    print("Verification Failed.")
                    print("No customer record found for the entered account number.")
                    print("Please contact your bank branch if the issue persists.")
                    print(f"Remaing chances {chances} are left!!")
            else:
                chances -= 1
                print("Enter a valid responce")
                print(f"Remaing chances {chances} are left!!")
        
        common.clear()
        print(message.Account.account_finalization)

        account_no = int(input("Enter The Account Number: "))
        _05_account_info.Account_Info.account_info(account_no)
        common.clear()


            
    @common.safe_sign_in
    def choice():

        common.clear()
        while True:

            
            print(message.Choice.choice)
            choice = int(input("Enter The Choice: "))


            if choice == 1:
                print("\n\n")
                Login.login_page()
                common.clear()
                print("\n\n")
                
            elif choice == 2:
                print("\n\n")
                Login.sign_in()
                print("\n\n")
                common.clear()
            elif choice == 3:
                Login.pending_sign_in()
                print("\n\n")
                common.clear()
            elif choice == 4:
                common.clear()
                print(message.Logout.PAGE)
                exit()
                print("\n\n")
                common.clear()


            


    

Login.choice()