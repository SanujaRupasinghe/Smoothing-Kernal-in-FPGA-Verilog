import serial
import matplotlib.pyplot as plt
from collections import deque


ser = serial.Serial(
    port='COM3',  
    baudrate=115200,  
    timeout=1  # Timeout for read operations
)


if not ser.is_open:
    ser.open()


window_size = 11520  # Number of samples to display in the plot
data = deque(maxlen=window_size)  # Use deque for dynamic buffer management

# Create a figure and axis for plotting
fig, ax = plt.subplots()

# Set plot limits and labels
ax.set_xlim(0, window_size)
ax.set_ylim(-128, 127)  # 8-bit 2's complement range
ax.set_xlabel('Sample Number')
ax.set_ylabel('Received Byte Value')
ax.set_title('Real-Time UART Data Plot (Stem)')

def decode_twos_complement(byte_value):
    """Decode 8-bit 2's complement value."""
    if byte_value & 0x80:  # Check if sign bit is set
        return byte_value - 256  # Convert to negative value for 2's complement
    return byte_value

def update_plot():
    """Update the real-time plot as a stem plot."""
    ax.clear()  # Clear the previous plot
    xdata = list(range(len(data)))  # X-axis data (sample numbers)
    ydata = list(data)  # Y-axis data (received values)
    
    # Plot the stem graph
    ax.stem(xdata, ydata, basefmt=" ")  # Use stem plot without 'use_line_collection'
    
    # Adjust plot settings
    ax.set_xlim(0, len(data))  # Adjust X-axis limits
    ax.set_ylim(-128, 127)  # Keep Y-axis within 8-bit 2's complement range
    ax.set_xlabel('Sample Number')
    ax.set_ylabel('Received Byte Value')
    ax.set_title('Real-Time UART Data Plot (Stem)')
    
    # Redraw the plot
    plt.tight_layout()
    plt.pause(0.01)  # Pause to allow the plot to refresh

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
            
            # Update the plot every 15000 samples
            if count % window_size == 0:
                update_plot()

finally:
    # Close UART port and figure when done
    ser.close()
    plt.close(fig)
