// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface Target{
    function increaseBalance(uint256 _amount) external;
}

contract Writeup{
    Target public target = Target(0x8E13df48763E76168e70ad3c49F54b3ab3636e5D);

    constructor() {
        target.increaseBalance(374);
    }
}