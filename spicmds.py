import time
import math


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


spi.open(0, 0)  #bus 0 chip select 0
spi.max_speed_hz = 1000000 # 1 MHz
spi.mode = 0b00          # Mode 0,0

#channel read ftn
def readadc(channel):
    if channel < 0 or channel > 7:
        raise ValueError("Channel must be a value 0-7")
    command = 0b10000000 | (channel << 4)  #makes cmd byte
    transfer_command = [0x01, command, 0x00]
    data = spi.xfer2(transfer_command)
    value = ((data[1] & 3) << 8) + data[2]  #first byte null, byte two msb byte 3 lsb
    return value


def readi2():
    val = readadc(0)
    adc = 5 / 1023
    conv = 1 / .04  #a/v
    val = val * adc
    val = conv * val
    return val


def readv2():
    val = readadc(1)
    adc = 5 / 1023
    conv = 1 / .32806
    val = val * adc
    val = val * conv
    return val


def readv3():
    val = readadc(2)
    adc = 5 / 1023
    conv = 1 / .328458
    val = val * adc
    val = val * conv
    return val


def readpsok():
    val = readadc(3)
    adc = 5 / 1023
    val = val * adc
    return val


def readv1():
    adc = 5 / 1023
    conv = 1 / .032
    mean = 0
    for i in range(1000):
        val = readadc(4)
        val = val * adc
        val = val * conv
        val = val * val
        mean += val
    mean /= 1000
    mean = math.sqrt(mean)
    return mean


def readi1():
    conv = 1 / .04167  #a/v
    adc = 5 / 1023
    mean = 0
    for i in range(1000):
        val = readadc(5)
        val = val * adc
        val = val * conv
        val = val * val
        mean += val
    mean /= 1000
    mean = math.sqrt(mean)
    return mean
