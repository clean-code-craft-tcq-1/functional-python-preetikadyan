
def collect_out_of_range_battery_parameters(parameters_exceeded_limit,parameter_name,parameter_value,parameter_limit):
     if parameter_value < parameter_limit['min'] or parameter_value > parameter_limit['max']:
        parameters_exceeded_limit.append(parameter_name)
