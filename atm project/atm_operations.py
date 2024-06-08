#Atm operations ---file name and module name
from atm_excepts import DepositError,WithdrawError,InSufficientFundError
bal=500.00
cus_name="Divya"
def deposit():

    depoamt=float(input("enter the deposite amount:"))
    if(depoamt<=0):
        raise DepositError
    else:
        global bal
        global cus_name
        bal=bal+depoamt
        print("Dear,",cus_name)

        print("ur account xxxxxxxxxxx312 credited with INR:{}".format(depoamt))
        print("now your Account xxxxxxxx312 Bal after Deposite INR:{}".format(bal))


def Withdraw():
    global bal


    Withamt=float(input("enter the withdraw amount:"))
    if(Withamt<=0):
        raise WithdrawError
    elif((Withamt+500)>bal):
        raise InSufficientFundError

    else:
        bal=bal-Withamt
        print("Dear,{}".format(cus_name))
        print("your Account xxxxxxx312 Debited with INR:{}".format(Withamt))
        print("your Account xxxxxxx312 after withdraw INR:{}".format(bal))

def Balance_Checking():
    print("Dear,{}".format(cus_name))
    print("your balance in  your account xxxxxxxxxx312 INR:{}".format(bal))
