import re
name = input("Enter your name: ")
# := walrus operator  
if matches := re.search(r"^(.+), ?(.+)$",name):
    name =f"{matches.group(2).strip()} {matches.group(1)}"
print("Hello,",name)