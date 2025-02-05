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
except ImportError:
    spidev = MockSPI()  # If it fails, use the mock

# Now your code can use 'spidev' regardless of whether the real
# library is available.