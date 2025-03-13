import os

def compilereport(passedtests, tests, load, eff, volt, ripple, wattage, date, user, serial, fullvout, medvout, lowvout, fullvin, medvin, lowvin, fullcout, medcout, lowcout, fullcin, medcin, lowcin, fulload, medload, lowload, rpin1, rpin2, rpin4, rpin6, rpin9, rpin10,  rpin11, rpin12, rpin13, rpin14, rpin21, rpin22, rpin23, vpin1, vpin2, vpin4, vpin6, vpin9, vpin10,  vpin11, vpin12, vpin13, vpin14, vpin21, vpin22, vpin23):
    mountpnt = "/media/pi/"
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
                elif (((passedtests >> 3) & 1) == 1) & ((tests >> 4) & 1) == 1:
                    f.write("Efficiency Test: Pass\n")
                if (((passedtests >> 2) & 1) == 0) & ((tests >> 2) & 1) == 1:
                    f.write("Load Test: Fail\n")
                elif (((passedtests >> 2) & 1) == 1) & ((tests >> 4) & 1) == 1:
                    f.write("Load Test: Pass\n")
                if (((passedtests >> 1) & 1) == 0) & ((tests >> 1) & 1) == 1:
                    f.write("Ripple Test: Fail\n")
                elif (((passedtests >> 1) & 1) == 1) & ((tests >> 4) & 1) == 1:
                    f.write("Ripple Test: Pass\n")
                if (((passedtests >> 0) & 1) == 0) & ((tests >> 0) & 1) == 1:
                    f.write("Voltage Test: Fail\n")
                elif (((passedtests >> 0) & 1) == 1) & ((tests >> 4) & 1) == 1:
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
