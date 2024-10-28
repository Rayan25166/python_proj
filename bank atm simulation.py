balance_amount=1000
while True:
    print("\n1. \tCheck Balance")
    print("\n2. \tDeposit Money")
    print("\n3. \tWithdraw Money")
    print("\n4. \tExit")
    choice=int(input("Enter your choice"))
    if choice==1:
        print(f"The current balance ${balance_amount}")
    elif choice ==2:
        deposit_amount = float(input("Enter bthe amount"))
        balnce_amount = balance_amount + deposit_amount
        print(f" The deposited amount ${deposit_amount}"f"the current_balance ${balance_amount}")
    elif choice ==3:
        withdraw_money = float(input("Enter the amount to withdraw:"))
        if withdraw_money>balance_amount:
              print("the account has insufficient funds")
        else:
             balance_amount = balance_amount-withdraw_money
             print(f"The amount withdrawn from the account"f"${withdraw_money} the balance amount "f"${balance_amount}")


    elif choice ==4:
        break
    else:
        print("invalid entry")



