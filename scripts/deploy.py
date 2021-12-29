from brownie import FundMe, accounts
from scripts.helper import get_account


def deploy_fund_me():
    account = get_account()
    fund_me = FundMe.deploy({"from": account})
    print(f"Contract address: {fund_me}")

def main():
    deploy_fund_me()
