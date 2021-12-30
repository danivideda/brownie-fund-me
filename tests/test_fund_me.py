from os import access
from scripts.helper import get_account
from scripts.deploy import deploy_fund_me


def test_can_fund_withdraw():
    account = get_account()
    fund_me = deploy_fund_me()
    entrace_fee = fund_me.getEntranceFee()
    tx = fund_me.fund({"from": account, "value": entrace_fee})
    tx.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == entrace_fee
    tx2 = fund_me.withdraw({"from": account})
    tx2.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == 0
