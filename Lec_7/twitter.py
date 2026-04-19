import re

url = input("Enter the URL of your x handle : ").strip().lower()

# username = re.sub(r"^(https?://)?(www\.)?x\.com/","",url,flags=re.IGNORECASE)

if matches := re.search(r"^(?:https?://)?(?:www\.)?x\.(?:com|org)/([a-z0-9_]+)$",url,flags=re.IGNORECASE):
    print(f"Username: {matches.group(1)}")
else:print("Invalid URL")
