
import time
import testselect
import initialization
import control
import CapacitanceTest
import loadtest
import voltagetest
import efficiency
import rippletest
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

date = input("Enter Date (mm_dd_yy): ")
user = input("Enter User: ")
serial = input("Enter Serial Number: ")
estop = 0
allpass = 1

tests, load, eff, volt, ripple = testselect.testsel()
passedtests = 0

if ((tests >> 4) & 1) == 1:
    captest = CapacitanceTest.capacitancetest()
    if captest == 1:
        passedtests |= 0b10000
    else:
        allpass = 0

if (((tests >> 3) & 1) == 1) & estop == 0:
    estop, pf, fullvout, medvout, lowvout, fullvin, medvin, lowvin, fullcout, medcout, lowcout, fullcin, medcin, lowcin = efficiency.runefftest(wattage, load)
    if pf == 1:
        passedtests |= 0b01000
    else:
        allpass = 0

if (((tests >> 2) & 1) == 1) & estop == 0:
    estop, pf, fulload, medload, lowload = loadtest.runloadtest(wattage, load)
    if pf == 1:
        passedtests |= 0b00100
    else:
        allpass = 0

if (((tests >> 1) & 1) == 1) & estop == 0:
    estop, pf, rpin1, rpin2, rpin4, rpin6, rpin9, rpin10,  rpin11, rpin12, rpin13, rpin14, rpin21, rpin22, rpin23 = rippletest.runrippletest(ripple)
    if pf == 1:
        passedtests |= 0b00010
    else:
        allpass = 0

if (((tests >> 0) & 1) == 1) & estop == 0:
    estop, pf, vpin1, vpin2, vpin4, vpin6, vpin9, vpin10,  vpin11, vpin12, vpin13, vpin14, vpin21, vpin22, vpin23 = voltagetest.voltagetest(volt)
    if pf == 1:
        passedtests |= 0b00001
    else:
        allpass = 0

if estop == 0:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Tests Complete")
    if allpass == 1:
        print("All Tests Passed")
    else:
        print("One Or more Tests Failed")
        if (((passedtests >> 4) & 1) == 0) & ((tests >> 4) & 1) == 1:
            print("Capacitance Test Failed")
        if (((passedtests >> 3) & 1) == 0) & ((tests >> 3) & 1) == 1:
            print("Efficiency Test Failed")
        if (((passedtests >> 2) & 1) == 0) & ((tests >> 2) & 1) == 1:
            print("Load Test Failed")
        if (((passedtests >> 1) & 1) == 0) & ((tests >> 1) & 1) == 1:
            print("Ripple Test Failed")
        if (((passedtests >> 0) & 1) == 0) & ((tests >> 0) & 1) == 1:
            print("Voltage Test Failed")
    print("Compiling Test Data in Report")
