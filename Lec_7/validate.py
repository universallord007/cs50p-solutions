import re

email = input("Enter your email address: ").strip()

# username, domain = email.split("@")

# if username and "." in domain:
#     print("Valid email address")
# else:    print("Invalid email address")

# [a-zA-Z0-9_] = \w is the same as [a-zA-Z0-9_]
if re.search(r"^[a-z0-9_\.]+@(\w+\.)?\w+\.(edu|com|org|net|gov)$",email,re.IGNORECASE):
    print("Valid email address")
else:
    print("Invalid email address")