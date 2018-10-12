flag_enc = "xprlozuz{nl3dlc_d4wlo}"
alphabet = "abcdefghijklmnopqrstuvwxyz"
key = int(input("Enter the key (number): "))
def caesar(flag_enc, key):
    flag_dec = ""
    for c in flag_enc:
        if c in alphabet:
            flag_dec += chr(ord(c) - key)
        else:
            flag_dec += c
    return flag_dec
flag_dec = caesar(flag_enc, key)
print(flag_dec)
