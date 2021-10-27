from pyModbusTCP.client import ModbusClient
from time import sleep

client = ModbusClient(host = "192.168.1.240", port = 502, auto_open = True, auto_close = False, timeout = 1, debug = False)

client.open()
f = open("demofile.txt", "w")

while (1):
    if client.is_open():
        client.write_single_coil(2088, 1)

        data = client.read_holding_registers(4100, 1)
        
        if data:
            if data[0]:
                print(data)
                f.write((str(data[0]) + "\n"))

                client.write_single_coil(2089, 1)

f.close()
