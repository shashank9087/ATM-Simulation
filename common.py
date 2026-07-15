import builtins
import json
import os
import time
import message
message



original_input = builtins.input

def my_input(prompt=""):
    value = original_input(prompt)

    if value.lower() == "exit":
        input("\n Press Enter To Exit !!")
        clear()   
        raise SystemExit(message.Logout.PAGE)
    return value



builtins.input = my_input

def safe(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            import _01_Login
            print(f"\nError: {e}")
            _01_Login.Login.login_page()      # args[0] = account_no
            return
    return wrapper

def safe_sign_in(func):
    def wrapper(*args, **kwargs):
        ATM_EXCEPTIONS = (
    KeyboardInterrupt,
    FileNotFoundError,
    PermissionError,
    OSError,
    json.JSONDecodeError,
    KeyError,
    ValueError,
    TypeError,
    IndexError,
    AttributeError,
    NameError,
    UnboundLocalError,
    ZeroDivisionError,
    OverflowError,
    RuntimeError,
)
        try:
            return func(*args, **kwargs)
        except ATM_EXCEPTIONS as e:
            import _01_Login

            print(f"\nError: {e}")
            _01_Login.Login.sign_in()      # Return to sign-in page
            return
    return wrapper

def clear():
    
    os.system("cls" if os.name == "nt" else "clear")

