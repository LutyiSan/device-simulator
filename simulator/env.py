MQTT_PARAMS = {'PUBLISHER': "lutyisan",
               'TRANSPORT': "websockets",
               'PATH': "/ws",
               'USER_NAME': "admin",
               'USER_PASS': "admin",
               'HOST': "46.8.210.67",
               'PORT': 15675,
               'SLEEPING_TIME': 3}

dict_heat = {'name': "heat-counter",
             'TE-1': 56,
             "TE-2": 34,
             'TE-3': 70,
             "TE-4": 60,
             "PE-1": 3.5,
             "PE-2": 2.8,
             "PE-3": 4.2,
             "PE-4": 3.5,
             "massa_in": 2321,
             "massa_out": 923,
             "volume_in": 628,
             "volume_out": 23,
             "heat_power": 2456,
             "heat_energy": 786}

dict_el = {'name': "el-counter",
           'volt_a': 221,
           "volt_b": 219,
           'volt_c': 223,
           "curr_a": 34,
           "curr_b": 32,
           "curr_c": 29,
           "act_en": 2245,
           "react_en": 237,
           "full_en": 2700,
           "act_pow": 6.00,
           "react_pow": 4.00,
           "full_pow": 9.00,
           }

dict_cool_water = {"name": 'cool-water', "volume": 4356}
dict_heat_water = {'name': "heat-water", "volume": 3871}
DEVICES = [dict_heat, dict_el, dict_cool_water, dict_heat_water]
DB = {'HOST': '46.8.210.67', 'PORT': 6033, 'USERNAME': 'root', 'PASSWD': 'admin', 'DBNAME': 'vbas'}
