pragma solidity ^0.5.0;

contract Art {

}

address[16] public owners;

//buying art
function buy(uint artId) public returns (uint) {
  require(artId >= 0 && artId <= 15)
}
