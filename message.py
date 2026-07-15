
class Input:
# 
    custumer_service = """
                ==========================================
                      CUSTOMER REGISTRATION SERVICE
                ==========================================

                Awaiting customer response...

                ==========================================
"""



class Choice:
    # 
    choice ="""
                ==========================================
                          ATM LOGIN PORTAL
                ==========================================

                Please choose an option:

                1. Existing User Login
                2. New User Registration
                3. Pending New User Registration
                4. Exit

                ------------------------------------------
                Enter your choice:
"""

class Login:

    PAGE = """
                ==========================================
                              LOGIN PORTAL
                ==========================================

                Please enter:

                • Account Number
                • ATM PIN

                ==========================================
"""
# 
    success = """
                ==========================================
                          LOGIN SUCCESSFUL
                ==========================================

                Welcome Back!

                Redirecting to ATM Main Menu...

                ==========================================
"""
# 
    def failed(attempts):
        import common
        common.clear()
        print(f"""
                ==========================================
                            LOGIN FAILED
                ==========================================

                Invalid Account Number or PIN.

                Remaining Attempts : {attempts}

                ==========================================
""")
# 
    locked = """
                ==========================================
                           ACCOUNT LOCKED
                ==========================================

                Maximum attempts exceeded.

                Please try again after 5 minutes.

                ==========================================
"""
# 
    aadhar_input = """
                ==========================================
                        AADHAAR VERIFICATION
                ==========================================

                Please enter your 12-digit Aadhaar Number.

                Note:
                • Ensure the number is entered correctly.
                • Do not include spaces or special symbols.
                • This information will be used for
                  identity verification purposes only.

                ==========================================
"""




class Menu:
# 
    page = """
                ==========================================
                            ATM MAIN MENU
                ==========================================

                1. Balance Inquiry
                2. Cash Deposit
                3. Cash Withdrawal
                4. Fund Transfer
                5. Change PIN
                6. Mini Statement
                7. Logout

                ==========================================
"""


class Account:
# 
    account_finalization = """
                ==========================================
                      ACCOUNT FINALIZATION PORTAL
                ==========================================

                Your registration process is almost
                complete.

                To finalize and verify your account
                details, please enter your Account Number.

                ------------------------------------------

                This will allow the system to:

                • Retrieve your account information
                • Verify registered details
                • Complete account setup

                ==========================================
"""



# 
    pin_generation_portal = """
                ==========================================
                         PIN GENERATION PORTAL
                ==========================================

                To generate or recover your ATM PIN,
                please enter your registered Account Number.

                ------------------------------------------

                • Enter a valid 10-digit Account Number.
                • Ensure the account is active.
                • This step is required for identity
                  verification.

                ==========================================
"""


# 
    REGISTRATION = """
                ==========================================
                         NEW ACCOUNT REGISTRATION
                ==========================================

                Welcome to ABC National Bank!

                We are delighted to assist you in opening
                a new savings account.

                To proceed, please keep the following
                documents/details ready:

                • Full Name
                • Date of Birth
                • Mobile Number
                • PAN Number
                • Aadhaar Number
                • Residential Address

                ------------------------------------------

                Important Instructions:

                • Enter all details carefully.
                • Ensure the information provided is
                  accurate and up-to-date.
                • Incorrect information may result in
                  account verification failure.

                Your privacy and security are our
                highest priorities.

                ------------------------------------------

                Please follow the on-screen instructions
                to complete your registration.

                ==========================================
"""

    # 
    def created(account_no):    
        print(f"""
                ==========================================
                      ACCOUNT CREATED SUCCESSFULLY
                ==========================================

                Account Number : {account_no}

                Please save your:
                • Account Number
                • ATM PIN

                These will be required for future logins.

                ==========================================
""")
# 
    info = """
                ==========================================
                          ACCOUNT INFORMATION
                ==========================================
"""


class Deposit:

    page = """
                ==========================================
                        CASH DEPOSIT
                ==========================================

                Welcome to the Cash Deposit Service.

                Please enter the amount you wish to
                deposit into your account.

                ------------------------------------------
                Note:
                • Enter the amount in whole numbers.
                • Ensure the cash is valid and genuine.

                ==========================================

    """
    def sucess(amoun_t,total_balanc_e):
        print(f"""
                ==========================================
                    CASH DEPOSIT SUCCESSFUL
                ==========================================

                Amount Deposited : ₹{amoun_t:,.2f}
                Total Balance    : ₹{total_balanc_e:,.2f}

                Your account has been credited
                successfully.

                Please collect your transaction receipt
                if available.

                ------------------------------------------
                Thank you for banking with us!
                ==========================================

    """)

    FAILED = """
                ==========================================
                         CASH DEPOSIT FAILED
                ==========================================

                Unable to process transaction.

                ==========================================
"""


