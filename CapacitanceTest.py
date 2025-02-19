import control
import spicmds
import time

def capacitancetest():
    control.deasertallrelays()
    control.asertcaprelay()
    control.asert12vrelays()
    control.asertpson()
    time.sleep(5)
    psok = spicmds.readpsok()
    control.deasertpson()
    control.deasert12vrelays()
    control.deasertcaprelay()
    if psok == 5:#needs ajusted acording to tested values
        return 1
    else:
        return 0