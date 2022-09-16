import csv                                                                                          # The csv library is imported to read and write csv files
from datetime import datetime                                                                       # The datetime library is imported to find the time taken to run the program

start=datetime.now()                                                                                # The start of the program is noted
input_file= csv.DictReader(open("crop.csv"), delimiter=';')                                         # The csv file is read into the program as a dictionary value

stations = {
    '188':'AURN Bristol Centre', '203':'Brislington Depot', '206':'Rupert Street', '209':'IKEA M32',    
'213':'Old Market', '215':'Parson Street School','228':'Temple Meads Station', '270':'Wells Road', 
'271':'Trailer Portway P&R', '375':'Newfoundland Road Police Station', '395':"Shiner's Garage",
'452':'AURN St Pauls', '447':'Bath Road', '459':'Cheltenham Road \ Station Road', '463':'Fishponds Road', 
'481':'CREATE Centre Roof', '500':'Temple Way', '501':'Colston Avenue'
}                                                                                                    # A dictionary is created with key-value pair as siteid and location 
                                                                                                     #   to check the mismatch in the csv file

addrow= 1                                                                                            # A counter to count the number of rows entered in the new csv  
removerow=0                                                                                          # A counter to count the number of rows not entered in the new csv

with open('clean.csv','w',newline='') as output_file:
    csv_writer=csv.DictWriter(output_file,fieldnames=input_file.fieldnames, delimiter=';')
    csv_writer.writeheader();
    for row in input_file:
        if((row['SiteID'],row['Location']) in stations.items()):
            addrow+=1;
            csv_writer.writerow(row);
        else:
            removerow+=1;                                                                              # using the dictionary defined above, the values in the csv file is 
                                                                                                       # checked for mismatch and a new csv file, in which the mismatch is removed is written
print(str(removerow) +' mismatches found and lines removed')                                           # The number of rows removed from the csv is printed
print(str(addrow) +' Lines written to clean.csv')                                                      # The number of rows written to the csv is printed
print("The program took", str(datetime.now()-start)," to complete")                                    # The time taken for the program is printed
