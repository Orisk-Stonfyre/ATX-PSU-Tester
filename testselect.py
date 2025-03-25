#ask user which tasks they would like to run
#save task as lsit or array
#ask device info

#cap
#efficincy
#Load
#ripple
#voltage

import os

def printtests(tests):
    print("Selected Tests:")
    if ((tests >> 4) & 1) == 1:
        print("Capacitance Test is selected.")
    if ((tests >> 3) & 1) == 1:
        print("Efficiency Test is selected.")
    if ((tests >> 2) & 1) == 1:
        print("Load Test is selected.")
    if ((tests >> 1) & 1) == 1:
        print("Ripple Test is selected.")
    if ((tests >> 0) & 1) == 1:
        print("Voltage Test is selected.")

def printloads(load):
    print("Selected Loads:")
    if ((load >> 2) & 1) == 1:
        print("Low Load is selected.")
    if ((load >> 1) & 1) == 1:
        print("Medium Load is selected.")
    if ((load >> 0) & 1) == 1:
        print("Full Load is selected.")

def printvolt(volt):
    print("Selected Voltage Pins:")
    if ((volt >> 14) & 1) == 1:
        print("Pin 1 is selected.")
    if ((volt >> 13) & 1) == 1:
        print("Pin 2 is selected.")
    if ((volt >> 12) & 1) == 1:
        print("Pin 4 is selected.")
    if ((volt >> 11) & 1) == 1:
        print("Pin 6 is selected.")
    if ((volt >> 10) & 1) == 1:
        print("Pin 9 is selected.")
    if ((volt >> 9) & 1) == 1:
        print("Pin 10 is selected.")
    if ((volt >> 8) & 1) == 1:
        print("Pin 11 is selected.")
    if ((volt >> 7) & 1) == 1:
        print("Pin 12 is selected.")
    if ((volt >> 6) & 1) == 1:
        print("Pin 13 is selected.")
    if ((volt >> 5) & 1) == 1:
        print("Pin 14 is selected.")
    if ((volt >> 4) & 1) == 1:
        print("Pin 21 is selected.")
    if ((volt >> 3) & 1) == 1:
        print("Pin 22 is selected.")
    if ((volt >> 2) & 1) == 1:
        print("Pin 23 is selected.")
    if volt == 0b001110000011100:
        print("All 5v pins are selected.")
    if volt == 0b110000011000000:
        print("All 3.3v pins are selected.")
    if volt == 0b000001100100000:
        print("All 12v pins are selected.")

