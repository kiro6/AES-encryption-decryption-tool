import secrets

key = secrets.token_hex(32)

print(bytes.fromhex(key) )

list  = [1,2,3,4,5,6,10]
print(list[-1])