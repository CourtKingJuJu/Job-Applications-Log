import pandas as pd
import csv
from datetime import datetime
from dataEntry import getCompany, getDate, getDescription, getHiringManager, getJobTitle, getStatus


class CSV():
    
    csvFile = "Job_Application_Log"
    columns = ["date","job_title", "company", "hiring_manager", "description", "status"]
    dateFormat = "%d-%m-%Y"

    # Checks to see if there is a file named 'Job_Applicartion_log'. If not creates file
    @classmethod
    def initalizeCSV(cls):
        try:
            pd.read_csv(cls.csvFile)
        except FileNotFoundError:
            dataFrame = pd.DataFrame(columns=cls.columns)
            dataFrame.to_csv(cls.csvFile, index=False)  #Index false just does not use the pandas default indexing I.E. (0, 1, 2)

    @classmethod
    def addApplication(cls, date, jobTitle, Company, hiringManager, Description, Status):
        
        newData = {"date": date, "job_title": jobTitle, "company": Company, "hiring_manager": hiringManager, "description": Description, "status": Status}
        
        with open(cls.csvFile, "a", newline="") as csvFile:
        
            writer = csv.DictWriter(csvFile, fieldnames=cls.columns)
            writer.writerow(newData)
            
        print("Added Entry, What else can we help you with today?")


def add():
    date = getDate("Please provide the date or press enter for todays date: ", True)
    jobTitle = getJobTitle()
    company = getCompany()
    hiringManager = getHiringManager()
    description = getDescription()
    status = getStatus()
    
    CSV.addApplication(date, jobTitle, company, hiringManager, description, status)
    
CSV.initalizeCSV()
add()