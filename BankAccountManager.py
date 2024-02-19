class Account:

    
    def __init__(self, acc_nbr, opening_balance):
        self.acc_nbr = acc_nbr
        self.balance = opening_balance

    
    def __str__(self):
        return f'{self.acc_nbr}\nBalance: ${self.balance:.2f}\n'
    
    
    def deposit(self, dep_amnt):
        self.balance += dep_amnt

    
    def withdrawl(self, with_amnt):
        if with_amnt > self.balance:
            print('\nFunds Unavailable/low')
        else:
            self.balance -= with_amnt
            print('\nTransaction Sucessfull')
        


class Checking(Account):

    
    def __init__(self, acc_nbr, opening_deposit):
        super().__init__(acc_nbr, opening_deposit)

    
    def __str__(self):
        return f'Checking Account: #{Account.__str__(self)}'


class Saving(Account):

    def __init__(self, saving_acc_nbr, opening_deposit):
        super().__init__(saving_acc_nbr, opening_deposit)

    def __str__(self):
        return f'Saving Account: #{Account.__str__(self)}'

class Business(Account):

    def __init__(self, business_acc_nbr, opening_deposit):
        super().__init__(business_acc_nbr, opening_deposit)

    def __str__(self):
        return f'Business Account: #{Account.__str__(self)}'

class Customer:

    def __init__(self, name, pin):
        self.name = name
        self.pin = pin
        self.accts = {'C':[], 'S':[], 'B':[]}

    def __str__(self):
        return self.name

    def open_checking(self, acc_nbr, opening_deposit):
        self.accts['C'].append(Checking(acc_nbr, opening_deposit))
    
    def open_saving(self, acc_nbr, opening_deposit):
        self.accts['S'].append(Saving(acc_nbr, opening_deposit))
    
    def open_business(self, acc_nbr, opening_deposit):
        self.accts['B'].append(Business(acc_nbr, opening_deposit))

    def get_total_deposit(self):
        total = 0
        for accnt in self.accts['C']:
            print(accnt)
            total += accnt.balance
        for accnt in self.accts['S']:
            print(accnt)
            total += accnt.balance
        for accnt in self.accts['B']:
            print(accnt)
            total += accnt.balance
        print(f'Combined deposits in all accounts is: ${total:.2f}\n')

def make_deposit(cust, acc_type, accnt_nbr, dep_amnt):
    for accnt in cust.accts[acc_type]:
        if accnt_nbr == accnt.acc_nbr:
            accnt.deposit(dep_amnt)
            return True
    return False

def make_withdraw(cust, acc_type, accnt_nbr, with_amnt):
    for accnt in cust.accts[acc_type]:
        if accnt_nbr == accnt.acc_nbr:
            accnt.withdrawl(with_amnt)
            return True
    return False

def create_accounts():
    for acc in range(123456, 1234567):
        yield acc

def check_for_credentials(custm_list, name, pin):
    for custm in custm_list:
        if custm.name == name and custm.pin == pin:
            return custm
    return False

def main():
    account_nbr = create_accounts()
    customers_list = []
    while True:
        print('\nHey Welcome to the Bank\n')
        select = int(input('Select the service:\n 1. Banking\n 2. ATM\n 3. Exit\n'))
        if select not in (1, 2, 3):
            print('Plsease select the valid option')
            continue
        if select == 3:
            break
        while True and select == 1:
            option = int(input('\nHow Can We Assist you\nPlease enter your options:\n 1: Open a new Account\n 2: Deposit money into your account\n 3: Exit the Bank\n'))
            if option not in (1, 2, 3):
                print('Please select the valid option')
                continue
            if option == 3:
                break
            if option == 1:
                exist_custm = int(input('Are you an existing customer ?\n 1. yes\n 2. no\n'))
                if exist_custm not in (1, 2):
                    print('Please select the valid option')
                    continue
            try:
                name = input('Please enter your name\n')
                pin = int(input('Please enter a four digit Pin\n'))
                acc_type = input('Please enter the type of account you want to open:\nChecking: "C", Saving: "S", Business: "B"\n')
                if option == 2:
                    accnt_nbr = int(input('Please Enter your Account number\n'))
                opening_deposit = int(input('Enter the amount you want to deposite\n'))
            except TypeError:
                print('Information you entered is not in order! Please try again')
                continue
            else:
                print('\n********************************\n')
                if option in (1,2):
                    custm = check_for_credentials(customers_list, name, pin)
                if option == 2:
                    if custm:
                        make_deposit(custm, acc_type.upper(), accnt_nbr, opening_deposit)
                        print(f'Name: {name}')
                        customers.get_total_deposit()
                    else:
                        print('Entered Credentials didnot match, Please re try')
                else:
                    if exist_custm == 2:
                        customers = Customer(name, pin)
                    elif custm:
                        customers = custm
                    else:
                        print('Entered Credentials didnot match, Please re try')
                        continue
                    if acc_type.upper() == 'C':
                        customers.open_checking(next(account_nbr), opening_deposit)
                    elif acc_type.upper() == 'S':
                        customers.open_saving(next(account_nbr), opening_deposit)
                    elif acc_type.upper() == 'B':
                        customers.open_business(next(account_nbr), opening_deposit)
                    else:
                        print('Failed to open an Account!\nPlease select the proper account type\n')
                        continue
                    customers_list.append(customers)
                    print(f'Congratulations Account has been created Sucessfully\nName: {name}\n')
                    customers.get_total_deposit()
                print('\n*****************************\n')
        while True:
            print('\nWelcome to the ATM Service\n')
            option = int(input('\nHow Can We Assist you\nPlease enter your options:\n 1: Withdraw money from ATM\n 2: Exit the Bank\n'))
            if option not in (1, 2): 
                print('Plsease select the valid option')
                continue
            if option == 2:
                break
            try:
                name = input('Please enter your name\n')
                acc_type = input('Please enter the type of account:\nChecking: "C", Saving: "S", Business: "B"\n')
                accnt_nbr = int(input('Please Enter your Account number\n'))
                pin = int(input('Please enter a four digit Pin\n'))
                withdraw_amnt = int(input('Enter the amount you want to withdraw\n'))
            except TypeError:
                print('Information you entered is not in order! Please try again')
                continue
            else:
                custm = check_for_credentials(customers_list, name, pin)
                print('\n************************************\n')
                if custm:
                    make_withdraw(custm, acc_type.upper(), accnt_nbr, withdraw_amnt)
                    print(f'Available balance:\nName: {name}')
                    custm.get_total_deposit()
                else:
                    print('Entered Credentials did not match, Please re try')
                print('\n*************************************\n')


if __name__ == '__main__':
    main()
