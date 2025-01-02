import random
import string

ln = int(input("Enter the desired password length: "))
uc = int(input("Enter the number of uppercase letters: "))
lc = int(input("Enter the number of lowercase letters: "))
dg = int(input("Enter the number of digits: "))
symb = int(input("Enter the number of symbols: "))

def generate_password(ln, uc, lc, dg, symb):
    password = ""
    password += ''.join(random.choice(string.ascii_uppercase) for _ in range(uc))
    password += ''.join(random.choice(string.ascii_lowercase) for _ in range(lc))
    password += ''.join(random.choice(string.digits) for _ in range(dg))
    password += ''.join(random.choice(string.punctuation) for _ in range(symb))
    
    password_list = list(password)
    password = ''.join(password_list)
    random.shuffle(password_list)

    return password

password = generate_password(ln, uc, lc, dg, symb)
print("Generated Password:", password)