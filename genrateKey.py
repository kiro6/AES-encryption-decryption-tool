import secrets

key = secrets.token_hex(32)

print(bytes.fromhex(key) )
