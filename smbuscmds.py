import time
RETRY_DELAY = 0.05
MAX_RETRIES = 3
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
IO_O2 = 0x24
IO_O3 = 0x23


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
# Init IO_O1, IODIRA
retries = 0
while retries < MAX_RETRIES:
    try:
        bus.write_byte_data(IO_O1, IODIRA, 0x00) #0x00 = all output
        break # Success
    except (IOError, OSError) as e:
        print(f"I2C Error Initializing IO_O1 Port A Direction: {e}")
        retries += 1
        if retries < MAX_RETRIES:
            print(f"Retrying ({retries}/{MAX_RETRIES})...")
            time.sleep(RETRY_DELAY)
        else:
            print(f"FAILED Init IO_O1 Port A Direction after {MAX_RETRIES} retries.")

# Init IO_O2, IODIRA
retries = 0
while retries < MAX_RETRIES:
    try:
        bus.write_byte_data(IO_O2, IODIRA, 0x00)
        break # Success
    except (IOError, OSError) as e:
        print(f"I2C Error Initializing IO_O2 Port A Direction: {e}")
        retries += 1
        if retries < MAX_RETRIES:
            print(f"Retrying ({retries}/{MAX_RETRIES})...")
            time.sleep(RETRY_DELAY)
        else:
            print(f"FAILED Init IO_O2 Port A Direction after {MAX_RETRIES} retries.")

# Init IO_O3, IODIRA
retries = 0
while retries < MAX_RETRIES:
    try:
        bus.write_byte_data(IO_O3, IODIRA, 0x00)
        break # Success
    except (IOError, OSError) as e:
        print(f"I2C Error Initializing IO_O3 Port A Direction: {e}")
        retries += 1
        if retries < MAX_RETRIES:
            print(f"Retrying ({retries}/{MAX_RETRIES})...")
            time.sleep(RETRY_DELAY)
        else:
            print(f"FAILED Init IO_O3 Port A Direction after {MAX_RETRIES} retries.")

# Init IO_O1, IODIRB
retries = 0
while retries < MAX_RETRIES:
    try:
        bus.write_byte_data(IO_O1, IODIRB, 0x00)
        break # Success
    except (IOError, OSError) as e:
        print(f"I2C Error Initializing IO_O1 Port B Direction: {e}")
        retries += 1
        if retries < MAX_RETRIES:
            print(f"Retrying ({retries}/{MAX_RETRIES})...")
            time.sleep(RETRY_DELAY)
        else:
            print(f"FAILED Init IO_O1 Port B Direction after {MAX_RETRIES} retries.")

# Init IO_O2, IODIRB
retries = 0
while retries < MAX_RETRIES:
    try:
        bus.write_byte_data(IO_O2, IODIRB, 0x00)
        break # Success
    except (IOError, OSError) as e:
        print(f"I2C Error Initializing IO_O2 Port B Direction: {e}")
        retries += 1
        if retries < MAX_RETRIES:
            print(f"Retrying ({retries}/{MAX_RETRIES})...")
            time.sleep(RETRY_DELAY)
        else:
            print(f"FAILED Init IO_O2 Port B Direction after {MAX_RETRIES} retries.")

# Init IO_O3, IODIRB
retries = 0
while retries < MAX_RETRIES:
    try:
        bus.write_byte_data(IO_O3, IODIRB, 0x00)
        break # Success
    except (IOError, OSError) as e:
        print(f"I2C Error Initializing IO_O3 Port B Direction: {e}")
        retries += 1
        if retries < MAX_RETRIES:
            print(f"Retrying ({retries}/{MAX_RETRIES})...")
            time.sleep(RETRY_DELAY)
        else:
            print(f"FAILED Init IO_O3 Port B Direction after {MAX_RETRIES} retries.")

