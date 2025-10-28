import serial
import time

SERIAL_PORT = '/dev/ttyACM0'
BAUD_RATE = 115200

try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    print(f"Connected to {SERIAL_PORT} at {BAUD_RATE} baud.")
    
    while True:
        try:
            line = ser.readline().decode('utf-8').strip()
            if line:
                print(line)
        except UnicodeDecodeError:
            # Ignore frames that are not valid utf-8
            pass
        time.sleep(0.01)

except serial.SerialException as e:
    print(f"Error: {e}")
except KeyboardInterrupt:
    print("\nExiting...")
finally:
    if 'ser' in locals() and ser.is_open:
        ser.close()
        print("Serial port closed.")
