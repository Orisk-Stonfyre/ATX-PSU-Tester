import  control
import time
import spicmds

def voltagetest(pins):
    pin1 = 0
    pin2 = 0
    pin4 = 0
    pin6 = 0
    pin9 = 0
    pin10 = 0
    pin11 = 0
    pin12 = 0
    pin13 = 0
    pin14 = 0
    pin21 = 0
    pin22 = 0
    pin23 = 0
    pf = 1
    estop = 0 #needs vals changed in comparison for pass/fail
    print("Begin Voltage Test")
    control.asertpson()
    print("Power On")
    time.sleep(.5)
    psok = spicmds.readpsok()
    if psok == 5: #needs changed
        if ((pins >> 14) & 1) == 1:
            print("Testing Pin 1")
            control.asertpin1()
            print("MOSFET Aserted")
            print("Measuring Voltage")
            sum = 0
            for i in range(1000):
                sum += spicmds.readv3()
            pin1 = sum / 1000
            print("Pin 1 Voltage")
            print(pin1)
            control.deasertpin1()
            print("MOSFET Deaserted")
            if 1<pin1<1:#not in range
                pf = 0
                print("Pin 1 Test Failed")
            else:
                print("Pin 1 Nominal")
        if ((pins >> 13) & 1) == 1:
            print("Testing Pin 2")
            control.asertpin2()
            print("MOSFET Aserted")
            print("Measuring Voltage")
            sum = 0
            for i in range(1000):
                sum += spicmds.readv3()
            pin2 = sum / 1000
            print("Pin 2 Voltage")
            print(pin2)
            control.deasertpin2()
            print("MOSFET Deaserted")
            if 1<pin2<1:#not in range
                pf = 0
                print("Pin 2 Test Failed")
            else:
                print("Pin 2 Nominal")
        if ((pins >> 12) & 1) == 1:
            print("Testing Pin 4")
            control.asertpin4()
            print("MOSFET Aserted")
            print("Measuring Voltage")
            sum = 0
            for i in range(1000):
                sum += spicmds.readv3()
            pin4 = sum / 1000
            print("Pin 4 Voltage")
            print(pin4)
            control.deasertpin4()
            print("MOSFET Deaserted")
            if 1<pin4<1:#not in range
                pf = 0
                print("Pin 4 Test Failed")
            else:
                print("Pin 4 Nominal")
        if ((pins >> 11) & 1) == 1:
            print("Testing Pin 6")
            control.asertpin6()
            print("MOSFET Aserted")
            print("Measuring Voltage")
            sum = 0
            for i in range(1000):
                sum += spicmds.readv3()
            pin6 = sum / 1000
            print("Pin 6 Voltage")
            print(pin6)
            control.deasertpin6()
            if 1<pin6<1:#not in range
                pf = 0
                print("Pin 6 Test Failed")
            else:
                print("Pin 6 Nominal")
            print("MOSFET Deaserted")
        if ((pins >> 10) & 1) == 1:
            print("Testing Pin 9")
            control.asertpin9()
            print("MOSFET Aserted")
            print("Measuring Voltage")
            sum = 0
            for i in range(1000):
                sum += spicmds.readv3()
            pin9 = sum / 1000
            print("Pin 9 Voltage")
            print(pin9)
            control.deasertpin9()
            print("MOSFET Deaserted")
            if 1<pin9<1:#not in range
                pf = 0
                print("Pin 9 Test Failed")
            else:
                print("Pin 9 Nominal")
        if ((pins >> 9) & 1) == 1:
            print("Testing Pin 10")
            control.asertpin10()
            print("MOSFET Aserted")
            print("Measuring Voltage")
            sum = 0
            for i in range(1000):
                sum += spicmds.readv3()
            pin10 = sum / 1000
            print("Pin 10 Voltage")
            print(pin10)
            control.deasertpin10()
            print("MOSFET Deaserted")
            if 1<pin10<1:#not in range
                pf = 0
                print("Pin 10 Test Failed")
            else:
                print("Pin 10 Nominal")
        if ((pins >> 8) & 1) == 1:
            print("Testing Pin 11")
            control.asertpin11()
            print("MOSFET Aserted")
            print("Measuring Voltage")
            sum = 0
            for i in range(1000):
                sum += spicmds.readv3()
            pin11 = sum / 1000
            print("Pin 11 Voltage")
            print(pin11)
            control.deasertpin11()
            print("MOSFET Deaserted")
            if 1<pin11<1:#not in range
                pf = 0
                print("Pin 11 Test Failed")
            else:
                print("Pin 11 Nominal")
        if ((pins >> 7) & 1) == 1:
            print("Testing Pin 12")
            control.asertpin12()
            print("MOSFET Aserted")
            print("Measuring Voltage")
            sum = 0
            for i in range(1000):
                sum += spicmds.readv3()
            pin12 = sum / 1000
            print("Pin 12 Voltage")
            print(pin12)
            control.deasertpin12()
            print("MOSFET Deaserted")
            if 1<pin12<1:#not in range
                pf = 0
                print("Pin 12 Test Failed")
            else:
                print("Pin 12 Nominal")
        if ((pins >> 6) & 1) == 1:
            print("Testing Pin 13")
            control.asertpin13()
            print("MOSFET Aserted")
            print("Measuring Voltage")
            sum = 0
            for i in range(1000):
                sum += spicmds.readv3()
            pin13 = sum / 1000
            print("Pin 13 Voltage")
            print(pin13)
            control.deasertpin13()
            print("MOSFET Deaserted")
            if 1<pin13<1:#not in range
                pf = 0
                print("Pin 13 Test Failed")
            else:
                print("Pin 13 Nominal")
        if ((pins >> 5) & 1) == 1:
            print("Testing Pin 14")
            control.asertpin14()
            print("MOSFET Aserted")
            print("Measuring Voltage")
            sum = 0
            for i in range(1000):
                sum += spicmds.readv3()
            pin14 = sum / 1000
            print("Pin 14 Voltage")
            print(pin14)
            control.deasertpin14()
            print("MOSFET Deaserted")
            if 1<pin14<1:#not in range
                pf = 0
                print("Pin 14 Test Failed")
            else:
                print("Pin 14 Nominal")
        if ((pins >> 4) & 1) == 1:
            print("Testing Pin 21")
            control.asertpin21()
            print("MOSFET Aserted")
            print("Measuring Voltage")
            sum = 0
            for i in range(1000):
                sum += spicmds.readv3()
            pin21 = sum / 1000
            print("Pin 21 Voltage")
            print(pin21)
            control.deasertpin21()
            print("MOSFET Deaserted")
            if 1<pin21<1:#not in range
                pf = 0
                print("Pin 21 Test Failed")
            else:
                print("Pin 21 Nominal")
        if ((pins >> 3) & 1) == 1:
            print("Testing Pin 22")
            control.asertpin22()
            print("MOSFET Aserted")
            print("Measuring Voltage")
            sum = 0
            for i in range(1000):
                sum += spicmds.readv3()
            pin22 = sum / 1000
            print("Pin 22 Voltage")
            print(pin22)
            control.deasertpin22()
            print("MOSFET Deaserted")
            if 1<pin22<1:#not in range
                pf = 0
                print("Pin 22 Test Failed")
            else:
                print("Pin 22 Nominal")
        if ((pins >> 2) & 1) == 1:
            print("Testing Pin 23")
            control.asertpin23()
            print("MOSFET Aserted")
            print("Measuring Voltage")
            sum = 0
            for i in range(1000):
                sum += spicmds.readv3()
            pin23 = sum / 1000
            print("Pin 23 Voltage")
            print(pin23)
            control.deasertpin23()
            print("MOSFET Deaserted")
            if 1<pin23<1:#not in range
                pf = 0
                print("Pin 23 Test Failed")
            else:
                print("Pin 23 Nominal")
    else:
        control.deasertpson()
        estop = 1
        print("Fatal Error : All Tests Stopped : Power Supply Unstable")

    return estop, pf, pin1, pin2, pin4, pin6, pin9, pin10,  pin11, pin12, pin13, pin14, pin21, pin22, pin23