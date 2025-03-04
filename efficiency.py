import  control
import time
import spicmds

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


def runefftest(wattage,loadselect):
    estop = 0
    fullvoltageout = 0
    fullcurrentout = 0
    medvoltageout = 0
    medcurrentout = 0
    lowvoltageout = 0
    lowcurrentout = 0
    fullvoltagein = 0
    fullcurrentin = 0
    medvoltagein = 0
    medcurrentin = 0
    lowvoltagein = 0
    lowcurrentin = 0
    pf = 1
    if ((loadselect >> 2) & 1) == 1:
        control.deasertallrelays()
        print("Running Low Load Efficiency Test:")
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
            lowvoltageout = spicmds.readv2()
            print("Voltage Out")
            print(lowvoltageout)
            lowcurrentout = spicmds.readi1()
            print("Current Out")
            print(lowcurrentout)
            lowvoltagein = spicmds.readv1()
            print("Voltage In")
            print(lowvoltagein)
            lowcurrentin = spicmds.readi2()
            print("Current In")
            print(lowcurrentin)
            control.deasertpson()
            print("Power Down")
            control.deasert12vrelays()
            control.deasertload()
            print("Relays Deaserted")
            print("Load Deaserted")
            if ((lowvoltageout / lowvoltagein) >= 1 | (lowvoltageout / lowvoltagein) <= 1) & ((lowcurrentout / lowcurrentin) >= 1 | (lowcurrentout / lowcurrentin) <= 1):  # needs corrected
                pf = 0
                print("Low Load Efficiency Test Failed")
            else:
                print("Low Load Efficiency Test Nominal")
        else:
            control.deasertpson()
            estop = 1
            print("Fatal Error : All Tests Stopped : Power Supply Unstable")

    if (((loadselect >> 1) & 1) == 1) & estop == 0:
        control.deasertallrelays()
        print("Running Med Load Efficiency Test:")
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
            medvoltageout = spicmds.readv2()
            print("Voltage Out")
            print(medvoltageout)
            medcurrentout = spicmds.readi1()
            print("Current Out")
            print(medcurrentout)
            medvoltagein = spicmds.readv1()
            print("Voltage In")
            print(medvoltagein)
            medcurrentin = spicmds.readi1()
            print("Current In")
            print(medcurrentin)
            control.deasertpson()
            print("Power Down")
            control.deasert12vrelays()
            control.deasertload()
            print("Relays Deaserted")
            print("Load Deaserted")
            if ((medvoltageout / medvoltagein) >= 1 | (medvoltageout / medvoltagein) <= 1) & ((medcurrentout / medcurrentin) >= 1 | (medcurrentout / medcurrentin) <= 1):  # needs corrected
                pf = 0
                print("Med Load Test Efficiency Failed")
            else:
                print("Med Load Test Efficiency Nominal")
        else:
            control.deasertpson()
            estop = 1
            print("Fatal Error : All Tests Stopped : Power Supply Unstable")

    if (((loadselect >> 0) & 1) == 1) & estop ==0:
        control.deasertallrelays()
        print("Running Full Load Efficiency Test:")
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
            fullvoltageout = spicmds.readv2()
            print("Voltage Out")
            print(fullvoltageout)
            fullcurrentout = spicmds.readi1()
            print("Current Out")
            print(fullcurrentout)
            fullvoltagein = spicmds.readv1()
            print("Voltage In")
            print(fullvoltagein)
            fullcurrentin = spicmds.readi1()
            print("Current In")
            print(fullcurrentin)
            control.deasertpson()
            print("Power Down")
            control.deasert12vrelays()
            control.deasertload()
            print("Relays Deaserted")
            print("Load Deaserted")
            if ((fullvoltageout / fullvoltagein) >= 1 | (fullvoltageout / fullvoltagein) <= 1) & ((fullcurrentout / fullcurrentin) >= 1 | (fullcurrentout / fullcurrentin) <= 1): #needs corrected
                pf = 0
                print("Full Load Test Efficiency Failed")
            else:
                print("Full Load Test Efficiency Nominal")
        else:
            control.deasertpson()
            estop = 1
            print("Fatal Error : All Tests Stopped : Power Supply Unstable")

    return estop, pf, fullvoltageout, medvoltageout, lowvoltageout, fullvoltagein, medvoltagein, lowvoltagein, fullcurrentout, medcurrentout, lowcurrentout, fullcurrentin, medcurrentin, lowcurrentin