#!usr/bin/env python3
# Creates One Time Password Generator
# Use Hexadecimal Key as Initialization Value
# Truncate hash to 12-digit Hexadecimal
# Generate and display the 1st 100 OTPs

import hashlib

passwords = []

def generator(keyInitiator, ranger):

    for x in range (0, ranger):
        # convert the Key Initiator into bytes
        byte_keyInitiator=bytes.fromhex(keyInitiator)

        hash_key = hashlib.sha256(byte_keyInitiator).hexdigest()
        keyInitiator = hash_key
        otp = hash_key[:6]
        passwords.append(otp)

    return passwords

