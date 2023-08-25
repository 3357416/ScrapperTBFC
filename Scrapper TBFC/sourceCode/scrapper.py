
def call_values(file):
    

    def call_serialNumber_value():
        serialNumber_str = "Serial Number: "
        serialNumber = file.find(serialNumber_str)
        serialNumber_value = file[serialNumber+len(serialNumber_str):serialNumber+ len(serialNumber_str)+12]
        print(serialNumber_str + serialNumber_value)
        return serialNumber_value
    
    def call_cell():
            cell_str = "Cell"
            cell  = file.find(cell_str)
            cell_value = file[cell:cell + len(cell_str) + 1]
            print("Carrier: " + cell_value)
            return cell_value
        
    def call_station():
            station_str = "TBFC20"
            station  = file.find(station_str)
            station_value = file[station:station + len(station_str) +1]
            print("Station " + station_value)
            return station_value
        
    def call_initial_battery_value():
        initial_battery_str = "Initial Battery SoC || "
        initial_battery = file.find(initial_battery_str)
        initial_battery_value = file[initial_battery + len(initial_battery_str):initial_battery + len(initial_battery_str)+2]
        print("Initial Battery: " + initial_battery_value + "%")
        return initial_battery_value
    
    def call_initial_battery_date():
        initial_battery_str = "Initial Battery SoC || "
        inital_values = file.find(initial_battery_str)
        initial_values_slice = file[inital_values - 71 : inital_values]
        
        initial_battery_date_value = initial_values_slice[0:len("xxxx-xx-xx xx:xx:xx")]
        print("Initial battery date: " + initial_battery_date_value)
        return  initial_battery_date_value

    def call_initial_values():
        initial_battery_str = "Initial Battery SoC || "
        inital_values = file.find(initial_battery_str)
        initial_values_slice = file[inital_values - 1500 : inital_values]
        # print(initial_values_slice)
        print("Initial Values: \n")

        def call_initial_FG_temp():
            initial_FG_temp_str = "FG Temp:"
            initial_FG_temp = initial_values_slice.find(initial_FG_temp_str)
            initial_FG_temp_value = initial_values_slice[initial_FG_temp + len(initial_FG_temp_str):initial_FG_temp + len(initial_FG_temp_str) + 11]
            print("FG Temp: " + initial_FG_temp_value)
            return initial_FG_temp_value
        
        initial_FG_temp_value =  call_initial_FG_temp()

        def call_initial_FG_current():
            initial_FG_current_str = "FG current:"
            initial_FG_current = initial_values_slice.find(initial_FG_current_str)
            initial_FG_current_value = initial_values_slice[initial_FG_current + len(initial_FG_current_str):initial_FG_current + len(initial_FG_current_str)+7]
            print("FG current:" + initial_FG_current_value)
            return initial_FG_current_value
          
        
        initial_FG_current_value =  call_initial_FG_current()

        def call_initial_FG_voltage():
            initial_FG_voltage_str = "FG voltage:"
            initial_FG_voltage = initial_values_slice.find(initial_FG_voltage_str)
            initial_FG_voltage_value = initial_values_slice[initial_FG_voltage + len(initial_FG_voltage_str):initial_FG_voltage + len(initial_FG_voltage_str)+8]
            print("FG voltage: " + initial_FG_voltage_value)
            return initial_FG_voltage_value
        
        initial_FG_voltage_value = call_initial_FG_voltage()

        def call_initial_FG_capacity():
            initial_FG_capacity_str = "FG capacity:"
            initial_FG_capacity = initial_values_slice.find(initial_FG_capacity_str)
            initial_FG_capacity_value = initial_values_slice[initial_FG_capacity + len(initial_FG_capacity_str):initial_FG_capacity + len(initial_FG_capacity_str) + 9]
            print("FG capacity: " + initial_FG_capacity_value)
            return initial_FG_capacity_value

        initial_FG_capacity_value = call_initial_FG_capacity()

        def call_initial_FG_avg_voltage():
            initial_FG_avg_voltage_str = "FG avg voltage:"
            initial_FG_avg_voltage  = initial_values_slice.find(initial_FG_avg_voltage_str)
            initial_FG_avg_voltage_value = initial_values_slice[initial_FG_avg_voltage + len(initial_FG_avg_voltage_str):initial_FG_avg_voltage + len(initial_FG_avg_voltage_str) + 8]
            print("FG avg voltage: " + initial_FG_avg_voltage_value)
            return initial_FG_avg_voltage_value
        
        initial_FG_avg_voltage_value = call_initial_FG_avg_voltage()

        def call_initial_FG_RSOC():
            initial_FG_RSOC_str = "FG RSOC:"
            initial_FG_RSOC  = initial_values_slice.find(initial_FG_RSOC_str)
            initial_FG_RSOC_value = initial_values_slice[initial_FG_RSOC + len(initial_FG_RSOC_str):initial_FG_RSOC + len(initial_FG_RSOC_str) + 4]
            print("FG RSOC: " + initial_FG_RSOC_value)
            return initial_FG_RSOC_value
        
        initial_FG_RSOC_value = call_initial_FG_RSOC()



        
        def call_initial_FG_USOC():
            initial_FG_USOC_str = "FG USOC:"
            initial_FG_USOC  = initial_values_slice.find(initial_FG_USOC_str)
            initial_FG_USOC_value = initial_values_slice[initial_FG_USOC + len(initial_FG_USOC_str):initial_FG_USOC + len(initial_FG_USOC_str) + 4]
            print("FG USOC: " + initial_FG_USOC_value)
            return initial_FG_USOC_value
        
        initial_FG_USOC_value = call_initial_FG_USOC()

        
        print("\n")
        return initial_FG_temp_value, initial_FG_current_value, initial_FG_voltage_value, initial_FG_capacity_value, initial_FG_avg_voltage_value, initial_FG_RSOC_value, initial_FG_USOC_value
        
    def call_final_battery_value():
        final_battery_str = "Final Battery SoC || "
        final_battery = file.find(final_battery_str)
        final_battery_value = file[final_battery + len(final_battery_str):final_battery + len(final_battery_str)+2]
        print("Final Battery: " + final_battery_value + "%")
        return final_battery_value

    def call_final_battery_date():
        final_battery_str = "Final Battery SoC || "
        inital_values = file.find(final_battery_str)
        final_values_slice = file[inital_values - 71 : inital_values]
        
        final_battery_date_value = final_values_slice[0:len("xxxx-xx-xx xx:xx:xx")]
        print("Final battery date: " + final_battery_date_value)

        return final_battery_date_value

    def call_final_values():
        
        final_battery_str = "Final Battery SoC || "
        inital_values = file.find(final_battery_str)
        final_values_slice = file[inital_values - 1500 : inital_values]
        # print(final_values_slice)
        print("Final Values: \n")
         
        def call_final_FG_temp():
            final_FG_temp_str = "FG Temp:"
            final_FG_temp = final_values_slice.find(final_FG_temp_str)
            final_FG_temp_value = final_values_slice[final_FG_temp + len(final_FG_temp_str):final_FG_temp + len(final_FG_temp_str) + 11]
            print("FG Temp: " + final_FG_temp_value)
            return final_FG_temp_value
        
        final_FG_temp_value =  call_final_FG_temp()

        def call_final_FG_current():
            final_FG_current_str = "FG current:"
            final_FG_current = final_values_slice.find(final_FG_current_str)
            final_FG_current_value = final_values_slice[final_FG_current + len(final_FG_current_str):final_FG_current + len(final_FG_current_str)+7]
            print("FG current:" + final_FG_current_value)
            return final_FG_current_value
          
        
        final_FG_current_value =  call_final_FG_current()

        def call_final_FG_voltage():
            final_FG_voltage_str = "FG voltage:"
            final_FG_voltage = final_values_slice.find(final_FG_voltage_str)
            final_FG_voltage_value = final_values_slice[final_FG_voltage + len(final_FG_voltage_str):final_FG_voltage + len(final_FG_voltage_str)+8]
            print("FG voltage: " + final_FG_voltage_value)
            return final_FG_voltage_value
        
        final_FG_voltage_value = call_final_FG_voltage()

        def call_final_FG_capacity():
            final_FG_capacity_str = "FG capacity:"
            final_FG_capacity = final_values_slice.find(final_FG_capacity_str)
            final_FG_capacity_value = final_values_slice[final_FG_capacity + len(final_FG_capacity_str):final_FG_capacity + len(final_FG_capacity_str) + 9]
            print("FG capacity: " + final_FG_capacity_value)
            return final_FG_capacity_value

        final_FG_capacity_value = call_final_FG_capacity()

        def call_final_FG_avg_voltage():
            final_FG_avg_voltage_str = "FG avg voltage:"
            final_FG_avg_voltage  = final_values_slice.find(final_FG_avg_voltage_str)
            final_FG_avg_voltage_value = final_values_slice[final_FG_avg_voltage + len(final_FG_avg_voltage_str):final_FG_avg_voltage + len(final_FG_avg_voltage_str) + 8]
            print("FG avg voltage: " + final_FG_avg_voltage_value)
            return final_FG_avg_voltage_value
        
        final_FG_avg_voltage_value = call_final_FG_avg_voltage()

        def call_final_FG_RSOC():
            final_FG_RSOC_str = "FG RSOC:"
            final_FG_RSOC  = final_values_slice.find(final_FG_RSOC_str)
            final_FG_RSOC_value = final_values_slice[final_FG_RSOC + len(final_FG_RSOC_str):final_FG_RSOC + len(final_FG_RSOC_str) + 4]
            print("FG RSOC: " + final_FG_RSOC_value)
            return final_FG_RSOC_value
        
        final_FG_RSOC_value = call_final_FG_RSOC()

        def call_final_FG_USOC():
            final_FG_USOC_str = "FG USOC:"
            final_FG_USOC  = final_values_slice.find(final_FG_USOC_str)
            final_FG_USOC_value = final_values_slice[final_FG_USOC + len(final_FG_USOC_str):final_FG_USOC + len(final_FG_USOC_str) + 4]
            print("FG USOC: " + final_FG_USOC_value)
            return final_FG_USOC_value
        
        final_FG_USOC_value = call_final_FG_USOC()

        
        print("\n")
        return final_FG_temp_value, final_FG_current_value, final_FG_voltage_value, final_FG_capacity_value, final_FG_avg_voltage_value, final_FG_RSOC_value, final_FG_USOC_value
        
    def call_date_value():
        date_value = file[0:len("xxxx-xx-xx xx:xx:xx")]
        print("Date: " + date_value)
        return date_value
        

    serialNumber_value = call_serialNumber_value()
    cell_value = call_cell()
    station_value = call_station()
    date_value = call_date_value()
    initial_battery_value = call_initial_battery_value()
    initial_battery_date_value = call_initial_battery_date()
    final_battery_value = call_final_battery_value()
    final_battery_date_value = call_final_battery_date()

    initial_FG_temp_value, initial_FG_current_value, initial_FG_voltage_value, initial_FG_capacity_value, initial_FG_avg_voltage_value, initial_FG_RSOC_value, initial_FG_USOC_value = call_initial_values() 
    final_FG_temp_value, final_FG_current_value, final_FG_voltage_value, final_FG_capacity_value, final_FG_avg_voltage_value, final_FG_RSOC_value, final_FG_USOC_value = call_final_values()
    
    return serialNumber_value, date_value, initial_battery_value,initial_FG_temp_value, initial_FG_current_value, initial_FG_voltage_value, initial_FG_capacity_value, initial_FG_avg_voltage_value, initial_FG_RSOC_value, initial_FG_USOC_value, final_battery_value,final_FG_temp_value, final_FG_current_value, final_FG_voltage_value, final_FG_capacity_value, final_FG_avg_voltage_value, final_FG_RSOC_value, final_FG_USOC_value, cell_value, station_value, initial_battery_date_value, final_battery_date_value



    
   
    


