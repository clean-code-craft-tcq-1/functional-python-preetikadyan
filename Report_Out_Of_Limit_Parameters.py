from Collect_Out_Of_Limit_Parameters import *

def report_out_of_limit_battery_parameters(Battery_Life_Parameters):
     parameters_exceeded_limit = []
     for battery_parameter in Battery_Life_Parameters:
          collect_out_of_range_battery_parameters(parameters_exceeded_limit,battery_parameter,Battery_Life_Parameters[battery_parameter],limit[battery_parameter])
     return parameters_exceeded_limit 