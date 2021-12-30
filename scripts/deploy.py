from brownie import FundMe, MockV3Aggregator, accounts, network, config
from scripts.helper import get_account, deploy_mocks, LOCAL_BLOCKCHAIN_ENVIRONTMENTS


def deploy_fund_me():
    account = get_account()

    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONTMENTS:
        deploy_mocks(account)
        price_feed_address = MockV3Aggregator[-1].address
    else:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )

    print(f"Contract deployed: {fund_me}")
    return fund_me


def main():
    deploy_fund_me()
