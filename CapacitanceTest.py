import control
import spicmds
import time

def capacitancetest():
    control.deasertallrelays()
    print("Aserting Capacitor")
    control.asertcaprelay()
    print("Aserting 12v Relays")
    control.asert12vrelays()
    print("Power Aserted")
    control.asertpson()
    print("Power Stabilizing")
    time.sleep(5)
    print("Reading Power Okay")
    psok = spicmds.readpsok()
    print("Power Down")
    control.deasertpson()
    print("Power Deaserting all Relays")
    control.deasert12vrelays()
    control.deasertcaprelay()
    if psok == 5:#needs ajusted acording to tested values
        print("Capacitance Test Complete, Value Nominal")
        return 1
    else:
        print("Capacitance Test Failed")
        return 0