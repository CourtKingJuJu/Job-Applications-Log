from datetime import datetime

dateFormat =  "%d-%m-%Y"
Categories = {"O": "Offer", "A": "Applied", "I": "Interview"}

def getDate(prompt, allowDefault=False):
    
    date_str = input(prompt)
    
    if allowDefault and not date_str:
        return datetime.today().strftime(dateFormat)
    else:
        try:
            valid_date = datetime.strptime(date_str, dateFormat)
            return valid_date.strftime(dateFormat)
        except ValueError:
            print("Invalid date format. Please enter the date in dd-mm-yyyy format")
            return getDate(prompt, allowDefault)
        

def getJobTitle():
    return input("Please provide the job title: ")

def getCompany():
    return input("Please provide the Company name: ")

def getHiringManager():
    return input("Please provide the Hiring Manager name: ")

def getDescription():
    return input("Pleae enter a breif description of the job: ")

def getStatus():
    
    status = input("Please input the job status (A: Applied, I: Interview, O: Offer): ")
        
    if status in Categories:
        return Categories[status]
    
    print("Please provide valid input (A: Applied, I: Interview, O: Offer): ")
    getStatus()