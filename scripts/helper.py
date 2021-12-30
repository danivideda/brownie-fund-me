from brownie import MockV3Aggregator, accounts, network, config
from web3 import Web3

LOCAL_BLOCKCHAIN_ENVIRONTMENTS = ["development", "ganache-local"]
PRIVATE_KEY = config["wallets"]["private_key"]
DECIMALS = 8
STARTING_PRICE = 2000 * 10 ** 8


def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONTMENTS:
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


def deploy_mocks(account):
    print(f"the active network is: {network.show_active()}")
    print("deploying mocks...")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": account})
    print("Mocks deployed")
