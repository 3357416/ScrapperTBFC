import os
from scrapper import call_values
from datetime import datetime

today = str(datetime.today().strftime('%Y-%m-%d'))
now = str(datetime.today().strftime('%H-%M-%S'))

directory = 'ScrapLogs'
f = open("logs_Battery_date_" + today + "_time_" + now + ".txt", "w")
c = open("logs_Battery_date_" + today + "_time_" + now + ".csv", "w")

for item in os.listdir(directory):

    if item.endswith('.txt'):
        filename = os.path.join(directory, item)
        file = open(filename, 'r')    
        file = file.read()

        serialNumber_value, date_value, initial_battery_value,initial_FG_temp_value, initial_FG_current_value, initial_FG_voltage_value, initial_FG_capacity_value, initial_FG_avg_voltage_value, initial_FG_RSOC_value, initial_FG_USOC_value, final_battery_value,final_FG_temp_value, final_FG_current_value, final_FG_voltage_value, final_FG_capacity_value, final_FG_avg_voltage_value, final_FG_RSOC_value, final_FG_USOC_value, cell_value, station_value, initial_battery_date_value, final_battery_date_value, = call_values(file)



        f.write("\n")
       
        f.write("serialNumber: " + serialNumber_value + "\n")
        f.write("Carrier: " + cell_value +"\n")
        f.write("Station: " + station_value +"\n")
        f.write("Date: " + date_value + "\n")
        f.write("Initial Values:\n")

        f.write("Initial Battery: "+ initial_battery_value +"%\n")
        f.write("Initial Battery date" + initial_battery_date_value)
        f.write("FG_temp: " + initial_FG_temp_value + "\n")
        f.write("FG_current: " + initial_FG_current_value + "\n")
        f.write("FG_voltage: " + initial_FG_voltage_value + "\n")
        f.write("FG_capacity: " + initial_FG_capacity_value + "\n")
        f.write("FG_avg_voltage: " + initial_FG_avg_voltage_value + "\n")
        f.write("FG_RSOC: " + initial_FG_RSOC_value + "\n")
        f.write("FG_USOC: " + initial_FG_USOC_value + "\n")
        f.write("\n")

        f.write("Final Values:\n")
        f.write("Final Battery: "+ final_battery_value + "%\n")
        f.write("Final Battery date" + final_battery_date_value)
        f.write("FG_temp: " + final_FG_temp_value + "\n")
        f.write("FG_current: " + final_FG_current_value + "\n")
        f.write("FG_voltage: " + final_FG_voltage_value + "\n")
        f.write("FG_capacity: " + final_FG_capacity_value + "\n")
        f.write("FG_avg_voltage: " + final_FG_avg_voltage_value + "\n")
        f.write("FG_RSOC: " + final_FG_RSOC_value + "\n")
        f.write("FG_USOC: " + final_FG_USOC_value + "\n")
        f.write("\n")
        f.write("\n")
        
        
        c.write(",\n")

        

        c.write("Serial Number,Date, Cell#,Station,Incomming Totem SoC,Date,Outgoing Totem SoC,Date\n")
        c.write(serialNumber_value + "," + date_value + "," + cell_value + "," + station_value + "," + initial_battery_value + "%," + initial_battery_date_value + "," + final_battery_value + "%," + final_battery_date_value + "\n")
        c.write("\n")
        c.write("Initial Parameters: ,Value,Final Parameters: ,Value \n ")
        c.write("Serial Number:," + serialNumber_value + ",Serial Number:,"+ serialNumber_value + "\n")
        c.write("FG_temp: ," + initial_FG_temp_value + ",FG_temp: ," + final_FG_temp_value +"\n")
        c.write("FG_current: ," + initial_FG_current_value + ",FG_current: ," + final_FG_current_value + "\n")
        c.write("FG_voltage: ," + initial_FG_voltage_value + ",FG_voltage: ," + final_FG_voltage_value + "\n")
        c.write("FG_capacity: ," + initial_FG_capacity_value + ",FG_capacity: ," + final_FG_capacity_value + "\n")
        c.write("FG_avg_voltage: ," + initial_FG_avg_voltage_value + ",FG_avg_voltage: ," + final_FG_avg_voltage_value + "\n")
        c.write("FG_RSOC: ," + initial_FG_RSOC_value + ",FG_RSOC: ," + final_FG_RSOC_value +"\n")
        c.write("FG_USOC: ," + initial_FG_USOC_value + ",FG_USOC: ," + final_FG_USOC_value +  "\n")
        
        c.write("\n")
        c.write(",\n")
        

c.close()
f.close()
input()