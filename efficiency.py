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
    fullpin = 0
    medpin = 0
    lowpin = 0
    pf = 1
    if ((loadselect >> 2) & 1) == 1:
        control.deasertallrelays()
        print("Running Low Load Efficiency Test:")
        low_map[wattage]()
        print("Load Aserted")
        control.asert12vrelays()
        print("Relays Aserted")
        control.asertpson()
        time.sleep(3)
        print("Power Aserted")
        time.sleep(.5)
        psok = spicmds.readpsok()
        if (psok >= 2.4) & (psok <= 5):
            print("Power Nominal")
            print("Measuring load")
            lowvoltageout = spicmds.readv2()
            print("Voltage Out")
            print(lowvoltageout)
            lowcurrentout = spicmds.readi2()
            print("Current Out")
            print(lowcurrentout)
            lowvoltagein, lowcurrentin, lowpin = spicmds.readinput()
            print("Voltage In (rms)")
            print(lowvoltagein)
            print("Current In (rms)")
            print(lowcurrentin)
            control.deasertpson()
            print("Power Down")
            control.deasert12vrelays()
            control.deasertload()
            control.deasertallrelays()
            print("Relays Deaserted")
            print("Load Deaserted")
            if lowvoltageout == 0:
                control.asertpson()
                time.sleep(3)
                control.asertpin10()
                sum = 0
                for i in range(1000):
                    sum += spicmds.readv3()
                control.deasertallrelays()
                control.deasertpin10()
                control.deasertpson()
                lowvoltageout = sum / 1000
                lowvoltageout += 7.83
                #if lowcurrentin > 20:
                   # lowcurrentin = 
            pout = lowcurrentout * lowvoltageout
            if (lowpin != 0):
                eff = pout / lowpin
            else:
                eff = 0
            if eff < .65:
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
        time.sleep(3)
        print("Power Aserted")
        time.sleep(.5)
        psok = spicmds.readpsok()
        if (psok >= 2.4) | (psok <= 5):
            print("Power Nominal")
            print("Measuring load")
            medvoltageout = spicmds.readv2()
            print("Voltage Out")
            print(medvoltageout)
            medcurrentout = spicmds.readi2()
            print("Current Out")
            print(medcurrentout)
            medvoltagein, medcurrentin, medpin = spicmds.readinput()
            print("Voltage In (rms)")
            print(medvoltagein)
            print("Current In (rms)")
            print(medcurrentin)
            control.deasertpson()
            print("Power Down")
            control.deasert12vrelays()
            control.deasertload()
            control.deasertallrelays()
            print("Relays Deaserted")
            print("Load Deaserted")
            if medvoltageout == 0:
                control.asertpson()
                time.sleep(3)
                control.asertpin10()
                sum = 0
                for i in range(1000):
                    sum += spicmds.readv3()
                control.deasertallrelays()
                control.deasertpin10()
                control.deasertpson()
                medvoltageout = sum / 1000
                medvoltageout += 7.83
            pout = medcurrentout * medvoltageout
            if (medpin != 0):
                eff = pout / medpin
            else:
                eff = 0
            if eff < .72:  # needs corrected
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
        time.sleep(3)
        print("Power Aserted")
        time.sleep(.5)
        psok = spicmds.readpsok()
        if (psok >= 2.4) | (psok <= 5):
            print("Power Nominal")
            print("Measuring load")
            fullvoltageout = spicmds.readv2()
            print("Voltage Out")
            print(fullvoltageout)
            fullcurrentout = spicmds.readi2()
            print("Current Out")
            print(fullcurrentout)
            fullvoltagein, fullcurrentin, fullpin = spicmds.readinput()
            print("Voltage In (rms)")
            print(fullvoltagein)
            print("Current In (rms)")
            print(fullcurrentin)
            control.deasertpson()
            print("Power Down")
            control.deasert12vrelays()
            control.deasertload()
            control.deasertallrelays()
            print("Relays Deaserted")
            print("Load Deaserted")
            if fullvoltageout == 0:
                control.asertpson()
                time.sleep(3)
                control.asertpin10()
                sum = 0
                for i in range(1000):
                    sum += spicmds.readv3()
                control.deasertallrelays()
                control.deasertpin10()
                control.deasertpson()
                fullvoltageout = sum / 1000
                fullvoltageout += 7.83
            pout = fullcurrentout * fullvoltageout
            if (fullpin != 0):
                eff = pout / fullpin
            else:
                eff = 0
            if eff < .70: #needs corrected
                pf = 0
                print("Full Load Test Efficiency Failed")
            else:
                print("Full Load Test Efficiency Nominal")
        else:
            control.deasertpson()
            estop = 1
            print("Fatal Error : All Tests Stopped : Power Supply Unstable")

    return estop, pf, fullvoltageout, medvoltageout, lowvoltageout, fullvoltagein, medvoltagein, lowvoltagein, fullcurrentout, medcurrentout, lowcurrentout, fullcurrentin, medcurrentin, lowcurrentin, fullpin, medpin, lowpin