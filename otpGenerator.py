#!usr/bin/env python3
# Creates One Time Password Generator
# Use Hexadecimal Key as Initialization Value
# Truncate hash to 16-digit Hexadecimal

import hashlib

passwords = []


def generator(keyInitiator, ranger):
    for x in range(0, ranger):
        # convert the Key Initiator into bytes
        byte_keyInitiator = bytes.fromhex(keyInitiator)

        hash_key = hashlib.sha256(byte_keyInitiator).hexdigest()
        keyInitiator = hash_key
        otp = hash_key[:16]
        passwords.append(otp)

    return passwords
