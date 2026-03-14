def truckTour(petrolpumps):

    start_pump_index = 0
    current_fuel = 0
    
    for pump_index in range(len(petrolpumps)):
        
        petrol_amount = petrolpumps[pump_index] [0]
        distance_to_next_pump = petrolpumps[pump_index] [1]
        current_fuel += petrol_amount - distance_to_next_pump
        
        if current_fuel < 0:
            start_pump_index = pump_index +1
            current_fuel =0
            
    return start_pump_index
