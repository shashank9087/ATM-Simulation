import os
import json
import common
common
import time
import _02_user_data as _02_user_data

@common.safe 
def account_info(account_no):
    
    account_detail = {}

    with open(f"USER_DATA\\{account_no}\\{account_no}.txt", "r") as file:
        for line in file:
            key, value = line.strip().split(":", 1)
            account_detail[key] = value

    important_fields = {
        "account_number",
        "account_holder_aadhar_number",
        "account_holder_pan_number",
        "account_holder_mobile_number"
    }
    important_detail = {}
    normal_detail = {}

    for key, value in account_detail.items():
        if key in important_fields:
            important_detail[key] = value
        else:
            normal_detail[key] = value
    with open(f"USER_DATA\\{account_no}\\{account_no}.json", "w") as file:
        json.dump(account_detail, file, indent=4)
        
    with open(f"USER_DATA\\{account_no}\\{account_no}.json", "w") as file:
        json.dump(important_detail, file, indent=4)
        
    with open(f"USER_DATA\\{account_no}\\{account_no}.json", "w") as file:
        json.dump(normal_detail, file, indent=4)
        


    

class Pin_Geni:  
   
    @common.safe_sign_in
    def pin_geni(self):

        

        common.clear()        
        print(common.message.Account.pin_generation_portal)
        input("\n Press Enter To Continue !!")
        chances = 5
        while chances > 0:

            try:
                # aadhar_no_1 = int(input("Enter aadhar Number ======: "))
                account_no_1 = int(input("Enter Account Number ======: "))
                common.clear()
            except ValueError:
                print("Enter The Valid Response Only!")
                chances -= 1
                print("Remaining chances:", chances)
                common.clear()
                continue
            try:

                
                if str(account_no_1) in os.listdir("USER_DATA"):
                    with open(f"USER_DATA\\{account_no_1}\\{account_no_1}.txt", "r") as txt:
                        print("Enter the All Correct Account Details !!")
                        common.clear()
                    user = _02_user_data.New_User_Data()
                    user.user_data_input()
                    user.user_data_output(account_no_1)





                    with open(f"USER_DATA\\{account_no_1}\\{account_no_1}.txt","r") as txt:
                        str_temp_data_1 = txt.readlines()
                        for line in str_temp_data_1:
                            if line.startswith("account_holder_aadhar_number:"):
                                aadhar_no_1 = line.removeprefix("account_holder_aadhar_number:").strip()
                    with open(f"USER_DATA\\{aadhar_no_1}\\temp.txt", "r") as file:
                        temp_data_1 = file.readlines()
                    with open(f"USER_DATA\\{account_no_1}\\temp.txt","w") as txt:
                        temp_data_2 = temp_data_1.copy()
                        for line in temp_data_2:
                            if line.startswith("account_number:None"):
                                txt.write(f"account_number:{account_no_1}\n")       
                            else:
                                txt.write(line)
                                

                                
                                








                        
                    with open(f"USER_DATA\\{account_no_1}\\copy.txt","r") as txt:
                        cop_y = txt.read()
                    with open(f"USER_DATA\\{account_no_1}\\temp.txt","r") as txt:
                        temp = txt.read()
                    
                        
                    if "account_number_pin:" in cop_y:
                            print("The Pin is Alredy Exist")
                            choice = input("IF you want to change your pin type ''==Y=='' anf if not  ''N'' : ")
                            common.clear()
                            if choice.lower() == "y":
                                while chances > 0:
                                    try:
                                        while chances > 0:
                                            try:     
                                                enter_pin = int(input("Enter The Old ATM Pin: "))
                                                
                                                if len(str(enter_pin)) != 4:
                                                    print("ATM PIN Should Be Of 4 Digit Only !!")
                                                    common.clear()
                                                    chances -= 1
                                                elif len(str(enter_pin)) == 4:
                                                    break
                                            except ValueError:
                                                 chances -= 1
                                                 print("ATM PIN Should Be Of 4 Digit Only !!")
                                                 common.clear()

                                        with open(f"USER_DATA\\{account_no_1}\\{account_no_1}.txt","r") as txt:
                                            data = txt.read()
                                        if f"account_number_pin:{enter_pin}" in data:
                                            break
                                        if not f"account_number_pin:{enter_pin}" in data:
                                            print("enter the correct pin")
                                            chances -= 1
                                            print("Remaining chances:", chances)
                                            common.clear()

                                            
                                    except ValueError:
                                        chances -= 1
                                        print("Remaining chances:", chances)

                                        print("Enter The Valid Response Only!")
                                        common.clear()

                                while chances > 0:
                                            try:     
                                                enter_new_pin = int(input("Enter The New ATM Pin: "))
                                                
                                                if len(str(enter_new_pin)) != 4:
                                                    print("ATM PIN Should Be Of 4 Digit Only !!")
                                                    chances -= 1
                                                    common.clear()
                                                elif len(str(enter_new_pin)) == 4:
                                                    break
                                            except ValueError:
                                                 chances -= 1
                                                 print("ATM PIN Should Be Of 4 Digit Only !!")
                                                 common.clear()
                                with open(f"USER_DATA\\{account_no_1}\\{account_no_1}.txt","r") as txt:
                                    data_1 = txt.readlines() 
                                with open(f"USER_DATA\\{account_no_1}\\{account_no_1}.txt","w") as txt:
                                        
                                        for line in data_1:
                                            if line.startswith("account_number_pin:"):
                                                txt.write(f"account_number_pin:{enter_new_pin}\n")
                                                
                                            else:
                                                txt.write(line)
                                os.remove(f"USER_DATA\\{account_no_1}\\copy.txt")
                                os.remove(f"USER_DATA\\{account_no_1}\\temp.txt")
                                break    
                            elif choice.lower() == "n":
                                print("your pin is not changed")
                                common.clear()
                                os.remove(f"USER_DATA\\{account_no_1}\\copy.txt")
                                os.remove(f"USER_DATA\\{account_no_1}\\temp.txt")
                                break

                    elif cop_y == temp:
                            with open(f"USER_DATA\\{account_no_1}\\{account_no_1}.txt","a") as txt:
                                while chances > 0:
                                    try:     
                                        enter_new_pin = int(input("Enter The New ATM Pin: "))
                                        common.clear()
                                        if len(str(enter_new_pin)) != 4:
                                            print("ATM PIN Should Be Of 4 Digit Only !!")
                                            chances -= 1
                                            common.clear()
                                        elif len(str(enter_new_pin)) == 4:
                                            account_info(account_no_1)
                                            break
                                    except ValueError:
                                            chances -= 1
                                            print("ATM PIN Should Be Of 4 Digit Only !!")
                                            common.clear()
                                txt.write(f"account_number_pin:{enter_new_pin}\n")
                                os.remove(f"USER_DATA\\{account_no_1}\\copy.txt")
                                os.remove(f"USER_DATA\\{account_no_1}\\temp.txt")
                            account_info(account_no_1)
                            break
                    else:
                            print("Fill The Correct Account Details !! ")
                            common.clear()


                else:
                    print("Account Number Not Found")
                    chances -= 1
                    print("Remaining chances:", chances)
                    common.clear()
            except Exception as e :
                print(e)
        try:
                     
            os.remove(f"USER_DATA\\{aadhar_no_1}\\temp.txt")
            os.rmdir(f"USER_DATA\\{aadhar_no_1}")
        except Exception as e:
             pass

# Pin_Geni().pin_geni()




