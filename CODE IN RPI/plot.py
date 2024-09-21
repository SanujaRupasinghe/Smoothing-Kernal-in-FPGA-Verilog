import serial
import matplotlib.pyplot as plt
from collections import deque

# Configure UART
ser = serial.Serial(
    port='COM3',  # Raspberry Pi UART port
    baudrate=115200,       # Baud rate (make sure it matches the transmitter)
    timeout=1              # Timeout for read operations
)

# Open UART port
if not ser.is_open:
    ser.open()

# Variables for real-time plotting
window_size = 15000 # Number of points to display in the plot
data = deque(maxlen=window_size)

# Create a figure and axis for plotting
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)

# Set plot limits and labels
ax.set_xlim(0, window_size)
ax.set_ylim(-128, 127)  # 8-bit 2's complement range
ax.set_xlabel('Sample Number')
ax.set_ylabel('Received Byte Value')
ax.set_title('Real-Time UART Data Plot')

def decode_twos_complement(byte_value):
    """Decode 8-bit 2's complement value."""
    if byte_value & 0x80:  # Check if sign bit is set
        return byte_value - 256  # Convert to negative value
    return byte_value

def update_plot():
    xdata = list(range(len(data)))
    ydata = list(data)
    line.set_data(xdata, ydata)
    ax.set_xlim(0, len(data))
    ax.relim()
    ax.autoscale_view()
    plt.draw()
    plt.pause(0.01)  # Pause to allow the plot to update

try:
    count = 0
    while True:
        # Read a byte from UART
        byte = ser.read(1)
        
        if byte:
            received_byte = int.from_bytes(byte, byteorder='big')
            decoded_value = decode_twos_complement(received_byte)
            data.append(decoded_value)
            count += 1
            
            # Update the plot every 6400 samples
            if count % 15000 == 0:
                update_plot()

finally:
    # Close UART port
    ser.close()
    plt.close(fig)
