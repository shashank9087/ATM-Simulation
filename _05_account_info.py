import json
class Account_Info:
    @staticmethod
    def account_info(account_no_):

        
        account_detail = {}

        with open(f"USER_DATA\\{account_no_}\\{account_no_}.txt", "r") as file:
            for line in file:
                key, value = line.strip().split(":", 1)
                account_detail[key] = value



        important_fields = {
            "account_number",
            "account_holder_aadhar_number",
            "account_holder_pan_number",
            "account_holder_mobile_number",
            "account_number_pin"
        }

        show_fields = {
            "account_holder_name",
            "account_number",
            }
        important_detail = {}
        normal_detail = {}
        account_holder_detail = {}
        data = {
    "a_d": account_detail,
    "i_d": important_detail,
    "n_d": normal_detail,
    "a_h_d": account_holder_detail
}
        

        for key, value in account_detail.items():
            if key in important_fields:
                important_detail[key] = value
            else:
                normal_detail[key] = value
        
        for key, value in account_detail.items():
            if key in show_fields:
                account_holder_detail[key] = value
            
                
        
        
        with open(f"USER_DATA\\{account_no_}\\{account_no_}.json", "w") as file:
            json.dump(data, file, indent=4)
        
            
