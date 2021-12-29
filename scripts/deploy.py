from brownie import FundMe, accounts
from scripts.helper import get_account


def deploy_fund_me():
    account = get_account()
    fund_me = FundMe.deploy({"from": account}, publish_source=True)
    print(f"Contract deployed: {fund_me}")

def main():
    deploy_fund_me()
