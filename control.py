import smbuscmds
import spicmds
def asertallrelays():
    smbuscmds.setallhigh()

def deasertallrelays():
    smbuscmds.setalllow()

def asert12vrelays():
    smbuscmds.updatepin(2,"b",3,1)#pin 4
    smbuscmds.updatepin(2,"b",4,1)#pin 5
    smbuscmds.updatepin(2,"b",5,1)#pin 6
    smbuscmds.updatepin(2,"b",6,1)#pin 7
    smbuscmds.updatepin(2,"b",7,1)# pin 8
    smbuscmds.updatepin(2, "a", 4, 1)  # pin 25
    smbuscmds.updatepin(2, "a", 5, 1)  # pin 26
    smbuscmds.updatepin(2, "a", 6, 1)  # pin 27
    smbuscmds.updatepin(2, "a", 7, 1)  # pin 28

def deasert12vrelays():
    smbuscmds.updatepin(2,"b",3,0)#pin 4
    smbuscmds.updatepin(2,"b",4,0)#pin 5
    smbuscmds.updatepin(2,"b",5,0)#pin 6
    smbuscmds.updatepin(2,"b",6,0)#pin 7
    smbuscmds.updatepin(2,"b",7,0)# pin 8
    smbuscmds.updatepin(2, "a", 4, 0)  # pin 25
    smbuscmds.updatepin(2, "a", 5, 0)  # pin 26
    smbuscmds.updatepin(2, "a", 6, 0)  # pin 27
    smbuscmds.updatepin(2, "a", 7, 0)  # pin 28

def asertb1load():
    smbuscmds.updatepin(3,"a",6,1)#pin 3-27
    smbuscmds.updatepin(3, "a", 1, 1)  # pin 3-22
    smbuscmds.updatepin(3, "a", 0, 1)  # pin 3-21
    smbuscmds.updatepin(3, "b", 5, 1)  # pin 3-6
    smbuscmds.updatepin(3, "b", 6, 1)  # pin 3-7

def deasertb1load():
    smbuscmds.updatepin(3, "a", 6, 0)  # pin 3-27
    smbuscmds.updatepin(3, "a", 1, 0)  # pin 3-22
    smbuscmds.updatepin(3, "a", 0, 0)  # pin 3-21
    smbuscmds.updatepin(3, "b", 5, 0)  # pin 3-6
    smbuscmds.updatepin(3, "b", 6, 0)  # pin 3-7

def asertb2load():
    smbuscmds.updatepin(3,"a",5,1)  # pin 3-26
def deasertb2load():
    smbuscmds.updatepin(3, "a", 5, 0)  # pin 3-26

def asertb3load():
    smbuscmds.updatepin(3, "a", 4, 1)  # pin 3-25
def deasertb3load():
    smbuscmds.updatepin(3, "a", 4, 0)  # pin 3-25

def asertb4load():
    smbuscmds.updatepin(3,"a",3,1)#pin 3-24
def deasertb4load():
    smbuscmds.updatepin(3, "a", 3, 0)  # pin 3-24

def asertb5load():
    smbuscmds.updatepin(3,"a",2,1)#pin 3-23
def deasertb5load():
    smbuscmds.updatepin(3, "a", 2, 0)  # pin 3-23

def asertb6load():
    smbuscmds.updatepin(3,"b",3,1)#pin 3-4
def deasertb6load():
    smbuscmds.updatepin(3, "b", 3, 0)  # pin 3-4

def asertb7load():
    smbuscmds.updatepin(3,"b",2,1)#pin 3-3
def deasertb7load():
    smbuscmds.updatepin(3, "b", 2, 0)  # pin 3-3

def asertb8load():
    smbuscmds.updatepin(3,"b",1,1)#pin 3-2
def deasertb8load():
    smbuscmds.updatepin(3, "b", 1, 0)  # pin 3-2

def asertb9load():
    smbuscmds.updatepin(3,"b",0,1)#pin 3-1
def deasertb9load():
    smbuscmds.updatepin(3, "b", 0, 0)  # pin 3-1

def asertb10load():
    smbuscmds.updatepin(3,"a",7,1)#pin 3-28
