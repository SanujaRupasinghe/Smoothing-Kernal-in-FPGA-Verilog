# Smoothing Kernel in FPGA Verilog

This project utilizes the built-in accelerometer on the DE0_Nano FPGA board to implement a hardware kernel that smoothens the data stream.

[DE0_Nano FPGA Board Documentation and Resources](https://www.terasic.com.tw/cgi-bin/page/archive.pl?Language=English&CategoryNo=165&No=593&PartNo=4)  
This webpage contains the CD-ROM for the DE0_Nano FPGA board, which includes example code on how to use the built-in accelerometer of the development kit.

## Implementation Overview

In this project, the data stream from the accelerometer is re-routed to the LED panel and processed through custom modules I created:

- **UART Transmitter**
- **Averaging Filter**

## Functional Block Diagram

Below is the functional block diagram illustrating how the implementation works:
![1](https://github.com/user-attachments/assets/3a18c8dd-0f4b-4610-bc9e-aed10d03659d)



## Up to now Implementation
https://github.com/user-attachments/assets/d4921b1c-4893-4645-8cdb-a17d9c9aec0e

