from Raise_Alert_If_Battery_Parameters_not_within_Limit import *

limit = {
     'temperature': {'min': 0, 'max': 45},
     'state_of_charge': {'min': 20, 'max': 80},
     'charge_rate': {'min' : 0, 'max': 0.8}
        }     
    
if __name__ == '__main__':
     raise_alert_battery_if_parameters_not_within_limit({'temperature' : 25, 'state_of_charge' : 70, 'charge_rate' : 0.7})
     raise_alert_battery_if_parameters_not_within_limit({'temperature' : 50, 'state_of_charge' : 85, 'charge_rate' : 0})
     raise_alert_battery_if_parameters_not_within_limit({'temperature' : 25, 'state_of_charge' : 40, 'charge_rate' : 0.9})