class Withdrawal:

    pin = """
                ==========================================
                         SECURITY VERIFICATION
                ==========================================

                Please enter your ATM PIN.

                ==========================================
"""

    page = """
                ==========================================
                      CASH WITHDRAWAL
                ==========================================

                Welcome to the Cash Withdrawal Service.

                Please enter the amount you wish to
                withdraw from your account.

                ------------------------------------------
                Note:
                • Enter the amount in whole numbers.
                • Ensure you have sufficient balance.
                • Collect your cash after the transaction.

                ==========================================

"""
    def success(amoun_t,total_balanc_e):
        print(f"""
                ==========================================
                    CASH WITHDRAWAL SUCCESSFUL
                ==========================================

                Amount Withdrawn : ₹{amoun_t:,.2f}
                Total Balance    : ₹{total_balanc_e:,.2f}

                Please collect your cash.

                Please collect your transaction receipt
                if available.

                ------------------------------------------
                Thank you for banking with us!
                ==========================================

    """)

    insufficient = """
                ==========================================
                       INSUFFICIENT BALANCE
                ==========================================

                Transaction could not be completed.

                ==========================================
"""
# 
    invalid_pin = """
                ==========================================
                            INVALID PIN
                ==========================================

                Please enter the correct PIN.

                ==========================================
"""


class FundTransfer:

    enter_fund_message = """

                ==========================================
                          FUND TRANSFER
                ==========================================

                Please enter the amount you want to transfer.

                • Amount must be greater than ₹0.
                • Ensure you have sufficient balance.
                • Transfer amount will be deducted
                  from your account immediately.

                ------------------------------------------


"""

    PAGE = """
                ==========================================
                            FUND TRANSFER
                ==========================================

                Enter:

                • Recipient Account Number
                • Recipient Name

                ==========================================
                """

    VERIFIED = """
                ==========================================
                       BENEFICIARY VERIFIED
                ==========================================

                Account verified successfully.

                ==========================================
"""

    SUCCESS = """
                ==========================================
                      FUND TRANSFER SUCCESSFUL
                ==========================================

                Recipient : {name}

                Amount    : ₹{amount:,.2f}

                ==========================================
                """

    insuficient = """
                ==========================================
                          TRANSACTION FAILED
                ==========================================

                Insufficient Balance!

                Your account does not have enough funds
                to complete this transfer.

                Please enter a smaller amount or
                deposit money and try again.

                ------------------------------------------

                """

    FAILED = """
                ==========================================
                       FUND TRANSFER FAILED
                ==========================================

                Invalid beneficiary details.

                ==========================================
                """


class Statement:
                # 
                    page = """
                ==========================================
                           MINI STATEMENT
                ==========================================

                Displaying recent transactions.

                ==========================================
                """

                    END = """
                ==========================================
                       END OF TRANSACTION LIST
                ==========================================
                """


class Pin:
                
                    PAGE = """
                ==========================================
                             CHANGE PIN
                ==========================================

                Enter:

                • Current PIN
                • New PIN

                ==========================================
                """

                    SUCCESS = """
                ==========================================
                      PIN UPDATED SUCCESSFULLY
                ==========================================

                Your PIN has been updated.

                ==========================================
                """


class Logout:
                
                    PAGE = """
                ==========================================
                            LOGGING OUT
                ==========================================

                Thank you for using
                ABC National Bank ATM Services.

                Have a Nice Day!

                ==========================================
                """


class Errors:
                
                    INVALID_INPUT = """
                ==========================================
                            INVALID INPUT
                ==========================================

                Please enter a valid response.

                ==========================================
                """

                    FEATURE = """
                ==========================================
                          FEATURE COMING SOON
                ==========================================

                This functionality is under development.

                ==========================================
                """

                    FILE_ERROR = """
                ==========================================
                             FILE ERROR
                ==========================================

                Unable to access account data.

                ==========================================
"""

class Pending_sign_in:

    Account_setup_menu ="""
                        ==========================================
                            ACCOUNT SETUP MENU
                        ==========================================

                        Please choose one of the following options:

                        1. Generate Account Number
                        (Requires Aadhaar Verification)

                        2. Generate ATM PIN
                        (Requires Account Number Verification)

                        ------------------------------------------

                        Enter Your Choice (1-2): 
    """