from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
 
def get_web(myWidget): 
    options = Options()
    options.add_argument("--disable-notifications")
    
    browser = ''

    if myWidget.browser.currentText() == "Chrome":
        browser = webdriver.Chrome('./chromedriver', chrome_options=options)
    elif myWidget.browser.currentText() == "Firefox":
        browser = webdriver.Firefox()

    browser.get("https://www.railway.gov.tw/tra-tip-web/tip/tip001/tip121/query")

    browser.implicitly_wait(5)

    # ID card
    pid = browser.find_element("id", "pid")
    pid.send_keys(myWidget.idCard.text())

    #start station
    startStation = browser.find_element("id", "startStation")
    # startStation.send_keys("1000-臺北")
    startStation.send_keys(myWidget.startStation.text())

    # end station
    endStation = browser.find_element("id", "endStation")
    endStation.send_keys(myWidget.endStation.text())
    
    # tripType
    if myWidget.roundtripSelect.isChecked():
        tabs =  (Keys.TAB)*3
        endStation.send_keys(tabs + Keys.ARROW_RIGHT)

    # tickets number
    normalQty = browser.find_element("id", "normalQty")
    normalQty.clear()
    normalQty.send_keys(myWidget.ticketNum.text())

    # date 1
    rideDate1 = browser.find_element("id", "rideDate1")
    rideDate1.clear()
    rideDate1.send_keys(myWidget.date1.text())

    # train number 1
    trainNoList1 = browser.find_element("id", "trainNoList1")
    trainNoList1.send_keys(myWidget.trainNumber1.text())

    if myWidget.roundtripSelect.isChecked():
        # date 2
        rideDate2 = browser.find_element("id", "rideDate2")
        rideDate2.clear()
        rideDate2.send_keys(myWidget.date2.text())

        # train number 2
        trainNoList2 = browser.find_element("id", "trainNoList4")
        trainNoList2.send_keys(myWidget.trainNumber2.text())        

    # # tabs from trainNoList1 to recaptcha
    tabs =  (Keys.TAB)*8
    if not myWidget.testSelect.isChecked():
        if myWidget.onewaySelect.isChecked():
            trainNoList1.send_keys(tabs + " ")
        else:
            trainNoList2.send_keys(tabs + " ")

    if myWidget.autoSelect.isChecked() and not myWidget.testSelect.isChecked():
        # wait recaptcha
        time.sleep(2)

        # tabs from trainNoList1 to submit
        tabs =  (Keys.TAB)*12
        if myWidget.onewaySelect.isChecked():
            trainNoList1.send_keys(tabs + " ")
        else:
            trainNoList2.send_keys(tabs + " ")
            


