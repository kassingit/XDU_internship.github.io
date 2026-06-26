#!/usr/bin/env python3
import serial
import time
import struct

def test_serial_communication():
    # Try both USB ports
    ports = ['/dev/ttyUSB0', '/dev/ttyUSB1']
    
    for port in ports:
        print(f"\n{'='*50}")
        print(f"Testing port: {port}")
        print(f"{'='*50}")
        
        try:
            # Open serial port
            ser = serial.Serial(
                port=port,
                baudrate=115200,
                timeout=1,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                bytesize=serial.EIGHTBITS
            )
            
            print(f"✓ Successfully opened {port}")
            print(f"  - Port: {ser.name}")
            print(f"  - Baudrate: {ser.baudrate}")
            print(f"  - Is open: {ser.is_open}")
            
            # Flush buffers
            ser.flushInput()
            ser.flushOutput()
            
            # Try to read any data
            print("\nReading any available data...")
            time.sleep(0.5)
            data = ser.read(100)
            if data:
                print(f"  Received {len(data)} bytes: {data.hex()}")
            else:
                print("  No data received")
            
            # Try to send a simple command (query firmware version or ping)
            # Common STM32 command format: header + command + length + data + checksum
            print("\nSending test command...")
            
            # Try sending a simple ping command (0x01 is commonly used)
            # Format: 0x55 0xAA (header) + command + checksum
            test_cmd = bytes([0x55, 0xAA, 0x01, 0x01])
            ser.write(test_cmd)
            print(f"  Sent: {test_cmd.hex()}")
            
            # Wait for response
            time.sleep(0.5)
            response = ser.read(50)
            if response:
                print(f"  Received response: {response.hex()}")
                print(f"  Response length: {len(response)} bytes")
            else:
                print("  No response received")
            
            # Close the port
            ser.close()
            print(f"\n✓ Port {port} test completed")
            
        except Exception as e:
            print(f"✗ Error with {port}: {e}")
    
    print(f"\n{'='*50}")
    print("Test completed!")

if __name__ == "__main__":
    print("STM32 Communication Test")
    print("="*50)
    test_serial_communication()