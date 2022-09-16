# module imports
from datetime import datetime # Importing the datetime library to calculate the time taken to complete the entire
import csv                      # The library is imported to use the functions required to read the csv files in the program
import itertools                # The iteration of variable that takes in the csv file is done with function islice, which is in the library itertools
Start = datetime.now()
# The inputted codes are checked for errors
try:                        
   
    Table_Name="`readings`"                                             # A variable is created to carry out the sql command to read values
                                                                        
    csvfile=csv.DictReader(open("clean.csv"),delimiter = ';');             # The csv file is read into a dictionary for reading in values.
    
    number=1;                                                              # A counter is initialised to record the indices of values
    f= open ("insert-100.sql","w")                                          # The SQL file to write the values is intialised 
                                    
    for row in itertools.islice(csvfile, 100):       # The iteration to read 100 values from the dictionary, then the SQL Insert command is used to insert values into a variable.
            sqlInsert= '''                                                                                               
                INSERT INTO '''+ Table_Name +''' (`ReadingId`,`DateTime`,`NOx`,`NO2`,`NO`,
                                                    `PM10`,`NVPM10`,`VPM10`,`NVPM2.5`,
                                                    `PM2.5`,`VPM2.5`,`CO`,`O3`,`SO2`,
                                                    `Temperature`,`RH`,`AirPressure`,`DateStart`,
                                                    `DateEnd`,`Current`,`InstrumentType`,
                                                    `SiteID-fk`) 
                                                        Values
                                                    ('''+str(number)+''',\''''+row['Date Time']+'''\',\''''+row['NOx']+'''\',\''''+row['NO2']+'''\',\''''+row['NO']+'''\',
                                                    \''''+row['PM10']+'''\',\''''+row['NVPM10']+'''\',\''''+row['VPM10']+'''\',\''''+row['NVPM2.5']+'''\',
                                                    \''''+row['PM2.5']+'''\',\''''+row['VPM2.5']+'''\',\''''+row['CO']+'''\',\''''+row['O3']+'''\', \''''+row['SO2']+'''\',
                                                    \''''+row['Temperature']+'''\',\''''+row['RH']+'''\',\''''+row['Air Pressure']+'''\', \''''+row['DateStart']+'''\',
                                                    \''''+row['DateEnd']+'''\',\''''+row['Current']+'''\',\''''+row['Instrument Type']+'''\',
                                                    \''''+row['SiteID']+'''\');      
                                                    
            '''
            number=number+1;                                        
            f.write(sqlInsert)                                  # The values are written into the SQL file
    
    print("Completed in "+ str(datetime.now()-Start),'seconds')         # A time check to calculate the time is done
except Exception as e:                                                  # except to handle any error.
    print(e)




