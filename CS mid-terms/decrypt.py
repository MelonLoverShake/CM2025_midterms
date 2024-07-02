# Define the mapping between letters and their numerical values
letter_to_num = {chr(i+65): i for i in range(26)}
num_to_letter = {i: chr(i+65) for i in range(26)}

# Function to decrypt a ciphertext using the given key
def decrypt(ciphertext, key):
    plaintext = ''
    for i in range(len(ciphertext)):
        if ciphertext[i] == ' ':
            plaintext += ' '
        else:
            ct_num = letter_to_num[ciphertext[i]]
            key_num = letter_to_num[key[i]]
            pt_num = (ct_num - key_num) % 26
            plaintext += num_to_letter[pt_num]
    return plaintext

# Get the ciphertext and key as input
ciphertext = "IUTPFJVN"
key = "THISISANEXAMPLEKEYINCOMPUTERSECURITYEXAM"

# Decrypt the ciphertext using the key and print the plaintext
plaintext = decrypt(ciphertext, key)
print("Plaintext:", plaintext)
