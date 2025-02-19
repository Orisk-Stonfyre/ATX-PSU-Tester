import time
class MockSPI:
    """
    A mock class for spidev or other SPI libraries.  This allows you to run and test
    code on a system that doesn't have access to the SPI bus (like Windows).
    """

    def __init__(self, bus=None, device=None):  # bus and device are optional
        print("Mock SPI initialized (no real hardware access)")
        self.bus = bus
        self.device = device

    def open(self, bus, device):
      print(f"Mock open: Bus: {bus}, Device: {device}")
      self.bus = bus
      self.device = device
      return None

    def close(self):
      print("Mock close")
      return None

    def xfer(self, data):
        print(f"Mock xfer: Data: {data}")
        # Simulate SPI transfer. Return dummy data.
        if isinstance(data, list):
            return [0] * len(data)  # Return a list of zeros
        elif isinstance(data, bytes) or isinstance(data, bytearray):
            return bytes([0] * len(data))  # Return a bytes object of zeros
        else:
            return 0  # Return a single zero if data is a single value

    def xfer2(self, data):  # Often the same as xfer, but included for completeness
        print(f"Mock xfer2: Data: {data}")
        if isinstance(data, list):
            return [0] * len(data)  # Return a list of zeros
        elif isinstance(data, bytes) or isinstance(data, bytearray):
            return bytes([0] * len(data))  # Return a bytes object of zeros
        else:
            return 0  # Return a single zero if data is a single value

    def writebytes(self, data):
        print(f"Mock writebytes: Data: {data}")

    def readbytes(self, length):
        print(f"Mock readbytes: Length: {length}")
        return bytes([0] * length)  # Return a bytes object of zeros

    # Add other methods from your SPI library as needed...


# How to use it (example using spidev):
try:
    import spidev  # Try importing the real library first
    spi = spidev.SpiDev()
except ImportError:
    spidev = MockSPI()  # If it fails, use the mock
    spi = spidev
# Now your code can use 'spidev' regardless of whether the real
# library is available.


spi.open(0, 0) #bus 0 chip select 0

#channel read ftn
def readadc(channel):
    if channel <0 or channel >7:
        raise ValueError("Channel must be a value 0-7")
    command = 0b10000000 | (channel << 4) #makes cmd byte
    spi.xfer2([0x01,command,0x00]) #sends command
    data = spi.readbytes(3)  #reads data
    value = ((data[1] & 3) << 8) + data[2] #first byte null, byte two msb byte 3 lsb
    return value

def readi2():
    return readadc(0)

def readv2():
    return readadc(1)

def readv3():
    return readadc(2)

def readpsok():
    return readadc(3)

def readv1():
    return readadc(4)

def readi1():
    return readadc(5)