from brownie import FundMe
from brownie.network import account
from scripts.helper import get_account


def fund_me():
    fund_me = FundMe[-1]
    account = get_account()
    entrace_fee = fund_me.getEntranceFee()
    # 0.025 ETH
    print("The current entrance fee is ", entrace_fee)
    print("Funding")
    fund_me.fund({"from": account, "value": entrace_fee})


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    fund_me.withdraw({"from": account})


def main():
    fund_me()
    withdraw()
