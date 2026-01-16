import serial
import time
import threading
import json
import sys

# ==========================================
# 🐧 LINUX PORTS CONFIGURATION
# ==========================================
PORTS = ['/dev/ttyUSB0', '/dev/ttyUSB1', '/dev/ttyUSB2']
BAUD = 115200
# ==========================================

def read_node(port_name):
    """
    Connects to a specific USB port and prints its data.
    """
    try:
        # Connect to Serial Port
        ser = serial.Serial(port_name, BAUD, timeout=1)
        print(f"✅ Connected to {port_name}")
        
        while True:
            try:
                if ser.in_waiting > 0:
                    # Read line, decode, and strip whitespace
                    line = ser.readline().decode('utf-8', errors='ignore').strip()
                    
                    # Parse JSON
                    if line.startswith('{') and line.endswith('}'):
                        try:
                            data = json.loads(line)
                            node_id = data.get('id', '?')
                            dist = data.get('dist', 0)
                            risk = data.get('risk', 0)
                            
                            # Print formatted output
                            print(f"[{port_name}] NODE {node_id}: Dist={dist}cm | Risk={risk}")
                        except json.JSONDecodeError:
                            pass # Ignore half-broken packets
            except OSError:
                print(f"❌ Device disconnected: {port_name}")
                break
                
    except serial.SerialException as e:
        print(f"❌ Could not open {port_name}: Permission denied or busy.")
        print("   Try running: sudo chmod 666 /dev/ttyUSB*")

# --- MAIN EXECUTION ---
print("-----------------------------------------")
print("   CROWDSENSE NETWORK LISTENER (LINUX)   ")
print("-----------------------------------------")

# Start a listener thread for each port
threads = []
for port in PORTS:
    t = threading.Thread(target=read_node, args=(port,))
    t.daemon = True # Kills thread when main program exits
    t.start()
    threads.append(t)

# Keep main program running
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\n🛑 Stopping Network...")
    sys.exit()