def updatepin(board, letter, pin, value):
    # --- Map board number to I2C address ---
    target_board_addr = None
    if board == 1:
        target_board_addr = IO_O1
    if board == 2:
        target_board_addr = IO_O2
    if board == 3:
        target_board_addr = IO_O3

    # --- Map letter to Register address ---
    target_reg_addr = None
    if letter == "a":
        target_reg_addr = OLATA
    if letter == "b":
        target_reg_addr = OLATB

    if target_board_addr is None or target_reg_addr is None:
        print(f"Error: Invalid board ({board}) or letter ({letter}) provided.")
        return

    # --- Perform Read with Retries ---
    current_olat = None
    read_success = False
    retries = 0
    while retries < MAX_RETRIES:
        try:
            current_olat = bus.read_byte_data(target_board_addr, target_reg_addr)
            read_success = True
            break # Exit retry loop on successful read
        except (IOError, OSError) as e:
            print(f"I2C Read Error on Addr={hex(target_board_addr)}, Reg={hex(target_reg_addr)}: {e}")
            retries += 1
            if retries < MAX_RETRIES:
                print(f"Retrying read ({retries}/{MAX_RETRIES})...")
                time.sleep(RETRY_DELAY)
            else:
                print(f"FAILED Read Addr={hex(target_board_addr)}, Reg={hex(target_reg_addr)} after {MAX_RETRIES} retries.")
                return # Cannot proceed without successful read

    if not read_success:
        # This case should ideally be covered by the return in the loop's else block,
        # but included for explicit safety.
        print("Read operation ultimately failed. Aborting updatepin.")
        return
  # --- Calculate new value ---
    new_olat = current_olat
    if value == 1:
        new_olat = current_olat | (1 << pin)
    elif value == 0:
        new_olat = current_olat & ~(1 << pin)
    # No handling if value is not 0 or 1

    # --- Perform Write with Retries (only if value changed) ---
    if new_olat != current_olat:
        write_success = False
        retries = 0
        while retries < MAX_RETRIES:
            try:
                bus.write_byte_data(target_board_addr, target_reg_addr, new_olat)
                write_success = True
                break # Exit retry loop on successful write
            except (IOError, OSError) as e:
                print(f"I2C Write Error on Addr={hex(target_board_addr)}, Reg={hex(target_reg_addr)}, Val={hex(new_olat)}: {e}")
                retries += 1
                if retries < MAX_RETRIES:
                    print(f"Retrying write ({retries}/{MAX_RETRIES})...")
                    time.sleep(RETRY_DELAY)
                else:
                    print(f"FAILED Write Addr={hex(target_board_addr)}, Reg={hex(target_reg_addr)}, Val={hex(new_olat)} after {MAX_RETRIES} retries.")
        # Note: The function currently doesn't explicitly report final write failure


def setallhigh():
    print("Setting all outputs HIGH with retries...")
    # Write IO_O1, OLATA
    retries = 0
    while retries < MAX_RETRIES:
         try:
             bus.write_byte_data(IO_O1, OLATA, 0xFF)
             break # Success
         except (IOError, OSError) as e:
             print(f"I2C Error setting high IO_O1 OLATA: {e}")
             retries += 1
             if retries < MAX_RETRIES:
                 print(f"Retrying ({retries}/{MAX_RETRIES})...")
                 time.sleep(RETRY_DELAY)
             else:
                 print(f"FAILED setting high IO_O1 OLATA after {MAX_RETRIES} retries.")

    # Write IO_O2, OLATA
    retries = 0
    while retries < MAX_RETRIES:
         try:
             bus.write_byte_data(IO_O2, OLATA, 0xFF)
             break # Success
         except (IOError, OSError) as e:
             print(f"I2C Error setting high IO_O2 OLATA: {e}")
             retries += 1
             if retries < MAX_RETRIES:
                 print(f"Retrying ({retries}/{MAX_RETRIES})...")
                 time.sleep(RETRY_DELAY)
             else:
                 print(f"FAILED setting high IO_O2 OLATA after {MAX_RETRIES} retries.")

    # Write IO_O3, OLATA
    retries = 0
    while retries < MAX_RETRIES:
         try:
             bus.write_byte_data(IO_O3, OLATA, 0xFF)
             break # Success
         except (IOError, OSError) as e:
             print(f"I2C Error setting high IO_O3 OLATA: {e}")
             retries += 1
             if retries < MAX_RETRIES:
                 print(f"Retrying ({retries}/{MAX_RETRIES})...")
                 time.sleep(RETRY_DELAY)
             else:
                 print(f"FAILED setting high IO_O3 OLATA after {MAX_RETRIES} retries.")

    # Write IO_O1, OLATB
    retries = 0
    while retries < MAX_RETRIES:
         try:
             bus.write_byte_data(IO_O1, OLATB, 0xFF)
             break # Success
         except (IOError, OSError) as e:
             print(f"I2C Error setting high IO_O1 OLATB: {e}")
             retries += 1
             if retries < MAX_RETRIES:
                 print(f"Retrying ({retries}/{MAX_RETRIES})...")
                 time.sleep(RETRY_DELAY)
             else:
                 print(f"FAILED setting high IO_O1 OLATB after {MAX_RETRIES} retries.")

    # Write IO_O2, OLATB
    retries = 0
    while retries < MAX_RETRIES:
         try:
             bus.write_byte_data(IO_O2, OLATB, 0xFF)
             break # Success
         except (IOError, OSError) as e:
             print(f"I2C Error setting high IO_O2 OLATB: {e}")
             retries += 1
             if retries < MAX_RETRIES:
                 print(f"Retrying ({retries}/{MAX_RETRIES})...")
                 time.sleep(RETRY_DELAY)
             else:
                 print(f"FAILED setting high IO_O2 OLATB after {MAX_RETRIES} retries.")

    # Write IO_O3, OLATB
    retries = 0
    while retries < MAX_RETRIES:
         try:
             bus.write_byte_data(IO_O3, OLATB, 0xFF)
             break # Success
         except (IOError, OSError) as e:
             print(f"I2C Error setting high IO_O3 OLATB: {e}")
             retries += 1
             if retries < MAX_RETRIES:
                 print(f"Retrying ({retries}/{MAX_RETRIES})...")
                 time.sleep(RETRY_DELAY)
             else:
                 print(f"FAILED setting high IO_O3 OLATB after {MAX_RETRIES} retries.")


