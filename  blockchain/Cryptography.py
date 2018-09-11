# import sha256
from hashlib import sha256
# text to hash
text = "I am excited to learn about blockchain!"
text = text.encode()
hash_result = sha256(text)
hash_result = hash_result.hexdigest()
# print result
print(hash_result)
