# Define the mapping between letters and their numerical values
letter_to_num = {chr(i+65): i for i in range(26)}
num_to_letter = {i: chr(i+65) for i in range(26)}

# Function to encrypt a plaintext using the given key
def encrypt(plaintext, key):
    ciphertext = ''
    for i in range(len(plaintext)):
        if plaintext[i] == ' ':
            ciphertext += ' '
        else:
            pt_num = letter_to_num[plaintext[i]]
            key_num = letter_to_num[key[i]]
            ct_num = (pt_num + key_num) % 26
            ciphertext += num_to_letter[ct_num]
    return ciphertext

# Get the plaintext and key as input
plaintext = "YEE CHONG"
key = "THISISANEXAMPLEKEYINCOMPUTERSECURITYEXAM"

# Encrypt the plaintext using the key and print the ciphertext
ciphertext = encrypt(plaintext, key)
print("Ciphertext:", ciphertext)