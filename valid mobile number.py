


def is_valid_mobile_number(number):
    if len(number)==10 and number[0] in["9","8","7"]:
        return True
    return False
mobile_number=input("enter the mobile number")
if is_valid_mobile_number(mobile_number):
    print("the mobile number{mobile_number} is valid")
else:
    print("the mobile number{mobile_number} is invalid")

