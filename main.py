
import time
import testselect
import initialization
import control
import CapacitanceTest
import loadtest
import voltagetest
import efficiency
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
estop = 0

tests, load, eff, volt = testselect.testsel()
passedtests = 0

if ((tests >> 4) & 1) == 1:
    captest = CapacitanceTest.capacitancetest()
    if captest == 1:
        passedtests |= 0b10000

if (((tests >> 3) & 1) == 1) & estop == 0:
    estop, pf, fullvout, medvout, lowvout, fullvin, medvin, lowvin, fullcout, medcout, lowcout, fullcin, medcin, lowcin = efficiency.runefftest(wattage, load)
    if pf == 1:
        passedtests |= 0b01000

if (((tests >> 2) & 1) == 1) & estop == 0:
    estop, pf, fulload, medload, lowload = loadtest.runloadtest(wattage, load)
    if pf == 1:
        passedtests |= 0b00100

if (((tests >> 0) & 1) == 1) & estop == 0:
    estop, pf, pin1, pin2, pin4, pin6, pin9, pin10,  pin11, pin12, pin13, pin14, pin21, pin22, pin23 = voltagetest.volatgetest(volt)
    if pf == 1:
        passedtests |= 0b00001