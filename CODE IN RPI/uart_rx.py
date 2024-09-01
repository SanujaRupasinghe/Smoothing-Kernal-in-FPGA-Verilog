import serial

# Configure UART
ser = serial.Serial(
    port='/dev/serial0',  # Raspberry Pi UART port
    baudrate=115200,       # Baud rate (make sure it matches the transmitter)
    timeout=1              # Timeout for read operations
)

# Open UART port
if not ser.is_open:
    ser.open()

# x = 0
count = 0
try:
    while True:
        # Read a byte from UART
        byte = ser.read(1)
        
        if byte:
            count += 1
            # Convert byte to integer
            received_byte = int.from_bytes(byte, byteorder='big')
            # Print the byte in binary format with leading zeros
            print(f"Received byte: {received_byte:08b} and received byte number is {count}")


finally:
    # Close UART port
    ser.close()
