import sys

class Report:
    def __init__(self):
        self.reportss=[{"id":1,"name":"Moeez","FathersName":"Sajid","registration":"sp1000","section":"B","Location":"Cafe","type":"mis","img":"D:\dd.jpg"},
                  {"id": 2, "name": "Moosa", "FathersName": "Shahid","registration":"sp1000", "section": "B", "Location": "Cafe", "type": "mis","img":"D:\db.jpg"},
                  {"id": 3, "name": "moeez", "FathersName": "Sajid","registration":"sp1000", "section": "B", "Location": "Cafe", "type": "all","img":"D:\dd.jpg"},
                  {"id": 4, "name": "Moosa", "FathersName": "Shahid","registration":"sp1000", "section": "B", "Location": "Cafe", "type": "mis","img":"D:\db.jpg"},
                  {"id": 5, "name": "Moeez", "FathersName": "Sajid","registration":"sp1000", "section": "B", "Location": "Cafe", "type": "all","img":"D:\dd.jpg"},
                  {"id": 6, "name": "moosa", "FathersName": "Shahid","registration":"sp1000", "section": "B", "Location": "Cafe", "type": "all","img":"D:\db.jpg"}
                  ]
        self.id=self.setId

    def setId(self):
        return 7

    def addMissedReport(self,name="no name",reg="no",fname="no",sec="no",loc="no"):
        self.reportss.append({"id": self.id, "name": name, "FathersName": fname, "section": sec, "Location": loc, "type": "mis"})
        id=id+1

    def addALLReport(self,name="no name",reg="no",fname="no",sec="no",loc="no"):
        self.reportss.append({"id": self.id, "name": name, "FathersName": fname,"registration":reg, "section": sec, "Location": loc, "type": "all"})
        id=id+1

    def deleteReport(self,lid):
        for i in range(len(self.reportss)):
            if self.reportss[i]['id'] == lid:
                self.reportss.pop(i)
                break

