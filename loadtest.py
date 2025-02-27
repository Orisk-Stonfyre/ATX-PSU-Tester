from os import waitpid

import  control
import time
import spicmds
from control import deasertpson


def asert400full():
    control.asertb1load()
    control.asertb2load()
    control.asertb3load()
    control.asertb4load()

def asert400med():
    control.asertb1load()
    control.asertb2load()

def asert400low():
    control.asertb1load()

def asert430full():
    control.asertb1load()
    control.asertb2load()
    control.asertb3load()
    control.asertb4load()

def asert430med():
    control.asertb1load()
    control.asertb2load()

def asert430low():
    control.asertb1load()

def asert500full():
    control.asertb1load()
    control.asertb2load()
    control.asertb3load()
    control.asertb4load()
    control.asertb5load()

def asert500med():
    control.asertb1load()
    control.asertb2load()

def asert500low():
    control.asertb1load()

def asert550full():
    control.asertb1load()
    control.asertb2load()
    control.asertb3load()
    control.asertb4load()
    control.asertb5load()

def asert550med():
    control.asertb1load()
    control.asertb2load()
    control.asertb3load()

def asert550low():
    control.asertb1load()

def asert600full():
    control.asertb1load()
    control.asertb2load()
    control.asertb3load()
    control.asertb4load()
    control.asertb5load()
    control.asertb6load()

def asert600med():
    control.asertb1load()
    control.asertb2load()
    control.asertb3load()

def asert600low():
    control.asertb1load()

def asert650full():
    control.asertb1load()
    control.asertb2load()
    control.asertb3load()
    control.asertb4load()
    control.asertb5load()
    control.asertb6load()

def asert650med():
    control.asertb1load()
    control.asertb2load()
    control.asertb3load()

def asert650low():
    control.asertb1load()

def asert700full():
    control.asertb1load()
    control.asertb2load()
    control.asertb3load()
    control.asertb4load()
    control.asertb5load()
    control.asertb6load()

def asert700med():
    control.asertb1load()
    control.asertb2load()
    control.asertb3load()
    control.asertb4load()

def asert700low():
    control.asertb1load()

def asert750full():
    control.asertb1load()
    control.asertb2load()
    control.asertb3load()
    control.asertb4load()
    control.asertb5load()
    control.asertb6load()
    control.asertb7load()

def asert750med():
    control.asertb1load()
    control.asertb2load()
    control.asertb3load()
    control.asertb4load()

def asert750low():
    control.asertb1load()

def asert800full():
    control.asertb1load()
    control.asertb2load()
    control.asertb3load()
    control.asertb4load()
    control.asertb5load()
    control.asertb6load()
    control.asertb7load()
    control.asertb8load()

def asert800med():
    control.asertb1load()
    control.asertb2load()
    control.asertb3load()
    control.asertb4load()

def asert800low():
    control.asertb1load()

def asert850full():
    control.asertb1load()
    control.asertb2load()
    control.asertb3load()
    control.asertb4load()
    control.asertb5load()
    control.asertb6load()
    control.asertb7load()
    control.asertb8load()

def asert850med():
    control.asertb1load()
    control.asertb2load()
    control.asertb3load()
    control.asertb4load()

def asert850low():
    control.asertb1load()
    control.asertb2load()

def asert900full():
    control.asertb1load()
    control.asertb2load()
    control.asertb3load()
    control.asertb4load()
    control.asertb5load()
    control.asertb6load()
    control.asertb7load()
    control.asertb8load()
    control.asertb9load()

def asert900med():
    control.asertb1load()
    control.asertb2load()
    control.asertb3load()
    control.asertb4load()
    control.asertb5load()

def asert900low():
    control.asertb1load()
    control.asertb2load()

def asert950full():
    control.asertb1load()
    control.asertb2load()
    control.asertb3load()
    control.asertb4load()
    control.asertb5load()
    control.asertb6load()
    control.asertb7load()
    control.asertb8load()
    control.asertb9load()
    control.asertb10load()

def asert950med():
    control.asertb1load()
    control.asertb2load()
    control.asertb3load()
    control.asertb4load()
    control.asertb5load()

