from hashlib import sha256

new_transactions = [{'amount': '30', 'sender':'alice', 'receiver':'bob'},
               	{'amount': '55', 'sender':'bob', 'receiver':'alice'}]

# sets the amount of leading zeros that must be found in the hash produced by the nonce
difficulty = 2
nonce = 0

# creating the proof 
proof = sha256((str(new_transactions) + str(nonce)).encode()).hexdigest()
# printing proof
print(proof)


# finding a proof that has 2 leading zeros
while True:
  nonce += 1
  final_proof = sha256((str(new_transactions) + str(nonce)).encode()).hexdigest()
  if final_proof[:difficulty] == "0"*difficulty:
    print(final_proof)
    break
