from threading import Thread
import gps

version = "0.7.1"
contributors = ["Issac Kee", "Colton Lee", "Ethan Lowrey", "Kenzie"]
contributors_str = ""
for contributor in contributors:
    contributors_str += f"{contributor}, "
contributors_str += " "
contributors_str, _ = contributors_str.split(",  ", 1)


print("Welcome to the RezWheels server's scripts!")
print(f"[Version]: {version}")
print(f"[Contributors]: {contributors_str}")
print(f"[Version]: {version}")
print(f"[Version]: {version}")

GPS_Thread = Thread(gps.main())
GPS_Thread.start()
GPS_Thread.join

