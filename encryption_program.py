import random
import string

chars = string.punctuation + string.ascii_letters + string.digits + " "
chars = list(chars)
key = chars.copy()

random.shuffle(key)

#encryption
text = input('Enter a message to encrypt  :')
cipher = ""

for letter in text:
    index = chars.index(letter)
    cipher += key[index]

print(f"the original message is {text}")
print(f"The encrypted message is {cipher}")

#decryption
cipher = input('Enter the key to decrypt  :')
text   = ""

for character in cipher:
    index = key.index(character)
    text += chars[index]

print(f"the encrypted message is {cipher}")
print(f"The original message is {text}")