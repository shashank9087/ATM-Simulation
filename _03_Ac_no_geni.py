import os
import random
import common
common


class Ac_No_Geni:
    @common.safe_sign_in
    def ac_no_geni(self):
        common.clear()
        print(common.message.Login.aadhar_input)
        self.temp_ac_no = int(input("Enter The Aadhar Number: "))
        common.clear()
        self.account_number = random.randint(1000000000, 9999999999)
        with open(f"USER_DATA\\{self.temp_ac_no}\\{self.temp_ac_no}.txt","r") as txt:
            data_1 = txt.read()
        with open(f"USER_DATA\\{self.temp_ac_no}\\{self.temp_ac_no}.txt","r") as txt:
            data_2 = txt.readlines()

        if "account_number:None" in data_1:            
            if "account_holder_aadhar_number:" in data_1:
                with open(f"USER_DATA\\{self.temp_ac_no}\\{self.temp_ac_no}.txt","w") as txt:
                    for line in data_2:
                        if line.startswith("account_number:None"):
                            txt.write(f"account_number:{self.account_number}\n")  
                            print("account_number: ",self.account_number)       
                        else:
                            txt.write(line)
        common.clear()
        
        if "account_number:" in data_1:
            for line in data_2:
                    try:
                        os.rename(
                            f"USER_DATA\\{self.temp_ac_no}",
                            f"USER_DATA\\{self.account_number}"
                        )
                        os.rename(
                            f"USER_DATA\\{self.account_number}\\{self.temp_ac_no}.txt",
                            f"USER_DATA\\{self.account_number}\\{self.account_number}.txt"
                        )

                        break
                    except FileNotFoundError:
                        print("Something Went Wrong!!")
        Ac_No_Geni.generated_account_no = self.account_number
        common.message.Account.created(Ac_No_Geni.generated_account_no)
        input("\n Press Enter To Continue !!")
        common.clear()
        return self.account_number




# Ac_No_Geni.ac_no_geni()