def testsel():
    tests = 0
    val = ''
    while val.lower() != 'q':
        os.system('cls' if os.name == 'nt' else 'clear')
        printtests(tests)
        print("\n")
        val = input ("Select Test(s) to Run:\n 1: Capacitance Test\n 2: Efficiency Test\n 3: Load Test\n 4: Ripple Test\n 5: Voltage Test\n a: All Tests\n r: reset Selected Tests\n q: Quit Selection\n")
        if val == '1':
            tests |= 0b10000
        elif val == '2':
            tests |= 0b01000
        elif val == '3':
            tests |= 0b00100
        elif val == '4':
            tests |= 0b00010
        elif val == '5':
            tests |= 0b00001
        elif val == 'a':
            tests |= 0b11111
        elif val == 'r':
            tests = 0
        elif val.lower() != 'q':  # handle invalid input
            print("Invalid input please select a valid test or q to quit")
    os.system('cls' if os.name == 'nt' else 'clear')
    val = ''
    load = 0
    if ((tests >> 2) & 1) == 1:#if load test
        while val.lower() != 'q':
            os.system('cls' if os.name == 'nt' else 'clear')
            printloads(load)
            print("\n")
            val = input("Load Test Configuration:\n 1: Low Load (10-20%)\n 2: Medium Load (40-60%)\n 3: Full Load (90-100%)\n a: All Loads\n r: reset Selected Loads\n q: Quit Selection\n")
            if val == '1':
                load |= 0b100
            elif val == '2':
                load |= 0b010
            elif val == '3':
                load |= 0b001
            elif val == 'a':
                load |= 0b111
            elif val == 'r':
                load = 0
            elif val.lower() != 'q':
                print("Invalid input please select a valid load or q to quit")
    os.system('cls' if os.name == 'nt' else 'clear')
    val = ''
    eff = 0
    if ((tests >> 3) & 1) == 1:
        while val.lower() != 'q':
            os.system('cls' if os.name == 'nt' else 'clear')
            printloads(eff)
            print("\n")
            val = input("Efficiency Test Configuration:\n 1: Low Load (10-20%)\n 2: Medium Load (40-60%)\n 3: Full Load (90-100%)\n a: All Loads\n r: reset Selected Loads\n q: Quit Selection\n")
            if val == '1':
                eff |= 0b100
            elif val == '2':
                eff |= 0b010
            elif val == '3':
                eff |= 0b001
            elif val == 'a':
                eff |= 0b111
            elif val == 'r':
                eff = 0
            elif val.lower() != 'q':
                print("Invalid input please select a valid load or q to quit")
    os.system('cls' if os.name == 'nt' else 'clear')
    val = ''
    volt = 0 #made an error and added 2 pins that dont exist in bit 0 and 1 deleted them but left bit if needed later so last 2 bits always 0
    if ((tests >> 0) & 1) == 1: #may also need to redo the pinout or ad diffrent configs basedon connector type, asumine std 24 pin connector
        while val.lower() != 'q':
            os.system('cls' if os.name == 'nt' else 'clear')
            printvolt(volt)
            print("\n")
            val = input("Voltage Test Configuration (By pin #)\n 1: +3.3v\n 2: +3.3v\n 4: +5v\n 6: +5v\n 9: +5v (Standby)\n 10: +12v\n 11: +12v\n 12: +3.3v\n 13: +3.3v\n 14: -12v\n 21: +5v\n 22: +5v\n 23: +5v\n 5v: All 5v Pins\n 3.3v: All 3.3v Pins\n 12v: all 12v Pins\n a: All Pins\n r: reset Selected Pins\n q: Quit Selection\n")
            if val == '1':
                volt |= 0b100000000000000
            elif val == '2':
                volt |= 0b010000000000000
            elif val == '4':
                volt |= 0b001000000000000
            elif val == '6':
                volt |= 0b000100000000000
            elif val == '9':
                volt |= 0b000010000000000
            elif val == '10':
                volt |= 0b000001000000000
            elif val == '11':
                volt |= 0b000000100000000
            elif val == '12':
                volt |= 0b000000010000000
            elif val == '13':
                volt |= 0b000000001000000
            elif val == '14':
                volt |= 0b000000000100000
            elif val == '21':
                volt |= 0b000000000010000
            elif val == '22':
                volt |= 0b000000000001000
            elif val == '23':
                volt |= 0b000000000000100
            elif val == '5v':
                volt |= 0b001110000011100
            elif val == '3.3v':
                volt |= 0b110000011000000
            elif val == '12v':
                volt |= 0b000001100100000
            elif val == 'a':
                volt |= 0b111111111111100
            elif val == 'r':
                volt = 0
            elif val.lower() != 'q':
                print("Invalid input please select a valid pin or q to quit")
    os.system('cls' if os.name == 'nt' else 'clear')

    val = ''
    ripple = 0 #made an error and added 2 pins that dont exist in bit 0 and 1 deleted them but left bit if needed later so last 2 bits always 0
    if ((tests >> 1) & 1) == 1: #may also need to redo the pinout or ad diffrent configs basedon connector type, asumine std 24 pin connector
        while val.lower() != 'q':
            os.system('cls' if os.name == 'nt' else 'clear')
            printvolt(ripple)
            print("\n")
            val = input("Ripple Test Configuration (By pin #)\n 1: +3.3v\n 2: +3.3v\n 4: +5v\n 6: +5v\n 9: +5v (Standby)\n 10: +12v\n 11: +12v\n 12: +3.3v\n 13: +3.3v\n 14: -12v\n 21: +5v\n 22: +5v\n 23: +5v\n 5v: All 5v Pins\n 3.3v: All 3.3v Pins\n 12v: all 12v Pins\n a: All Pins\n r: reset Selected Pins\n q: Quit Selection\n")
            if val == '1':
                ripple |= 0b100000000000000
            elif val == '2':
                ripple |= 0b010000000000000
            elif val == '4':
                ripple |= 0b001000000000000
            elif val == '6':
                ripple |= 0b000100000000000
            elif val == '9':
                ripple |= 0b000010000000000
            elif val == '10':
                ripple |= 0b000001000000000
            elif val == '11':
                ripple |= 0b000000100000000
            elif val == '12':
                ripple |= 0b000000010000000
            elif val == '13':
                ripple |= 0b000000001000000
            elif val == '14':
                ripple |= 0b000000000100000
            elif val == '21':
                ripple |= 0b000000000010000
            elif val == '22':
                ripple |= 0b000000000001000
            elif val == '23':
                ripple |= 0b000000000000100
            elif val == '5v':
                ripple |= 0b001110000011100
            elif val == '3.3v':
                ripple |= 0b110000011000000
            elif val == '12v':
                ripple |= 0b000001100100000
            elif val == 'a':
                ripple |= 0b111111111111100
            elif val == 'r':
                ripple = 0
            elif val.lower() != 'q':
                print("Invalid input please select a valid pin or q to quit")
    os.system('cls' if os.name == 'nt' else 'clear')

    return tests, load, eff, volt, ripple