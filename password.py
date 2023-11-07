import random
import string
import secrets
print("WELCOME TO PASSWORD GENERATOR")
num=int(input("Enter the length of password to generate: "))
res=''.join(secrets.choice(string.ascii_letters)for x in range(num))
print("Secure random password is: ",res)

