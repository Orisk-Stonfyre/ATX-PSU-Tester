import spicmds
import control
import time



def runrippletest(pins):
    pf = 1
    estop = 0
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

    r12 = .120 #max ripple allowed in v
    r5 = .050
    r33 = .050

    print("Begin Voltage Test")
    control.asertpson()
    time.sleep(3)
    print("Power On")
    time.sleep(.5)
    psok = spicmds.readpsok()
    if (psok >= 2.4) & (psok <= 5):
        if ((pins >> 14) & 1) == 1:
            max = 0
            min = 10000
            print("Testing Pin 1")
            control.asertpin1()
            print("MOSFET Aserted")
            print("Measuring Ripple")
            for i in range(1000):
                temp = spicmds.readv3()
                if temp > max:
                    max = temp
                elif temp < min:
                    min = temp
            pin1 = max - min
            print("Pin 1 Ripple")
            print(pin1)
            control.deasertpin1()
            print("MOSFET Deaserted")
            if pin1 > r33:#not in range
                pf = 0
                print("Pin 1 Test Failed")
            else:
                print("Pin 1 Nominal")
                
        if ((pins >> 13) & 1) == 1:
            max = 0
            min = 10000
            print("Testing Pin 2")
            control.asertpin2()
            print("MOSFET Aserted")
            print("Measuring Ripple")
            sum = 0
            for i in range(1000):
                temp = spicmds.readv3()
                if temp > max:
                    max = temp
                elif temp < min:
                    min = temp
            pin2 = max - min
            print("Pin 2 Ripple")
            print(pin2)
            control.deasertpin2()
            print("MOSFET Deaserted")
            if pin2 > r33:#not in range
                pf = 0
                print("Pin 2 Test Failed")
            else:
                print("Pin 2 Nominal")
                
        if ((pins >> 12) & 1) == 1:
            max = 0
            min = 10000
            print("Testing Pin 4")
            control.asertpin4()
            print("MOSFET Aserted")
            print("Measuring Ripple")
            sum = 0
            for i in range(1000):
                temp = spicmds.readv3()
                if temp > max:
                    max = temp
                elif temp < min:
                    min = temp
            pin4 = max - min
            print("Pin 4 Ripple")
            print(pin4)
            control.deasertpin4()
            print("MOSFET Deaserted")
            if pin4 > r5:#not in range
                pf = 0
                print("Pin 4 Test Failed")
            else:
                print("Pin 4 Nominal")
                
        if ((pins >> 11) & 1) == 1:
            max = 0
            min = 10000
            print("Testing Pin 6")
            control.asertpin6()
            print("MOSFET Aserted")
            print("Measuring Ripple")

            for i in range(1000):
                temp = spicmds.readv3()
                if temp > max:
                    max = temp
                elif temp < min:
                    min = temp
            pin6 = max - min
            print("Pin 6 Ripple")
            print(pin6)
            control.deasertpin6()
            if pin6 > r5:#not in range
                pf = 0
                print("Pin 6 Test Failed")
            else:
                print("Pin 6 Nominal")
            print("MOSFET Deaserted")
            
        if ((pins >> 10) & 1) == 1:
            max = 0
            min = 10000
            print("Testing Pin 9")
            control.asertpin9()
            print("MOSFET Aserted")
            print("Measuring Ripple")

            for i in range(1000):
                temp = spicmds.readv3()
                if temp > max:
                    max = temp
                elif temp < min:
                    min = temp
            pin9 = max - min
            print("Pin 9 Ripple")
            print(pin9)
            control.deasertpin9()
            print("MOSFET Deaserted")
            if pin9 > r5:#not in range
                pf = 0
                print("Pin 9 Test Failed")
            else:
                print("Pin 9 Nominal")
                
        if ((pins >> 9) & 1) == 1:
            max = 0
            min = 10000
            print("Testing Pin 10")
            control.asertpin10()
            print("MOSFET Aserted")
            print("Measuring Ripple")

            for i in range(1000):
                temp = spicmds.readv3()
                if temp > max:
                    max = temp
                elif temp < min:
                    min = temp
            pin10 = max - min
            print("Pin 10 Ripple")
            print(pin10)
            control.deasertpin10()
            print("MOSFET Deaserted")
            if pin10 > r12:#not in range
                pf = 0
                print("Pin 10 Test Failed")
            else:
                print("Pin 10 Nominal")
                
        if ((pins >> 8) & 1) == 1:
            max = 0
            min = 10000
            print("Testing Pin 11")
            control.asertpin11()
            print("MOSFET Aserted")
            print("Measuring Ripple")

            for i in range(1000):
                temp = spicmds.readv3()
                if temp > max:
                    max = temp
                elif temp < min:
                    min = temp
            pin11 = max - min
            print("Pin 11 Ripple")
            print(pin11)
            control.deasertpin11()
            print("MOSFET Deaserted")
            if pin11 > r12:#not in range
                pf = 0
                print("Pin 11 Test Failed")
            else:
                print("Pin 11 Nominal")
                
        if ((pins >> 7) & 1) == 1:
            max = 0
            min = 10000
            print("Testing Pin 12")
            control.asertpin12()
            print("MOSFET Aserted")
            print("Measuring Ripple")

            for i in range(1000):
                temp = spicmds.readv3()
                if temp > max:
                    max = temp
                elif temp < min:
                    min = temp
            pin12 = max - min
            print("Pin 12 Ripple")
            print(pin12)
            control.deasertpin12()
            print("MOSFET Deaserted")
            if pin12 > r33:#not in range
                pf = 0
                print("Pin 12 Test Failed")
            else:
                print("Pin 12 Nominal")
                
        if ((pins >> 6) & 1) == 1:
            max = 0
            min = 10000
            print("Testing Pin 13")
            control.asertpin13()
            print("MOSFET Aserted")
            print("Measuring Ripple")

            for i in range(1000):
                temp = spicmds.readv3()
                if temp > max:
                    max = temp
                elif temp < min:
                    min = temp
            pin13 = max - min
            print("Pin 13 Ripple")
            print(pin13)
            control.deasertpin13()
            print("MOSFET Deaserted")
            if pin13 > r33:#not in range
                pf = 0
                print("Pin 13 Test Failed")
            else:
                print("Pin 13 Nominal")
                
        if ((pins >> 5) & 1) == 1:
            max = 0
            min = 10000
            print("Testing Pin 14")
            control.asertpin14()
            print("MOSFET Aserted")
            print("Measuring Ripple")

            for i in range(1000):
                temp = spicmds.readv3()
                if temp > max:
                    max = temp
                elif temp < min:
                    min = temp
            pin14 = max - min
            print("Pin 14 Ripple")
            print(pin14)
            control.deasertpin14()
            print("MOSFET Deaserted")
            if pin14 > r12:#not in range
                pf = 0
                print("Pin 14 Test Failed")
            else:
                print("Pin 14 Nominal")
                
        if ((pins >> 4) & 1) == 1:
            max = 0
            min = 10000
            print("Testing Pin 21")
            control.asertpin21()
            print("MOSFET Aserted")
            print("Measuring Ripple")

            for i in range(1000):
                temp = spicmds.readv3()
                if temp > max:
                    max = temp
                elif temp < min:
                    min = temp
            pin21 = max - min
            print("Pin 21 Ripple")
            print(pin21)
            control.deasertpin21()
            print("MOSFET Deaserted")
            if pin21 > r5:#not in range
                pf = 0
                print("Pin 21 Test Failed")
            else:
                print("Pin 21 Nominal")
                
        if ((pins >> 3) & 1) == 1:
            max = 0
            min = 10000
            print("Testing Pin 22")
            control.asertpin22()
            print("MOSFET Aserted")
            print("Measuring Ripple")

            for i in range(1000):
                temp = spicmds.readv3()
                if temp > max:
                    max = temp
                elif temp < min:
                    min = temp
            pin22 = max - min
            print("Pin 22 Ripple")
            print(pin22)
            control.deasertpin22()
            print("MOSFET Deaserted")
            if pin22 > r5:#not in range
                pf = 0
                print("Pin 22 Test Failed")
            else:
                print("Pin 22 Nominal")
                
        if ((pins >> 2) & 1) == 1:
            max = 0
            min = 10000
            print("Testing Pin 23")
            control.asertpin23()
            print("MOSFET Aserted")
            print("Measuring Ripple")

            for i in range(1000):
                temp = spicmds.readv3()
                if temp > max:
                    max = temp
                elif temp < min:
                    min = temp
            pin23 = max - min
            print("Pin 23 Ripple")
            print(pin23)
            control.deasertpin23()
            print("MOSFET Deaserted")
            if pin23 > r5:#not in range
                pf = 0
                print("Pin 23 Test Failed")
            else:
                print("Pin 23 Nominal")
    else:
        control.deasertpson()
        estop = 1
        print("Fatal Error : All Tests Stopped : Power Supply Unstable")

    return estop, pf, pin1, pin2, pin4, pin6, pin9, pin10,  pin11, pin12, pin13, pin14, pin21, pin22, pin23