def asert950low():
    control.asertb1load()
    control.asertb2load()

def asert1000full():
    control.asertb1load()
    control.asertb2load()
    control.asertb3load()
    control.asertb4load()
    control.asertb5load()
    control.asertb6load()
    control.asertb7load()
    control.asertb8load()
    control.asertb9load()
    control.asertb10load()

def asert1000med():
    control.asertb1load()
    control.asertb2load()
    control.asertb3load()
    control.asertb4load()
    control.asertb5load()

def asert1000low():
    control.asertb1load()
    control.asertb2load()

full_map = {
    400: asert400full,
    430: asert430full,
    500: asert500full,
    550: asert550full,
    600: asert600full,
    650: asert650full,
    700: asert700full,
    750: asert750med,
    800: asert800full,
    850: asert850full,
    900: asert900full,
    950: asert950full,
    1000: asert1000full,
}
med_map = {
    400: asert400med,
    430: asert430med,
    500: asert500med,
    550: asert550med,
    600: asert600med,
    650: asert650med,
    700: asert700med,
    750: asert750med,
    800: asert800full,
    850: asert850full,
    900: asert900med,
    950: asert950med,
    1000: asert1000full,
}
low_map = {
    400: asert400low,
    430: asert430low,
    500: asert500low,
    550: asert550low,
    600: asert600low,
    650: asert650low,
    700: asert700low,
    750: asert750low,
    800: asert800full,
    850: asert850full,
    900: asert900full,
    950: asert950full,
    1000: asert1000full,
}

def runloadtest(wattage, loadselect):
    estop = 0
    fullvoltage=0
    medvoltage=0
    lowvoltage=0
    if ((loadselect >> 2) & 1) == 1:
        control.deasertallrelays()
        print("Running Low Load Test:")
        low_map[wattage]()
        print("Load Aserted")
        control.asert12vrelays()
        print("Relays Aserted")
        control.asertpson()
        print("Power Aserted")
        time.sleep(.5)
        psok = spicmds.readpsok()
        if psok == 5:
            print("Power Nominal")
            print("Measuring load")
            lowvoltage = spicmds.readv2()
            print(lowvoltage)
            control.deasertpson()
            print("Power Down")
            control.deasert12vrelays()
            control.deasertload()
            print("Relays Deaserted")
            print("Load Deaserted")
        else:
            control.deasertpson()
            estop = 1
            print("Fatal Error : All Tests Stopped : Power Supply Unstable")

    if (((loadselect >> 1) & 1) == 1) & estop ==0:
        control.deasertallrelays()
        print("Running Med Load Test:")
        med_map[wattage]()
        print("Load Aserted")
        control.asert12vrelays()
        print("Relays Aserted")
        control.asertpson()
        print("Power Aserted")
        time.sleep(.5)
        psok = spicmds.readpsok()
        if psok == 5:
            print("Power Nominal")
            print("Measuring load")
            medvoltage = spicmds.readv2()
            print(medvoltage)
            control.deasertpson()
            print("Power Down")
            control.deasert12vrelays()
            control.deasertload()
            print("Relays Deaserted")
            print("Load Deaserted")
        else:
            control.deasertpson()
            estop = 1
            print("Fatal Error : All Tests Stopped : Power Supply Unstable")
    if (((loadselect >> 0) & 1) == 1) & estop ==0:
        control.deasertallrelays()
        print("Running Med Load Test:")
        full_map[wattage]()
        print("Load Aserted")
        control.asert12vrelays()
        print("Relays Aserted")
        control.asertpson()
        print("Power Aserted")
        time.sleep(.5)
        psok = spicmds.readpsok()
        if psok == 5:
            print("Power Nominal")
            print("Measuring load")
            fullvoltage = spicmds.readv2()
            print(fullvoltage)
            control.deasertpson()
            print("Power Down")
            control.deasert12vrelays()
            control.deasertload()
            print("Relays Deaserted")
            print("Load Deaserted")
        else:
            control.deasertpson()
            estop = 1
            print("Fatal Error : All Tests Stopped : Power Supply Unstable")
    return estop, fullvoltage, medvoltage, lowvoltage