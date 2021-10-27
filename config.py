from pyModbusTCP.client import ModbusClient
from pyModbusTCP import utils
from time import sleep

client = ModbusClient(host = "192.168.1.238", port = 502, auto_open = True, auto_close = True, timeout = 0.1, debug = False)

client.unit_id(13)

ModbusTCP_ADRESS_config_change_flag = 10

ModbusTCP_ADRESS_IP_1st_Byte = 1
ModbusTCP_ADRESS_IP_2nd_Byte = 2
ModbusTCP_ADRESS_IP_3rd_Byte = 3
ModbusTCP_ADRESS_IP_4th_Byte = 4
ModbusTCP_ADRESS_MAC_1st_Byte = 5
ModbusTCP_ADRESS_MAC_2nd_Byte = 6
ModbusTCP_ADRESS_MAC_3rd_Byte = 7
ModbusTCP_ADRESS_MAC_4th_Byte = 8
ModbusTCP_ADRESS_MAC_5th_Byte = 9
ModbusTCP_ADRESS_MAC_6th_Byte = 10
ModbusTCP_ADRESS_RS485_serial_baud_rate = 11;
ModbusTCP_ADRESS_RS485_serial_setting = 12;
ModbusTCP_ADRESS_num_of_sensor_per_station = 13;
ModbusTCP_ADRESS_station_address = 14;
ModbusTCP_ADRESS_PLC_offset = 15;
ModbusTCP_ADRESS_onboard_inputs_data_type = 16;

# baud_list   = [300,          #0
#                1200,         #1
#                2400,         #2
#                4800,         #3
#                9600,         #4
#                19200,        #5
#                38400,        #6
#                57600,        #7
#                74880,        #8
#                115200,       #9
#                230400        #10
#                ];
#
# serial_config_list   = [SERIAL_8N1,           #0
#                         SERIAL_8N2,           #1
#                         SERIAL_9N1,           #2
#                         SERIAL_9N2,           #3
#                         SERIAL_8E1,           #4
#                         SERIAL_8E2,           #5
#                         SERIAL_8O1,           #6
#                         SERIAL_8O2            #7
#                        ];



client.write_single_register(ModbusTCP_ADRESS_IP_1st_Byte, 192)
client.write_single_register(ModbusTCP_ADRESS_IP_2nd_Byte, 168)
client.write_single_register(ModbusTCP_ADRESS_IP_3rd_Byte, 1)
client.write_single_register(ModbusTCP_ADRESS_IP_4th_Byte, 238)

client.write_single_register(ModbusTCP_ADRESS_MAC_1st_Byte, int("0x80", 16))
client.write_single_register(ModbusTCP_ADRESS_MAC_2nd_Byte, int("0x81", 16))
client.write_single_register(ModbusTCP_ADRESS_MAC_3rd_Byte, int("0x82", 16))
client.write_single_register(ModbusTCP_ADRESS_MAC_4th_Byte, int("0x83", 16))
client.write_single_register(ModbusTCP_ADRESS_MAC_5th_Byte, int("0x84", 16))
client.write_single_register(ModbusTCP_ADRESS_MAC_6th_Byte, int("0x85", 16))

client.write_single_register(ModbusTCP_ADRESS_RS485_serial_baud_rate, 5)             #5
client.write_single_register(ModbusTCP_ADRESS_RS485_serial_setting, 4)               #4

client.write_single_register(ModbusTCP_ADRESS_num_of_sensor_per_station, 5)          #5
client.write_single_register(ModbusTCP_ADRESS_station_address, 1)                    #1
client.write_single_register(ModbusTCP_ADRESS_PLC_offset, 30)                        #40

client.write_single_register(ModbusTCP_ADRESS_onboard_inputs_data_type, 938)
# 341 all inputs send on_timer data
# 853 input 1, 2, 3, 4 send on_timer and input 5 sends edge and on_timer
# 1023 all inputs send edge and on_timer
# 938 input 1, 2, 3, 4 send edge and input 5 sends edge and on_timer

client.write_single_coil(ModbusTCP_ADRESS_config_change_flag, 1)
#final
