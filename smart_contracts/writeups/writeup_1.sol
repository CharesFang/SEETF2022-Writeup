// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface Target {
    function setWelcomeMessage(string memory _welcomeMessage) external;
}

contract Writeup {
    Target private target =  Target(0x5cf50385021BDFf8Afa19dFF6aeba231346d8DF1);

    function attack() external {
        string memory my_msg = "Welcome to SEETF";
        target.setWelcomeMessage(my_msg);
    }
}

