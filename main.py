
import time
import testselect
import initialization
import control
import CapacitanceTest

wattage = input("Enter Wattage of Power Supply: ")
date = input("Enter Date: ")
user = input("Enter User: ")
serial = input("Enter Serial Number: ")

tests, load, eff, volt = testselect.testsel()
passedtests = 0

if ((tests >> 4) & 1) == 1:
    captest = CapacitanceTest.capacitancetest()
    if captest == 1:
        passedtests |= 0b10000




