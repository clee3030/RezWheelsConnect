import subprocess
import flask_endpoint

version = "0.7.1"
contributors = ["Issac Kee", "Colton Lee", "Ethan Lowrey", "Kenzie Mccabe", "Peyton Dineyazhe"]
contributors_str = ""
for contributor in contributors:
    contributors_str += f"{contributor}, "
contributors_str += " "
contributors_str, _ = contributors_str.split(",  ", 1)
contributors_str += "."
org = "AISES"

print("Welcome to the RezWheels server!")
print(f"[Version]: {version}")
print(f"[Contributors]: {contributors_str}")
print(f"[Organization]: {org}")
Flask_API.main()
