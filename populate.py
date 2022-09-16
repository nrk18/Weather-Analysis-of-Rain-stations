import mariadb                                                  # The SQL Database used her is Mariadb, so all the commands to mariadb work with mariadb library 
import sys                                                      # The  library provides access to interact with interpreter
import datetime                                                 # The library to check the time taken to run the file

start = datetime.datetime.now()                                         # the time required for the program to run is measured

try:                                                                                    # codes are tried for errors.
    conn = mariadb.connect(user='root',password='', host= 'localhost', port=3306)       # Firstly, the connection to the Maria server is established
    cur= conn.cursor()                                                                  # To execute all the commands the cursor is used. 

    cur.execute("DROP DATABASE IF EXISTS `pollution-db2`")                              # Deletes existing database if it exists
    cur.execute("CREATE DATABASE `pollution-db2`")                                      # and creates a new one
    conn.commit()                                                                       # connection commits the changes done on the database and exits.
    conn.close()
except BaseException as err:                                                            # To handle any error in the code
    print(f"An error occured: {err}")
    sys.exit(1)                                                                         # Exits from the program if any error is found in the code

try:
    conn = mariadb.connect(user='root',password='', host= 'localhost', port=3306)       # Trying a new set of codes, the connection is now established with the created database
    cur= conn.cursor()                                                                  # Placing the cursor in the database to execute the commands
    cur.execute("USE `pollution-db2`")                                                  # The database pollution-db2 is used to execute the commands
    cur.execute("CREATE TABLE `stations`(`SiteID` INT PRIMARY KEY, \
            `location` VARCHAR(48), geo_point_2d VARCHAR(24))")                         # The table stations is created                
    cur.execute("CREATE TABLE readings(readingid INT PRIMARY KEY AUTO_INCREMENT, \
        `date time` DATETIME NULL, nox FLOAT NULL, no2 FLOAT NULL, `no` FLOAT NULL, \
            `pm  10` FLOAT NULL, `nvpm 10` FLOAT NULL, `vpm 10` FLOAT NULL, \
            `mvpm 2.5` FLOAT NULL, `pm 2.5` FLOAT NULL, `vpm 2.5` FLOAT NULL,\
            co FLOAT NULL, o3 FLOAT NULL, so2 FLOAT NULL, temperature REAL NULL, \
            rh INT NULL, `air pressure` INT NULL, datestart DATETIME NULL, dateend DATETIME NULL, \
            current TEXT(5) NULL, instrumenttype VARCHAR(32) NULL, `SiteID` INT NOT NULL, FOREIGN KEY(`SiteID`) REFERENCES stations(SiteID))")
                                                                                        # The table readings is created
    cur.execute("CREATE TABLE `schema`(schemaID int PRIMARY KEY AUTO_INCREMENT, `measure` VARCHAR(32) UNIQUE, \
    `description` VARCHAR(64) NOT NULL, `unit` VARCHAR(24) NOT NULL)")                  # The table schema is created

    conn.commit()                                                                       # The changes made in the mariadb server is committed.

    schema_lines=[]                                                                     # The values to be entered into the schema table is stored in a list, the inital variable schema_lines is created 

    with open('schema.csv', mode = 'r', encoding='UTF-8') as file:                      
        schema_lines=file.readlines()                                                   # The csv file storing schema values are read into the program

    sch_header=schema_lines.pop(0)                                                      # The header values are popped out, so that only values are entered into the tables

    readings_lines=[]                                                                   # The values to be entered into the readings table is stored in a list, the inital variable readings_lines is created 


    with open('clean.csv','r') as file:                                                 
        readings_lines=file.readlines()                                                 # The csv file storing reading values are read into the program

    readings_header=readings_lines.pop(0)                                               # The header values are popped out, so that only values are entered into the tables

    schema=[]                                                                           # The variables reading values from the csv to be written into tables are defined. Schema and
    readings=[]                                                                         #  readings are set as list variables. The stations are used as set to avoid duplication of data.
    stations=set()                                                                      

# The values from the csv file is read into the respective tables through for loop iteration. For insertion SQL command is followed. 
    for number,line in enumerate(schema_lines):                                         
        record=line.split(';')
        schema.append([record[0], record[1],record[2].strip('\n')])
        #print(record)

    sql="INSERT INTO `pollution-db2`.`schema` (measure,`description`,unit) values(%s, %s, %s)"
    for row in schema:
        cur.execute(sql, row)

    for number,line in enumerate(readings_lines):
        record=line.split(';')
        stations.add((record[4], record[17], record[18]))
        readings.append([record[0], record[1],record[2],record[3],record[4],record[5],record[6],record[7],record[8],record[9],record[10],record[11],record[12],record[13],record[14],record[15],record[16],record[19],record[20],record[21],record[22].strip('\n')])

    sql="INSERT INTO `pollution-db2`.`stations` (SiteID,`location`,geo_point_2d) values(%s, %s, %s)"
    for row in stations:
        if(row):
            cur.execute(sql, row)
        else:
            row = "NULL"


    sql="INSERT INTO `pollution-db2`.`readings` (`date time`,nox,no2,`no`,`SiteID`,`pm  10`,`nvpm 10`,`vpm 10`,`mvpm 2.5`,`pm 2.5`,`vpm 2.5`,co, o3, so2,temperature,rh,`air pressure`,datestart,dateend,current,instrumenttype) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    for row in readings:
        cur.execute(sql, row)

    conn.commit()                                                                         # Changes were committed
    conn.close()                                                                          # Connection is closed
except BaseException as err:                                                              # The error with the code is handled using except  
    print(f"An error occured: {err}")
    sys.exit(1)
print('populate.py took ', str(datetime.datetime.now()-start),'seconds to execute')         # The time taken for the entire process is calculated and printed