def setalllow():
    print("Setting all outputs LOW with retries...")
    # Write IO_O1, OLATA
    retries = 0
    while retries < MAX_RETRIES:
         try:
             bus.write_byte_data(IO_O1, OLATA, 0x00)
             break # Success
         except (IOError, OSError) as e:
             print(f"I2C Error setting low IO_O1 OLATA: {e}")
             retries += 1
             if retries < MAX_RETRIES:
                 print(f"Retrying ({retries}/{MAX_RETRIES})...")
                 time.sleep(RETRY_DELAY)
             else:
                 print(f"FAILED setting low IO_O1 OLATA after {MAX_RETRIES} retries.")

    # Write IO_O2, OLATA
    retries = 0
    while retries < MAX_RETRIES:
         try:
             bus.write_byte_data(IO_O2, OLATA, 0x00)
             break # Success
         except (IOError, OSError) as e:
             print(f"I2C Error setting low IO_O2 OLATA: {e}")
             retries += 1
             if retries < MAX_RETRIES:
                 print(f"Retrying ({retries}/{MAX_RETRIES})...")
                 time.sleep(RETRY_DELAY)
             else:
                 print(f"FAILED setting low IO_O2 OLATA after {MAX_RETRIES} retries.")

    # Write IO_O3, OLATA
    retries = 0
    while retries < MAX_RETRIES:
         try:
             bus.write_byte_data(IO_O3, OLATA, 0x00)
             break # Success
         except (IOError, OSError) as e:
             print(f"I2C Error setting low IO_O3 OLATA: {e}")
             retries += 1
             if retries < MAX_RETRIES:
                 print(f"Retrying ({retries}/{MAX_RETRIES})...")
                 time.sleep(RETRY_DELAY)
             else:
                 print(f"FAILED setting low IO_O3 OLATA after {MAX_RETRIES} retries.")

    # Write IO_O1, OLATB
    retries = 0
    while retries < MAX_RETRIES:
         try:
             bus.write_byte_data(IO_O1, OLATB, 0x00)
             break # Success
         except (IOError, OSError) as e:
             print(f"I2C Error setting low IO_O1 OLATB: {e}")
             retries += 1
             if retries < MAX_RETRIES:
                 print(f"Retrying ({retries}/{MAX_RETRIES})...")
                 time.sleep(RETRY_DELAY)
             else:
                 print(f"FAILED setting low IO_O1 OLATB after {MAX_RETRIES} retries.")

    # Write IO_O2, OLATB
    retries = 0
    while retries < MAX_RETRIES:
         try:
             bus.write_byte_data(IO_O2, OLATB, 0x00)
             break # Success
         except (IOError, OSError) as e:
             print(f"I2C Error setting low IO_O2 OLATB: {e}")
             retries += 1
             if retries < MAX_RETRIES:
                 print(f"Retrying ({retries}/{MAX_RETRIES})...")
                 time.sleep(RETRY_DELAY)
             else:
                 print(f"FAILED setting low IO_O2 OLATB after {MAX_RETRIES} retries.")

    # Write IO_O3, OLATB
    retries = 0
    while retries < MAX_RETRIES:
         try:
             bus.write_byte_data(IO_O3, OLATB, 0x00)
             break # Success
         except (IOError, OSError) as e:
             print(f"I2C Error setting low IO_O3 OLATB: {e}")
             retries += 1
             if retries < MAX_RETRIES:
                 print(f"Retrying ({retries}/{MAX_RETRIES})...")
                 time.sleep(RETRY_DELAY)
             else:
                 print(f"FAILED setting low IO_O3 OLATB after {MAX_RETRIES} retries.")