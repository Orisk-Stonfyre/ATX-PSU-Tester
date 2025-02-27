
import time
import testselect
import initialization
import control
import os

temp=0
while 0 == temp:
    wattage = input("Enter Wattage of Power Supply: \n 400\n430\n500\n550\n600\n650\n700\n750\n800\n850\n900\n950\n1000")
    temp =1
    if wattage == "400":
        wattage = 400
    elif wattage == "430":
        wattage = 430
    elif wattage == "500":
        wattage = 500
    elif wattage == "550":
        wattage = 550
    elif wattage == "600":
        wattage = 600
    elif wattage == "650":
        wattage = 650
    elif wattage == "700":
        wattage = 700
    elif wattage == "750":
        wattage = 750
    elif wattage == "800":
        wattage = 800
    elif wattage == "850":
        wattage = 850
    elif wattage == "900":
        wattage = 900
    elif wattage == "950":
        wattage = 950
    elif wattage == "1000":
        wattage = 1000
    else:
        print("Invalid Wattage")
        temp = 0
    os.system('cls' if os.name == 'nt' else 'clear')

date = input("Enter Date: ")
user = input("Enter User: ")
serial = input("Enter Serial Number: ")

tests, load, eff, volt = testselect.testsel()




