### How Hashing Maintains the Blockchain's Integrity
- In a blockchain, each block has a unique hash and a link to the previous block’s hash. If a participant decides to tamper with a block by modifying the transactions, the block’s unique hash gets changed. However, the following block does not update to reflect this change — it still points to the previous block’s hash. Thus, there is a mismatch between hashes and the link between blocks is broken. This results in an invalid copy of the blockchain.

- In this way, the records in the blockchain cannot be altered. In other words, the records are said to be immutable.

##### Key Terms:
- __Hashing__: Generating a random string of characters from a given input.
- __Immutable__: Something whose records can’t be changed.