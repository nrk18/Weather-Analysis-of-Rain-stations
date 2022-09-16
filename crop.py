import csv                                                                      # Library to read and write csv files is imported
from datetime import datetime                                                   # To calculate the time taken to run the program, datetime library was imported
start=datetime.now()                                                            # The start time of the program is initialised
file= csv.DictReader(open("bristol-air-quality-data.csv"), delimiter=';')       # The csv file is read as dictionary variable
                                                           
with open('crop.csv','w',newline='') as write_file:
    writer=csv.DictWriter(write_file,fieldnames=file.fieldnames, delimiter=';') # To write the filtered values from csv into a new file, first it is written in the program as a variable 
    writer.writeheader()                                                        # The header values are stored seperately

# The syntax of the program that filters out the values that were taken before Jan 1, 2010. For that the values stored after the year 2010 is written into the new csv file  
    for row in file:
        if(row['Date Time']==''):
            continue
        else:
            row['Date Time']=datetime.strptime(row['Date Time'],'%Y-%m-%dT%H:%M:%S%z')
            if(row['Date Time'].year>=2010):
                writer.writerow(row)
            else:
                continue
print('crop.py took ', str(datetime.now()-start),'seconds to execute')          # The time taken to run the program is printed