def deasertb10load():
    smbuscmds.updatepin(3, "a", 7, 0)  # pin 3-28

def deasertload():
    deasertb1load()
    deasertb2load()
    deasertb3load()
    deasertb4load()
    deasertb5load()
    deasertb6load()
    deasertb7load()
    deasertb8load()
    deasertb9load()
    deasertb10load()

def asertr1load():
    smbuscmds.updatepin(3,"b",6,1)#pin 3-7
def deasertr1load():
    smbuscmds.updatepin(3, "b", 6, 0)  # pin 3-7

def asertr2load():
    smbuscmds.updatepin(3,"b",7,1)#pin 3-8
def deasertr2load():
    smbuscmds.updatepin(3, "b", 7, 0)  # pin 3-8

def asertr3load():
    smbuscmds.updatepin(3,"a",0,1)#pin 3-21
def deasertr3load():
    smbuscmds.updatepin(3, "a", 0, 0)  # pin 3-21

def asertr4load():
    smbuscmds.updatepin(3,"a",1,1)#pin 3-22
def deasertr4load():
    smbuscmds.updatepin(3, "a", 1, 0)  # pin 3-22

def asertcaprelay():
    smbuscmds.updatepin(3,"b",4,1)#pin 3-5
def deasertcaprelay():
    smbuscmds.updatepin(3,"b",4,0)#pin 3-5

def asertpin1():
    smbuscmds.updatepin(1,"a",3,1)#1-24
def deasertpin1():
    smbuscmds.updatepin(1, "a", 3, 0)  # 1-24

def asertpin2():
    smbuscmds.updatepin(1,"a",2,1)#1-23
def deasertpin2():
    smbuscmds.updatepin(1, "a", 2, 0)  # 1-23

def asertpin4():
    smbuscmds.updatepin(1,"a",1,1)#1-22
def deasertpin4():
    smbuscmds.updatepin(1, "a", 1, 0)  # 1-22

def asertpin6():
    smbuscmds.updatepin(1,"a",0,1)#1-21
def deasertpin6():
    smbuscmds.updatepin(1, "a", 0, 0)  # 1-21

def asertpin9():
    smbuscmds.updatepin(1,"a",6,1)#1-27
def deasertpin9():
    smbuscmds.updatepin(1, "a", 6, 0)  # 1-27

def asertpin10():
    smbuscmds.updatepin(1,"a",4,1)#1-25
def deasertpin10():
    smbuscmds.updatepin(1, "a", 4, 0)  # 1-25

def asertpin11():
    smbuscmds.updatepin(1,"a",5,1)#1-26
def deasertpin11():
    smbuscmds.updatepin(1, "a", 5, 0)  # 1-26

def asertpin12():
    smbuscmds.updatepin(1,"b",7,1)#1-8
def deasertpin12():
    smbuscmds.updatepin(1, "b", 7, 0)  # 1-8

def asertpin13():
    smbuscmds.updatepin(1,"b",1,1) #1-2
def deasertpin13():
    smbuscmds.updatepin(1, "b", 1, 0)  # 1-2

def asertpin14():
    smbuscmds.updatepin(1,"b",2,1)#1-3
def deasertpin14():
    smbuscmds.updatepin(1, "b", 2, 0)  # 1-3

def asertpson():
    smbuscmds.updatepin(1,"b",0,1)#1-1
def deasertpson():
    smbuscmds.updatepin(1, "b", 0, 0)  # 1-1

def asertpin20():
    smbuscmds.updatepin(1,"b",3,1)#1-4
def deasertpin20():
    smbuscmds.updatepin(1, "b", 3, 0)  # 1-4

def asertpin21():
    smbuscmds.updatepin(1,"b",4,1)#1-5
def deasertpin21():
    smbuscmds.updatepin(1, "b", 4, 0)  # 1-5

def asertpin22():
    smbuscmds.updatepin(1,"b",5,1)#1-6
def deasertpin22():
    smbuscmds.updatepin(1, "b", 5, 0)  # 1-6

def asertpin23():
    smbuscmds.updatepin(1,"b",6,1)#1-7
def deasertpin23():
    smbuscmds.updatepin(1, "b", 6, 0)  # 1-7

