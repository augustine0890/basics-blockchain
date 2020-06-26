### Proof-of-Work
- Instead of randomly being chosen to broadcast their unconfirmed block, a special group of participants, also known as miners, now need to solve a problem in order to be eligible to broadcast their block. The problem, also known as `Proof-of-Work`, takes the form of a guessing game that involves the use of hashing.
- The hash function that’s most commonly used to create the hash for the block is the SHA-256. Miners first guess a nonce value, which is then combined with the contents of the block (i.e transactions, timestamp, hash, and previous hash). They repeat this process until the desired hash is generated.
- Mining is the process of gathering blockchain data and hashing it along with a nonce until you find a particular hash. If you find a hash that satisfies the conditions set out by the protocol, you get the right to broadcast the new block to the network.
##### Key Terms:

- __Miners__: Special participants who calculate the Proof-of-Work to mine new blocks.
- __Nonce__: A number to be guessed by miners which when combined with the block produces an acceptable hash.