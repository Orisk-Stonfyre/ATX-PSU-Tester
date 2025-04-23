#import spi and i2c controllers
import time
import smbuscmds
import spicmds
#init spi and i2c


def init():

    #msg about waiting for init to complete before connecting psu
    print("Please Wait to Connect PSU Until Calibration Completes")

    # assert relays needed to meaure ground for refrence
    smbuscmds.setallhigh() #assert all high


    #read and save gnd reference values
    refi2 = spicmds.readi2()
    refv2 = spicmds.readv2()
    refv3 = spicmds.readv3()
    refpsok = spicmds.readpsok()


    #deasert all relays
    smbuscmds.setalllow() #deasserts all relays

    #display connection msg
    print("Calibration Complete, Please connect PSU and Press Enter")
    input()