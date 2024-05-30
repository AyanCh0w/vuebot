from selenium import webdriver
from selenium.webdriver.common.by import By

def getGradeInfo(username, password):
  driver = webdriver.Chrome()

  driver.get("https://md-mcps-psv.edupoint.com/PXP2_Login_Student.aspx?regenerateSessionId=True")

  #LOGIN
  usernameInput = driver.find_element(by= By.NAME, value= "ctl00$MainContent$username")
  passwordInput = driver.find_element(by= By.NAME, value= "ctl00$MainContent$password")
  submitInput = driver.find_element(by= By.NAME, value= "ctl00$MainContent$Submit1")

  usernameInput.send_keys(username)
  passwordInput.send_keys(password)
  submitInput.click()

  #ENTER INTO GRADEBOOK
  driver.implicitly_wait(0.5)

  gradeBookInput = driver.find_element(by= By.XPATH, value= '/html/body/div[4]/div[2]/div/div[2]/form/div[4]/component-provider/launch-pad/div/div/div[2]/div/div[8]')
  gradeBookInput.click()

  #GET CLASS DATA
  driver.implicitly_wait(0.5)

  classData = []
  for i in range(1, 7):
    if i != 1:
      classNameIndex = (2*i)+(i-2)
    else:
      classNameIndex = i

    classData.append({
      'className': driver.find_element(by= By.XPATH, value= f'/html/body/div[4]/div[2]/div/div[2]/form/div[4]/div[2]/div[2]/div[1]/div/div[1]/div[2]/div[{classNameIndex}]/div[1]/button'),
      'classGrade': driver.find_element(by= By.XPATH, value= f'/html/body/div[4]/div[2]/div/div[2]/form/div[4]/div[2]/div[2]/div[1]/div/div[1]/div[2]/div[{classNameIndex+1}]/div[1]/div[2]/span[1]')
    })

  formattedClassData = []
  for clas in classData:
    formattedClassData.append([
      clas['className'].text[3:],
      clas['classGrade'].text
    ])

  
  return formattedClassData

  driver.quit()

