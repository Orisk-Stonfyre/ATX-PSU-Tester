import os

def compilereport(passedtests, tests, load, eff, volt, ripple, wattage, date, user, serial, fullvout, medvout, lowvout, fullvin, medvin, lowvin, fullcout, medcout, lowcout, fullcin, medcin, lowcin, fulload, medload, lowload, rpin1, rpin2, rpin4, rpin6, rpin9, rpin10,  rpin11, rpin12, rpin13, rpin14, rpin21, rpin22, rpin23, vpin1, vpin2, vpin4, vpin6, vpin9, vpin10,  vpin11, vpin12, vpin13, vpin14, vpin21, vpin22, vpin23):
    mountpnt = "/media/usb/"
    filename = "TestReport_" + serial + "_" + date + ".txt"
    loop = 1
    while loop == 1:
        loop = 0
        try:
            # Find the USB drive (assuming only one is connected)
            usbdrive = None
            for item in os.listdir(mountpnt):
                fullpath = os.path.join(mountpnt, item)
                if os.path.isdir(fullpath):
                    usbdrive = fullpath
                    break

            if usbdrive is None:
                print("No USB drive found.")
                loop = 1


            filepath = os.path.join(usbdrive, filename)

            with open(filepath, "a") as f:
                f.write("Power Supply Test Report\n")

                f.write("\nPower Supply Information \n")
                f.write("Wattage: " + str(wattage) + "\n")
                f.write("Serial Number: " + str(serial) + "\n")

                f.write("\nTest Information\n")
                f.write("Date: " + str(date) + "\n")
                f.write("User Who Completed Test: " + str(user) + "\n")

                f.write("\nTests Completed\n")
                if ((tests >> 4) & 1) == 1:
                    f.write("Capacitance Test Completed\n")
                if ((tests >> 3) & 1) == 1:
                    f.write("Efficiency Test Completed\n")
                if ((tests >> 2) & 1) == 1:
                    f.write("Load Test Completed\n")
                if ((tests >> 1) & 1) == 1:
                    f.write("Ripple Test Completed\n")
                if ((tests >> 0) & 1) == 1:
                    f.write("Voltage Test Completed\n")

                f.write("\nPass Fail Summary\n")
                if (((passedtests >> 4) & 1) == 0) & ((tests >> 4) & 1) == 1:
                    f.write("Capacitance Test: Fail\n")
                elif (((passedtests >> 4) & 1) == 1) & ((tests >> 4) & 1) == 1:
                    f.write("Capacitance Test: Pass\n")
                if (((passedtests >> 3) & 1) == 0) & ((tests >> 3) & 1) == 1:
                    f.write("Efficiency Test: Fail\n")
                elif (((passedtests >> 3) & 1) == 1) & ((tests >> 3) & 1) == 1:
                    f.write("Efficiency Test: Pass\n")
                if (((passedtests >> 2) & 1) == 0) & ((tests >> 2) & 1) == 1:
                    f.write("Load Test: Fail\n")
                elif (((passedtests >> 2) & 1) == 1) & ((tests >> 2) & 1) == 1:
                    f.write("Load Test: Pass\n")
                if (((passedtests >> 1) & 1) == 0) & ((tests >> 1) & 1) == 1:
                    f.write("Ripple Test: Fail\n")
                elif (((passedtests >> 1) & 1) == 1) & ((tests >> 1) & 1) == 1:
                    f.write("Ripple Test: Pass\n")
                if (((passedtests >> 0) & 1) == 0) & ((tests >> 0) & 1) == 1:
                    f.write("Voltage Test: Fail\n")
                elif (((passedtests >> 0) & 1) == 1) & ((tests >> 0) & 1) == 1:
                    f.write("Voltage Test: Pass\n")

                f.write("\n Detailed Test Results Below:\n")

                if ((tests >> 4) & 1) == 1:
                    f.write("\n Capacitance Test Results:\n")
                    if ((passedtests >> 4) & 1) == 1:
                        f.write("Power supply was able to operate under a load of 5000 uF as per ATX 2.0 Specifications\n")
                    else:
                        f.write("Power supply was unable to operate under a load of 5000 uF/n The power supply therefore does not meet ATX 2.0 Specifications\n")

                if ((tests >> 3) & 1) == 1:
                    f.write("\n Efficiency Test Results:\n")
                    if ((passedtests >> 3) & 1) == 1:
                        f.write("Power supply operated at nominal efficiency per ATX 2.0 Specifications\n")
                    else:
                        f.write("Power supply was unable to operate at nominal efficiency per ATX 2.0 Specifications\n")
                    f.write("\n Recorded efficiency and related values:\n")
                    if ((eff >> 2) & 1) == 1:
                        lowpwro = lowvout * lowcout
                        lowpwri = lowcout * lowvin
                        if lowpwri != 0:
                            loweff = lowpwro / lowpwri
                        else:
                            loweff = 0
                        f.write("Low load Efficiency: " + str(loweff) + "\n")
                        f.write("Low load power output: " + str(lowpwro) + "\n")
                        f.write("Low load power input (rms): " + str(lowpwri) + "\n")
                        f.write("Low load voltage output: " + str(lowvout) + "\n")
                        f.write("Low load voltage input (rms): " + str(lowvin) + "\n")
                        f.write("Low load current output: " + str(lowcout) + "\n")
                        f.write("Low load current input (rms): " + str(lowcin) + "\n")

                    if ((eff >> 1) & 1) == 1:
                        medpwro = medvout * medcout
                        medpwri = medcout * medvin
                        if medpwri != 0:
                            medeff = medpwro / medpwri
                        else:
                            medeff = 0
                        f.write("Medium load Efficiency: " + str(medeff) + "\n")
                        f.write("Medium load power output: " + str(medpwro) + "\n")
                        f.write("Medium load power input (rms): " + str(medpwri) + "\n")
                        f.write("Medium load voltage output: " + str(medvout) + "\n")
                        f.write("Medium load voltage input (rms): " + str(medvin) + "\n")
                        f.write("Medium load current output: " + str(medcout) + "\n")
                        f.write("Medium load current input (rms): " + str(medcin) + "\n")

                    if ((eff >> 0) & 1) == 1:
                        fullpwro = fullvout * fullcout
                        fullpwri = fullcout * fullvin
                        if fullpwri != 0:
                            fulleff = fullpwro / fullpwri
                        else:
                            fulleff = 0
                        f.write("Full load Efficiency: " + str(fulleff) + "\n")
                        f.write("Full load power output: " + str(fullpwro) + "\n")
                        f.write("Full load power input (rms): " + str(fullpwri) + "\n")
                        f.write("Full load voltage output: " + str(fullvout) + "\n")
                        f.write("Full load voltage input (rms): " + str(fullvin) + "\n")
                        f.write("Full load current output: " + str(fullcout) + "\n")
                        f.write("Full load current input (rms): " + str(fullcin) + "\n")

                if ((tests >> 2) & 1) == 1:
                    f.write("\n Load Test Results:\n")
                    if ((passedtests >> 2) & 1) == 1:
                        f.write("Power supply operated under load per ATX 2.0 Specifications\n")
                    else:
                        f.write("Power supply was unable to operate under load per ATX 2.0 Specifications\n")
                    f.write("\n Recorded Voltages Under Load:\n")
                    if ((load >> 2) & 1) == 1:
                        f.write("Low load voltage: " + str(lowload) + "\n")
                    if ((load >> 1) & 1) == 1:
                        f.write("Medium load voltage: " + str(medload) + "\n")
                    if ((load >> 0) & 1) == 1:
                        f.write("Full load voltage: " + str(fulload) + "\n")

                if ((tests >> 1) & 1) == 1:
                    f.write("\n Ripple Test Results:\n")
                    if ((passedtests >> 1) & 1) == 1:
                        f.write("DC ripple conformed to ATX 2.0 Specifications\n")
                    else:
                        f.write("DC ripple did not conform to ATX 2.0 Specifications\n")
                    f.write("\n Recorded Ripple by Pin (Taken over 1000 samples): \n")
                    if ((ripple >> 14) & 1) == 1:
                        f.write("Pin 1 voltage (pk-pk) (+3.3v): " + str(rpin1) + "\n")
                    if ((ripple >> 13) & 1) == 1:
                        f.write("Pin 2 voltage (pk-pk) (+3.3v): " + str(rpin2) + "\n")
                    if ((ripple >> 12) & 1) == 1:
                        f.write("Pin 4 voltage (pk-pk) (+5v): " + str(rpin4) + "\n")
                    if ((ripple >> 11) & 1) == 1:
                        f.write("Pin 6 voltage (pk-pk) (+5v): " + str(rpin6) + "\n")
                    if ((ripple >> 10) & 1) == 1:
                        f.write("Pin 9 voltage (pk-pk) (+5v): " + str(rpin9) + "\n")
                    if ((ripple >> 9) & 1) == 1:
                        f.write("Pin 10 voltage (pk-pk) (+12v): " + str(rpin10) + "\n")
                    if ((ripple >> 8) & 1) == 1:
                        f.write("Pin 11 voltage (pk-pk) (+12v): " + str(rpin11) + "\n")
                    if ((ripple >> 7) & 1) == 1:
                        f.write("Pin 12 voltage (pk-pk) (+3.3v): " + str(rpin12) + "\n")
                    if ((ripple >> 6) & 1) == 1:
                        f.write("Pin 13 voltage (pk-pk) (+3.3v): " + str(rpin13) + "\n")
                    if ((ripple >> 5) & 1) == 1:
                        f.write("Pin 14 voltage (pk-pk) (-12v): " + str(rpin14) + "\n")
                    if ((ripple >> 4) & 1) == 1:
                        f.write("Pin 21 voltage (pk-pk) (+5v): " + str(rpin21) + "\n")
                    if ((ripple >> 3) & 1) == 1:
                        f.write("Pin 22 voltage (pk-pk) (+5v): " + str(rpin22) + "\n")
                    if ((ripple >> 2) & 1) == 1:
                        f.write("Pin 23 voltage (pk-pk) (+5v): " + str(rpin23) + "\n")

                    if ((tests >> 0) & 1) == 1:
                        f.write("\n Voltage Test Results:\n")
                        if ((passedtests >> 0) & 1) == 1:
                            f.write("DC voltage conformed to ATX 2.0 Specifications\n")
                        else:
                            f.write("DC voltage did not conform to ATX 2.0 Specifications\n")
                        f.write("\n Recorded Voltage by Pin (Avg over 1000 samples): \n")
                        if ((volt >> 14) & 1) == 1:
                            f.write("Pin 1 voltage (+3.3v): " + str(vpin1) + "\n")
                        if ((volt >> 13) & 1) == 1:
                            f.write("Pin 2 voltage (+3.3v): " + str(vpin2) + "\n")
                        if ((volt >> 12) & 1) == 1:
                            f.write("Pin 4 voltage (+5v): " + str(vpin4) + "\n")
                        if ((volt >> 11) & 1) == 1:
                            f.write("Pin 6 voltage (+5v): " + str(vpin6) + "\n")
                        if ((volt >> 10) & 1) == 1:
                            f.write("Pin 9 voltage (+5v): " + str(vpin9) + "\n")
                        if ((volt >> 9) & 1) == 1:
                            f.write("Pin 10 voltage (+12v): " + str(vpin10) + "\n")
                        if ((volt >> 8) & 1) == 1:
                            f.write("Pin 11 voltage (+12v): " + str(vpin11) + "\n")
                        if ((volt >> 7) & 1) == 1:
                            f.write("Pin 12 voltage (+3.3v): " + str(vpin12) + "\n")
                        if ((volt >> 6) & 1) == 1:
                            f.write("Pin 13 voltage (+3.3v): " + str(vpin13) + "\n")
                        if ((volt >> 5) & 1) == 1:
                            f.write("Pin 14 voltage (-12v): " + str(vpin14) + "\n")
                        if ((volt >> 4) & 1) == 1:
                            f.write("Pin 21 voltage (+5v): " + str(vpin21) + "\n")
                        if ((volt >> 3) & 1) == 1:
                            f.write("Pin 22 voltage (+5v): " + str(vpin22) + "\n")
                        if ((volt >> 2) & 1) == 1:
                            f.write("Pin 23 voltage (+5v): " + str(vpin23) + "\n")
                f.write("\n \n End of Report\n ATX 2.0 Power Supply Tester V1.0\n Code by Patrick Clark (2025)")

        except Exception as e:
            print(f"Error saving data: {e}")
            loop = 1

        if loop == 1:
            q = 0
            while q == 0:
                temp = input("Attempt data save again?: Y/N").lower()
                if temp == 'y':
                    loop = 1
                    q = 1
                elif temp == 'n':
                    loop = 0
                    q = 1
