import time

class MockSMBus:
    """
    A mock class for smbus or smbus2.  This allows you to run and test
    code on a system that doesn't have access to the I2C bus (like Windows).
    """

    def __init__(self, bus=None):  # bus parameter is optional for mock
        print("Mock SMBus initialized (no real hardware access)")
        self.bus = bus  # Store the bus number if provided (for compatibility)

    def read_byte(self, address, command=None):
        print(f"Mock read_byte: Address: {address}, Command: {command}")
        return 0  # Return a dummy value (replace with your desired mock value)

    def write_byte(self, address, value):
        print(f"Mock write_byte: Address: {address}, Value: {value}")

    def read_byte_data(self, address, command):
        print(f"Mock read_byte_data: Address: {address}, Command: {command}")
        return 0  # Return a dummy value

    def write_byte_data(self, address, command, data):
        print(f"Mock write_byte_data: Address: {address}, Command: {command}, Data: {data}")

    def read_word_data(self, address, command):
        print(f"Mock read_word_data: Address: {address}, Command: {command}")
        return 0  # Dummy value

    def write_word_data(self, address, command, data):
        print(f"Mock write_word_data: Address: {address}, Command: {command}, Data: {data}")

    def read_i2c_block_data(self, address, command, length):
        print(f"Mock read_i2c_block_data: Address: {address}, Command: {command}, Length: {length}")
        return [0] * length  # Dummy list of zeros

    def write_i2c_block_data(self, address, command, data):
        print(f"Mock write_i2c_block_data: Address: {address}, Command: {command}, Data: {data}")

    # Add other methods from smbus/smbus2 as needed...
    def open(self, bus):
      print(f"Mock open: Bus: {bus}")

    def close(self):
      print("Mock Close")


# How to use it:
try:
    import smbus2 as smbus  # Try importing the real library first
    bus = smbus.SMBus(1)
except ImportError:
    smbus = MockSMBus()  # If it fails, use the mock
    bus = smbus

# Now your code can use 'smbus' regardless of whether the real
# library is available.  If you're on Windows (or any system
# where smbus2 isn't installed), the mock version will be used.


#o1 adress 110 0x26
#O2 adress 101 0x25
#O3 adress 001 0x21
IO_O1 = 0x26
IO_O2 = 0x25
IO_O3 = 0x21


#common io adresses
IODIRA: int = 0x00  # Input/Output Direction Register A
IODIRB = 0x01  # Input/Output Direction Register B
GPPUA = 0x0C  # Pull-Up Resistor Register A
GPPUB = 0x0D  # Pull-Up Resistor Register B
GPIOA = 0x12  # GPIO Register A
GPIOB = 0x13  # GPIO Register B
OLATA = 0x14  # Output Latch Register A
OLATB = 0x15  # Output Latch Register B

#start bus on i2c bus one


  #  set all ports to output for each io board
bus.write_byte_data(IO_O1, IODIRA, 0x00) #0x00 = all output
bus.write_byte_data(IO_O2, IODIRA, 0x00)
bus.write_byte_data(IO_O3, IODIRA, 0x00)
bus.write_byte_data(IO_O1, IODIRB, 0x00)
bus.write_byte_data(IO_O2, IODIRB, 0x00)
bus.write_byte_data(IO_O3, IODIRB, 0x00)

def updatepin(board, letter, pin, value):
    if board == 1:
        board = IO_O1
    if board == 2:
        board = IO_O2
    if board == 3:
        board = IO_O3
    if letter == "a":
        letter = OLATA
    if letter == "b":
        letter = OLATB
    if value == 1:
        current_olat = bus.read_byte_data(board, letter)
        new_olat = current_olat | (1 << pin)
        bus.write_byte_data(board, letter, new_olat)
    if value == 0:
        current_olat = bus.read_byte_data(board, letter)
        new_olat = current_olat & ~(1 << pin)
        bus.write_byte_data(board, letter, new_olat)

def setallhigh():
    bus.write_byte_data(IO_O1, IODIRA, 0xFF)
    bus.write_byte_data(IO_O2, IODIRA, 0xFF)
    bus.write_byte_data(IO_O3, IODIRA, 0xFF)
    bus.write_byte_data(IO_O1, IODIRB, 0xFF)
    bus.write_byte_data(IO_O2, IODIRB, 0xFF)
    bus.write_byte_data(IO_O3, IODIRB, 0xFF)

def setalllow():
    bus.write_byte_data(IO_O1, IODIRA, 0x00)
    bus.write_byte_data(IO_O2, IODIRA, 0x00)
    bus.write_byte_data(IO_O3, IODIRA, 0x00)
    bus.write_byte_data(IO_O1, IODIRB, 0x00)
    bus.write_byte_data(IO_O2, IODIRB, 0x00)
    bus.write_byte_data(IO_O3, IODIRB, 0x00)