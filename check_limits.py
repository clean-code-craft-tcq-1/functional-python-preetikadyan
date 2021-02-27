limit = {
     'temperature': {'min': 0, 'max': 45},
     'state_of_charge': {'min': 20, 'max': 80},
     'charge_rate': {'max': 0.8}
        } 
 
def collect_out_of_range_battery_parameters(parameters_exceeded_limit,parameter_name,parameter_value,parameter_limit):
     if parameter_value < parameter_limit['min'] or parameter_value > parameter_limit['max']:
        parameters_exceeded_limit.append(parameter_name)
         
def report_out_of_limit_battery_parameters(Battery_Life_Parameters):
     parameters_exceeded_limit = []
     for battery_parameter in Battery_Life_Parameters:
         collect_out_of_range_battery_parameters(parameters_exceeded_limit,battery_parameter,Battery_Life_Parameters[battery_parameter],limit[battery_parameter])
     return parameters_exceeded_limit    
     

if __name__ == '__main__':
    
  Battery_Life_Parameters = {
       'temperature' : 25,
       'state_of_charge' : 70,
       'charge_rate' : 0.9
          }  
  
print(report_out_of_limit_battery_parameters(Battery_Life_Parameters))
     
