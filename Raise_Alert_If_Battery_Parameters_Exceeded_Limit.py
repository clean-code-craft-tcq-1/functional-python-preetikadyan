from Report_Out_Of_Limit_Parameters import *
from Collect_Out_Of_Limit_Parameters import *

def raise_alert_battery_if_parameters_not_within_limit(Battery_Life_Parameters):
     battery_parameters_exceeded = report_out_of_limit_battery_parameters(Battery_Life_Parameters)
     if len(battery_parameters_exceeded) > 1 :
          print(len(battery_parameters_exceeded),"battery Parameters not within limit--->High Breach")
     elif len(battery_parameters_exceeded) == 1:
          print(len(battery_parameters_exceeded),"battery Parameters not within limit--->Low Breach")
     else :
          print("No battery parameter exceeded limit") 
