import json


def save_data(myWidget):
    data = []
    with open("save.json", "r") as f:
        data = json.load(f)

    data.update({"browser": myWidget.browser.currentText()})
    data.update({"idCard": myWidget.idCard.text()})
    data.update({"startStation": myWidget.startStation.text()})
    data.update({"endStation": myWidget.endStation.text()})
    data.update({"onewaySelect": myWidget.onewaySelect.isChecked()})
    data.update({"roundtripSelect": myWidget.roundtripSelect.isChecked()})
    data.update({"ticketNum": myWidget.ticketNum.text()})
    data.update({"date1": myWidget.date1.text()})
    data.update({"trainNumber1": myWidget.trainNumber1.text()})
    data.update({"date2": myWidget.date2.text()})
    data.update({"trainNumber2": myWidget.trainNumber2.text()})
    data.update({"testSelect": myWidget.testSelect.isChecked()})
    data.update({"autoSelect": myWidget.autoSelect.isChecked()})    

    with open("save.json", "w") as f:    
        json.dump(data, f, ensure_ascii=False)

def load_data(myWidget):
    data = []
    with open("save.json", "r") as f:
        data = json.load(f)
    
    if "browser" in data:
        myWidget.browser.setCurrentText(data["browser"])
    if "idCard" in data:
        myWidget.idCard.setText(data["idCard"])
    if "startStation" in data:
        myWidget.startStation.setText(data["startStation"])
    if "endStation" in data:
        myWidget.endStation.setText(data["endStation"])
    if "onewaySelect" in data:
        myWidget.onewaySelect.setChecked(data["onewaySelect"])
    if "roundtripSelect" in data:
        myWidget.roundtripSelect.setChecked(data["roundtripSelect"])
    if "ticketNum" in data:
        myWidget.ticketNum.setText(data["ticketNum"])
    if "date1" in data:
        myWidget.date1.setText(data["date1"])
    if "trainNumber1" in data:
        myWidget.trainNumber1.setText(data["trainNumber1"])
    if "date2" in data:
        myWidget.date2.setText(data["date2"])
    if "trainNumber2" in data:
        myWidget.trainNumber2.setText(data["trainNumber2"])
    if "testSelect" in data:
        myWidget.testSelect.setChecked(data["testSelect"])
    if "autoSelect" in data:
        myWidget.autoSelect.setChecked(data["autoSelect"])
    

