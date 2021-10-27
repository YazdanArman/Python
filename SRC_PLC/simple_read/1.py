# this is the last code


from pyModbusTCP.client import ModbusClient
from time import sleep

client = ModbusClient(host = "192.168.1.240", port = 502, auto_open = True, auto_close = False, timeout = 1, debug = False)

client.open()

while (1):
    if client.is_open():
        client.write_single_coil(2088, 1)
        # client.write_single_coil(2098, 1)
        data_ = client.read_holding_registers(4100, 1)
        if data_:
            if data_[0]:
                print(data_[0])
                # print(data_, data_[0]/1000 , " sec")

                client.write_single_coil(2089, 1)
