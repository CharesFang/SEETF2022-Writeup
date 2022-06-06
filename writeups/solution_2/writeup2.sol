// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface Target{
    function increaseBalance(uint256 _amount) external;
}

contract Writeup{
    Target public target = Target("TARGET ADDRESS");

    constructor() {
        target.increaseBalance(374);
    }
}