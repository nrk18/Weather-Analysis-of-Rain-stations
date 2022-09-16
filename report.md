# Report on Assignment on Data Management Fundamentals
The purpose of all the assignments is to make a person better understand the key things learnt. <br /> <br />
The problems encountered and their solutions were giving opportunities to widen the understanding of the different approaches that can be taken in completing any task. Taking each task separately would be effective in describing the process through which completion was possible.
### Task 1: Crop, Cleanse and Refactor the Data.
The task was composed of a column date time which was formatted in timestamp. The solution to find a method to filter out the values previous to the year 2010, was found out after going through several trials. Only after changing the date stamp to a datetime variable, the filtering was possible. The second sub-task took a lot of trial and error. The dictionary was used to identify the key-value pair in the `siteId` and `Location` columns. Even though the right method was obtained only after the discussion on assignment in the class.
### Task 2: Create and Implement a Normalized Database.
This was an easy task. The application MySQL workbench was used to create an ER model. The model was done forward engineer to create a physical database from the ER model and then using reverse engineering, an ER model was made from a physical database. The SQL script was written to do the reverse engineering.
### Task 3: Write Python scripts to populate the database & generate SQL.
The understanding of writing the python script to populate a database and the syntax that covers all the steps were referred from various sources. That was easy to understand. However, writing the codes was troublesome. The `populate.py` file always returned an error. It took a lot of trials to get the program running. Even after that the database were not fully populating. The task was kept pending and attended after completing task 5. The next time when it was run, the problems were easily rectified. The second part of this task was easy to program. The distress felt in task 3a, was relieved after completing this task.
### Task 4: Design, Write and Run SQL Queries.
Running SQL queries required connecting Visual Studio code with the SQL database. The queries were tried multiple times to get the required result. The `stackoverflow` website along with `w3schools` helped in understanding SQL. After understanding basics of SQL, it was felt as a simple language to access database and how it could not be replaced by any other language for querying due to its simplicity.
### Task 5: Model, implement and query a selected NoSQL database.   
This task was faced with confusions and anxiety. This task weighed more marks, it was difficult to understand. Whether the NoSQL database must be populated with all the readings from Bristol air quality and then report on it or is it about understanding a NoSQL database. The worries were cleared through discussion with the tutor. The modelling and understanding of NoSQL was really exciting. The knowledge about NoSQL was really beneficial as I think the future will be about going further than NoSQL.
### Visualizing tools         
The most widely used tools for data visualization is graphs and charts. The libraries in python like seaborn and matplotlib are commonly used for data visualization. Some of the data visualization libraries are explained below:
1.  Matplotlib: It can be used in python regardless of the application. The library also supports a wide range of popular charts and graphs.
2.  Seaborn: This library provides the user with all types of beautiful visualizations.
3.  Bokeh: A library that can handle web friendly visualization.
4.  Altair: Focusses on spending less time in coding and more time to make the visualization look more informative.

The readings in the Bristol Air quality csv file is incomplete. Since the readings are from 2010, the use of charts will be of use in the case of  pie chart. It could give the change in contribution of certain values to pollution. However, it is better to use graphs to show the variations over the years. So, using graphs such as scatterplot or bar plot, the variation of values of `NOx`, `NO` and `NO2` (as these are the only values entered for most of the stations) can be identified.

### Learning Outcome
In short, there was a ton of knowledge gained by going through the tasks in this assignment. The errors in the program was always teaching me the various possibilities by which a problem in coding can be solved. The assignment was designed in such a way that it almost covered a lot of area of the fundamentals of data management.
