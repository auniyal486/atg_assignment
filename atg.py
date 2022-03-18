import mysql.connector
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import requests
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import os
load_dotenv()# for getting .env file's variable
class atg:
    mycursor=mydb=None
    def __init__(self,email,password,database_password):
        self.mydb=mysql.connector.connect(
            host="pxukqohrckdfo4ty.cbetxkdyhwsb.us-east-1.rds.amazonaws.com",
            user="vjcgx7f2h6c83kso",
            password='q3u6cd8d3na4qahc',
            database="ge9dqfao1hyo6sxq",
            auth_plugin='mysql_native_password'
        )# for connecting to sql database
        self.mydb.autocommit = True
        self.mycursor=self.mydb.cursor()
        data=self.career_guide() #https://www.careerguide.com/career-options
        url="https://www.linkedin.com/jobs"
        driver = webdriver.Chrome('C:/Users/abhis/Downloads/chromedriver') #initialize webdriver with selenium
        driver.get(url)# open url in web browser window which is controlled by selenium
        signin=driver.find_element_by_css_selector('a[data-tracking-control-name="guest_homepage-jobseeker_nav-header-signin"]') #find signin element 
        ActionChains(driver).click(signin).perform()#go to singin page
        driver.find_element_by_css_selector('#username').send_keys(email)# pass email to input element in signin page
        driver.find_element_by_css_selector('#password').send_keys(password)#pass password to input element in signin page
        submit=driver.find_element_by_css_selector('button[aria-label="Sign in"]')#find id of sign in button
        ActionChains(driver).click(submit).perform()#click signin button
        states=["Andaman and Nicobar","Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chandigarh","Chhattisgarh",\
                "Dadra and Nagar Haveli","Daman and Diu ","Delhi","Goa","Gujarat","Haryana","Himachal Pradesh",\
                "Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Lakshadweep","Madhya Pradesh","Maharashtra",\
                "Manipur","Meghalaya","Mizoram","Nagaland","Orissa","Puducherry ","Punjab","Rajasthan","Sikkim",\
                "Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal"]
        for i in states:
            self.mycursor.execute("INSERT INTO atg_app_states (State) VALUES (%s)",(i,))
        delay=50
        count=0
        for i in data:#iterate through different categorie
            for j in data[i]:#iterate through different subcategorie
                for l in states: 
                    state=l
                    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR,\
                                                    'input[aria-label="City, state, or zip code"]'))).send_keys(l)
                    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR,\
                                                'input[aria-label="Search by title, skill, or company"]'))).send_keys(j,Keys.ENTER)
                    #pass subcategorie to search input box and press enter button
                    val=WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#results-list__title'))).text
                    if("Jobs you may be interested in" in val):
                        driver.back()
                        continue
                    results=WebDriverWait(driver, delay).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'.jobs-search-results__list li .job-card-list__title')))
                    list_pages=[]
                    for k in results:
                        try:
                            t=k.get_attribute("href")
                            list_pages.append(t)
                        except:
                            pass
                        #storing all job post link of current page
                    if len(list_pages)==0:
                        driver.back()
                        continue
                    for t in list_pages:
                        driver.execute_script("window.open('');")
                        driver.switch_to.window(driver.window_handles[1])
                        driver.get(t) 
                        try:
                            jobTitle=WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'h1'))).text#scrape comapny name
                        except:
                            jobTitle=None
                        try:
                            q=driver.find_element_by_css_selector('.jobs-unified-top-card__subtitle-primary-grouping ')
                            company=q.find_element_by_css_selector('span').text#scrape company name
                        except:
                            company=None
                        try:
                            location=q.find_element_by_css_selector('span[class="jobs-unified-top-card__bullet"]').text# scrape location
                        except:
                            location=None
                        try:
                            workType=q.find_element_by_css_selector('span[class="jobs-unified-top-card__workplace-type"]').text
                            if(workType.strip()=='Remote'):
                                location=None
                                state=None
                        except:
                            workType=None
                        try:
                            link=q.find_element_by_css_selector('a').get_attribute("href")#get link of company page
                            driver.execute_script("window.open('');")
                            driver.switch_to.window(driver.window_handles[2])
                            driver.get(link)
                            try:
                                locat_ele=WebDriverWait(driver, delay).until(EC.presence_of_all_elements_located(\
                                                        (By.CSS_SELECTOR, '.org-top-card-summary-info-list__info-item')))
                                field=locat_ele[0].text
                                headqua_ele=locat_ele[1].text
                                headqua=None
                                if('follower' not in headqua_ele):
                                    headqua=headqua_ele
                            except:
                                headqua=None
                                field=None
                            navigation_items=driver.find_elements_by_css_selector('ul[class="org-page-navigation__items "] li')
                            ActionChains(driver).click(navigation_items[1]).perform()
                            WebDriverWait(driver, delay).until(lambda driver:'about' in driver.current_url.split('/'))
                            try:
                                description=driver.find_element_by_css_selector('.org-grid__content-height-enforcer p').text
                            except:
                                description=None #scrape description
                            driver.close()
                        except:
                            headqua=None
                            field=None
                            description=None
                        try:
                            self.mycursor.execute("INSERT INTO atg_app_companydetails (Name,Field,Headquarters,Description)\
                            VALUES (%s,%s,%s,%s);",(company,field,headqua,description))#adding record in companydetails table
                        except:
                            pass
                        try:
                            self.mycursor.execute("INSERT INTO atg_app_jobs (Company_id,JobPosition,Location,WorkType,State,Subcategory) VALUES\
                            ((SELECT id FROM atg_app_companydetails WHERE Name = %s AND Field=%s),%s,%s,%s,(SELECT State FROM atg_app_states WHERE State = %s),(SELECT Subcategory FROM atg_app_jobtype2 WHERE Subcategory = %s));",(company,field,jobTitle,location,\
                            workType,state,j))#adding record in jobs table
                        except:
                            pass
                        state=l
                        driver.switch_to.window(driver.window_handles[1])
                        driver.close()
                        driver.switch_to.window(driver.window_handles[0])
                        count+=1
                        if(count>100):
                            #for simplicity and posting csv file to github, we are only storing 100 jobs 
                            break
                    driver.back()
                    if(count>100):
                        break
                if(count>100):
                    break
            if(count>100):
                break
    def career_guide(self):
        url=requests.get("https://www.careerguide.com/career-options")
        soup = BeautifulSoup(url.text, 'html.parser')
        val=soup.find("div",{"class":"c-body"}).find_all("div",{"class":"col-md-4"})
        data={}
        for i in val:
            head=i.h2.text
            data[head]=[]
            count=0
            self.mycursor.execute("INSERT INTO atg_app_jobtype1 (Category) VALUES (%s)",(head,))
            for j in i.find_all("li"):
                try:
                    self.mycursor.execute("INSERT INTO atg_app_jobtype2 (Category,Subcategory) VALUES ((SELECT Category FROM atg_app_jobtype1 WHERE Category = %s), %s);",(head,j.text,))
                    data[head].append(j.text)
                except:
                    pass
                count+=1
                if(count==2):
                    break
        return data  

email=os.getenv("email")
password=os.getenv("password")
database_password=os.getenv("database_password")
atg(email,password,database_password)
