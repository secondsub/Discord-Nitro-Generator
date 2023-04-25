import string
import random
chars = list(string.ascii_lowercase)+list(string.ascii_uppercase)+list(string.digits)
    
print("𝙽𝚒𝚝𝚛𝚘𝙶𝚎𝚗𝚎𝚛𝚊𝚝𝚘𝚛𝚋𝚢𝚜𝚎𝚌𝚘𝚗𝚍𝚜𝚞𝚋")
print("Nitro Generator by secondsub (https://github.com/secondsub)")
amt = int(input("How many Nitro Codes do you want to generate? "))

main = "https://discord.gift/"

import sys
sys.stdout = open("Nitrocodes.txt", "w")

for i in range(amt):
    ending = ""
    for i in range(random.randint(13,20)):
        ending += random.choice(chars)
    print(main+ending)

sys.stdout.close()