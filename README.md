# Norman Police Department Incident Summary


## Author
### Bhavya Reddy Kanuganti
Email: bhavya.reddy.kanuganti-1@ou.edu
## Project Description
The aim of the project is to download incident summary pdf from [The Norman police department website](https://www.normanok.gov/public-safety/police-department/crime-prevention-data/department-activity-reports) 
and extract required fields. Then using sqlite database has to be created and the extracted data should be inserted into the database. The nature of the incident and the number of times it occurs has to be displayed.
# Packages Installed
The following packages were used in the project:

urllib 

urllib.request 

tempfile

PyPDF2

sqlite3

ssl

re

# Files and Function Description
main.py, project0.py and testare the files used in this code
## 1. main.py
All the functions defined in the project0.py file are called in main.py file for execution.
## 2. project0.py
The required functions are defined in project0.py file 
### Function Description
### 1. fetchincidents(url)
urllib.request library is used in this function.An aurgument url is passed, for fetching the data and then returning it.
### 2. extractincidents(data)
In this function the fetched data is written in a temporary file and that is read using PyPdf2.
Each row from each page is extracted from the pdf and is stored in a list. There are few exceptions that has to be taken care of while extracting.
The headings and the date that data was released should be replaced.
I have attached '$' before the date and the using a for loop
'\n' was replaced with ',' and '$' with '\n' so that each column is displayed as element of list.
It is then split into a seperate lists and each list is appended to a variable if length is 5. I have used try exept block if the length of string is either greater than or less than 5 
If length of the list is less than 5 and the nature is unknown we count the number of unknown values. If length is greater than 5 
then it is considered that in place of nature of incidents the next line of address is displayed so the next element is being appended to the nature of incidents row in the end. 
In this function we return all the rows, length of the row and count of unknown nature of incidents.


### 3. createdb()
Database is created using sqlite. A table named incidents with incident_time, incident_number, incident_location, nature, and incident_ori columns
is being created in norman.db. This function returns db.

### 4. populatedb(db, incidents0, incidents1, incidents2, incidents3, incidents4, x)
The db, data from each row and length of the row are passed as arguments for this function. The data that has been fetched and extracted from the pdf is inserted into the database.

### 5. status(db)
This function takes db as the argument, the nature of incident and the number of times that has occured will be sorted and printed and also the number of times nature of incidents is unknown is also displayed in the end.

## 3. test_project0.py
This file tests all the functions in project0.py file, when executed it returns
ifv test case has passed or failed.

### 1. test_fetchincidents()
This test function is used to test fetchincidents() function in project0.py, test is passed if the data that has been fetched from the pdf is not none.

### 2. test_extractincidents()
This test function is used to test extractincidents() in project0.py, test is passed if all the rows in the pdf are not none.

### 3. test_createdb()
This test function is used to check weather the normapd.db database has been created or not in createdb() function in project0.py.

### 4. test_popuatedb()
This test function is used to test populatedb() function in project0.py and is passed if each row in the database has been inserted with the extracted data.

### 5. test_status()
This is a test function for status() function in project0.py and is passed if the records returned is not none.
### Assumptions and bugs

If length of the list of columns is greater than five then the fifth element in the list is taken as nature since   

# Execution
The following command has to be used to run the main.py file:

pipenv run python project0/main.py --incidents <url>

pipenv run python project0/main.py --incidents "https://www.normanok.gov/sites/default/files/documents/2022-02/2022-02-21_daily_incident_summary.pdf"

The following command has to be used to run the test_project0.py  file  
  
pipenv run pytest  
  

# External links used

https://www.geeksforgeeks.org/

https://www.markdownguide.org/cheat-sheet/

https://www.programcreek.com/python/example/69411/ssl._create_default_https_context

https://www.kite.com/python/

https://note.nkmk.me/en/python-string-line-break/

https://appdividend.com/2022/01/26/how-to-create-sqlite-database-in-python/
