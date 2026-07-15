import os
import _03_Ac_no_geni as _03_Ac_no_geni
import common
common
class New_User_Data:

    @common.safe_sign_in 
    def user_data_input(self):
        

    
        custumer_id_fields = {
        "account_holder_name",
        "account_holder_father_name",
        "account_holder_mother_name",
        "account_holder_dob",
        "account_holder_pan_number",
        "account_holder_aadhar_number",
        "account_holder_nationality",
        "account_holder_occupation",
        "account_holder_age",
        "account_holder_email",
        "account_holder_mobile_number",
        "account_holder_gender",
        "account_holder_address",
        "account_number",
        }
        self.custumer_id = dict.fromkeys(custumer_id_fields)
        


        
            

        while True:
            common.clear()
            print(common.message.Input.custumer_service)
            try:

                self.custumer_id.update({
                    "account_holder_name": input("Enter The Account Holder Name: "),
            }) 

                common.clear()
                break
            except ValueError:
                print("Enter The Valid Response Only!")
                common.clear()

                
            common.clear()
            

            
        while True:
            print(common.message.Input.custumer_service)
            try:

                self.custumer_id.update({
                    "account_holder_father_name": input("Enter The Account Holder Father Name: "),
            })
                common.clear()
                break
            except ValueError:
                print("Enter The Valid Response Only!")
                common.clear()
            common.clear()

            
        while True:
            print(common.message.Input.custumer_service)

            try:

                self.custumer_id.update({
                    "account_holder_mother_name": input("Enter The Account Holder Mother Name: "),
            })
                common.clear()
                break
            except ValueError:
                print("Enter The Valid Response Only!")
                common.clear()
            common.clear()

            
        while True:
            print(common.message.Input.custumer_service)

            try:

                self.custumer_id.update({
                    "account_holder_dob": input("Enter The Account Holder Date Of Birth: "),
            })
                common.clear()
                break
            except ValueError:
                print("Enter The Valid Response Only!")
                common.clear()
            common.clear()

            
        while True:
            print(common.message.Input.custumer_service)

            try:

                self.custumer_id.update({
                    "account_holder_pan_number": int(input("Enter The Account Holder PAN Number: ")),
            })
                common.clear()
                break
            except ValueError:
                print("Enter The Valid Response Only!")
                common.clear()
            common.clear()

            
        while True:
            print(common.message.Input.custumer_service)

            try:

                self.custumer_id.update({
                    "account_holder_nationality": input("Enter The Account Holder Nationality: "),
            })
                common.clear()
                break
            except ValueError:
                print("Enter The Valid Response Only!")
                common.clear()
            common.clear()

            
        while True:
            print(common.message.Input.custumer_service)

            try:

                self.custumer_id.update({
                    "account_holder_aadhar_number": int(input("Enter The Account Holder Aadhar Number: ")),
            })
                common.clear()
                break
            except ValueError:
                print("Enter The Valid Response Only!")
                common.clear()
            common.clear()

            
        while True:
            print(common.message.Input.custumer_service)

            try:

                self.custumer_id.update({
                    "account_holder_occupation": input("Enter The Account Holder Occupation: "),
            })
                common.clear()
                break
            except ValueError:
                print("Enter The Valid Response Only!")
                common.clear()
            common.clear()

            
        while True:
            print(common.message.Input.custumer_service)

            try:

                self.custumer_id.update({
                    "account_holder_age": int(input("Enter The Account Holder Age: ")),
            })
                common.clear()
                break
            except ValueError:
                print("Enter The Valid Response Only!")
                common.clear()
            common.clear()

            
        while True:
            print(common.message.Input.custumer_service)

            try:

                self.custumer_id.update({
                    "account_holder_email": input("Enter The Account Holder Email: "),
            })
                common.clear()
                break
            except ValueError:
                print("Enter The Valid Response Only!")
                common.clear()
            common.clear()

            
        while True:
            print(common.message.Input.custumer_service)

            try:

                self.custumer_id.update({
                    "account_holder_mobile_number": int(input("Enter The Account Holder Mobile Number: ")),
            })
                common.clear()
                break
            except ValueError:
                print("Enter The Valid Response Only!")
                common.clear()
            common.clear()

            
        while True:
            print(common.message.Input.custumer_service)

            try:

                self.custumer_id.update({
                    "account_holder_gender": input("Enter The Account Holder Gender: "),
            })
                common.clear()
                break
            except ValueError:
                print("Enter The Valid Response Only!")
                common.clear()
            common.clear()

            

        while True:
            print(common.message.Input.custumer_service)

            try:

                self.custumer_id.update({
                    "account_holder_address": input("Enter The Account Holder Address")
            })
                common.clear()
                break
            except ValueError:
                print("Enter The Valid Response Only!")
                common.clear()
            common.clear()
            
        
        

            
            
       



        


        try:
            os.mkdir("USER_DATA")    
        except FileExistsError:
            pass


        try:
            os.makedirs(f"USER_DATA\\{self.custumer_id.get("account_holder_aadhar_number")}")
        except FileExistsError:
            pass


        with open(f"USER_DATA\\{self.custumer_id.get("account_holder_aadhar_number")}\\temp.txt", "w") as file:
            # data_1 = str(self.custumer_id)
            for key, value in sorted(self.custumer_id.items()):
                file.write(f"{key}:{value}\n")
        
        
    







        




    @common.safe_sign_in
    def save_to_file(self):

            try:
                os.mkdir("USER_DATA")
            except FileExistsError:
                pass


            try:
                os.makedirs(f"USER_DATA\\{self.custumer_id.get("account_holder_aadhar_number")}")
            except FileExistsError:
                pass
            
            
            try:
                account_no = self.custumer_id.get('account_holder_aadhar_number')
                with open(f"USER_DATA\\{account_no}\\temp.txt", "r") as file:
                    data = file.read()
                formatted_data = data.replace("),",'\n', len(self.custumer_id))
                with open(f"USER_DATA\\{account_no}\\{account_no}.txt", "w") as txt:
                    txt.write(formatted_data)
                os.remove(f"USER_DATA\\{account_no}\\temp.txt")          
            except FileNotFoundError:
                print("wtf")

    
    
    
    
    
    
    @common.safe_sign_in
    def user_data_output(self,ac_no = None):


        if ac_no is not None:
            
            try:
                with open(f"USER_DATA\\{ac_no}\\{ac_no}.txt", "r") as file:
                    data_2 = file.read()
                formatted_data = data_2.replace("),","\n", 150)
                with open(f"USER_DATA\\{ac_no}\\copy.txt", "w") as file:
                    file.write(formatted_data)
            except FileNotFoundError:
                print("Enter The Correct Account No")
            
            

        elif self.custumer_id.get("account_holder_aadhar_number") != None:
            account_no = self.custumer_id["account_holder_aadhar_number"]
            try:
                with open(f"USER_DATA\\{self.custumer_id.get("account_holder_aadhar_number")}\\{self.custumer_id.get("account_holder_aadhar_number")}.txt", "r") as file:
                    data_2 = file.read()
                formatted_data = data_2.replace("),","\n", len(self.custumer_id))
                with open(f"USER_DATA\\{account_no}\\copy.txt", "w") as file:
                    file.write(formatted_data)
            except FileNotFoundError:
                print("Enter The Account No")
        
        
        
        else:
            while True:
                
                    
                try:
               
                    account_no_double = int(input("Enter The Account No"))
                    common.clear()
                    try:
                        with open(f"USER_DATA\\{account_no_double}\\{account_no_double}.txt", "r") as file:
                            data_2 = file.read()
                        formatted_data = data_2.replace("),","\n", )
                        with open(f"USER_DATA\\{account_no_double}\\copy.txt", "w") as file:
                            file.write(formatted_data)
                    except FileNotFoundError:
                        print("Account does not exist.")
                        common.clear()
                except ValueError:
                    print("Enter The correct Account Number")
                    common.clear()
        common.clear()
            
                






            #               *************************************************************
            #               *************************************************************
            #               *************************************************************
                
                
        

