# this is the last code

from pyModbusTCP.client import ModbusClient
from time import sleep

client = ModbusClient(host = "192.168.1.240", port = 502, auto_open = True, auto_close = True, timeout = 2.2, debug = False)


def input_number_to_modbus_address(input_name_number):
    main_offset = 1024
    return main_offset + int(str(input_name_number), base = 8)


while(1):
    state = client.read_discrete_inputs(input_number_to_modbus_address(53), 1)
    print(state)
