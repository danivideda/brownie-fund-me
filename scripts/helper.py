from brownie import accounts, network, config

PRIVATE_KEY = config["wallets"]["private_key"]

def get_account():
    if network.show_active() == "development":
        account = accounts[0]

        print("My Account: \n", account)

        print("All account: ")
        for i in range(len(accounts)):
            print(accounts[i])

        print("==========")
    else:
        account = accounts.add(PRIVATE_KEY)
        print("My Account: \n", account)
    
    return account