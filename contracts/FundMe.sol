// SPDX-License-Identifier: MIT
pragma solidity 0.8.11;
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

contract FundMe {
    mapping(address => uint256) public addressToAmountFunded;
    mapping(address => bool) public addressExist;
    address[] funders;
    address public owner;

    constructor() {
        owner = msg.sender;
    }

    function fund() public payable {
        // Pay minimum $50
        uint256 minimumUsd = 50 * 10**18;
        require(
            getConversionRate(msg.value) >= minimumUsd,
            "Need to spend more ETH!"
        );

        addressToAmountFunded[msg.sender] += msg.value;
        if (!addressExist[msg.sender]) {
            addressExist[msg.sender] = true;
            funders.push(msg.sender);
        }
    }

    function getVersion() public view returns (uint256) {
        AggregatorV3Interface priceFeed = AggregatorV3Interface(
            0x8A753747A1Fa494EC906cE90E9f37563A8AF630e
        );
        return priceFeed.version();
    }

    function getPrice() public view returns (uint256) {
        AggregatorV3Interface priceFeed = AggregatorV3Interface(
            0x8A753747A1Fa494EC906cE90E9f37563A8AF630e
        );
        (, int256 answer, , , ) = priceFeed.latestRoundData();
        return uint256(answer * 10000000000);
    }

    // 1000000000 WEI = 1 GWEI
    function getConversionRate(uint256 ethAmount)
        public
        view
        returns (uint256)
    {
        uint256 ethPrice = getPrice();
        uint256 ethAmountInUsd = (ethPrice * ethAmount) / 1000000000000000000;
        // 0.000004039010000000
        return ethAmountInUsd;
    }

    modifier onlyOwner() {
        require(msg.sender == owner);
        _;
    }

    function withdraw() public payable onlyOwner {
        payable(msg.sender).transfer(address(this).balance);
        for (
            uint256 funderIndex = 0;
            funderIndex < funders.length;
            funderIndex++
        ) {
            addressToAmountFunded[funders[funderIndex]] = 0;
            addressExist[funders[funderIndex]] = false;
        }
        funders = new address[](0);
    }
}
