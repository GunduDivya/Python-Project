#Atmmain programm
from atm_menu import menu
from atm_excepts import DepositError,WithdrawError,InSufficientFundError
from atm_operations import deposit,Withdraw,Balance_Checking
from atm_operations import cus_name
import sys
while(True):
    menu()
    try:
        ch=int(input("enter your choice:"))

        match(ch):
            case 1:
                try:
                    deposit()
                except DepositError:
                    print("dont enter -ve or zero for Deposite ammount")
                except ValueError:
                    print("Don't try to deposite alnums ,strs and special ymbols for for depositing amount")

            case 2:
                try:
                    Withdraw()
                except WithdrawError:
                    print("Don't enter -ve or zero for Withdrwaing Amount")
                except InSufficientFundError:
                    print("Dear,{}".format(cus_name))
                    print("Your account has no sufficeint balance")

                except ValueError:
                    print("Don't Enter  alnums ,strs,and special symbols for withdrwaing:")

            case 3:

                    Balance_Checking()
            case 4:
                print("Thanks for visiting our Bank ...")
                sys.exit()

            case _:
                print("your selection of operation Wrong-try again")
                sys.exit()

    except ValueError:
        print("Your choice of operation should not be alnums,strs and symbols  ---Please Try Again Later")
        sys.exit()



