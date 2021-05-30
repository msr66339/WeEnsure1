import smtplib


class mail:
    def __init__(self,address,report):
        self.report=report
        self.address=address
        self.server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        self.server.login("wiiensure@gmail.com", "we@12345")
        self.sendmail()

    def sendmail(self):

        self.server.sendmail("wiiensure@gmail.com",self.address,"The report for the mask violaton"
                                                                     "\n"
                                                                     "Name: " + self.report["name"]+
                                                                    "\n"
                                                                        "Fathers Name: "+self.report["FathersName"]+
                                                                    "\n"
                                                                        "Registration: "+self.report["registration"]+
                                                                    "\n"
                                                                        "Section: "+self.report["section"]+
                                                                    "\n"
                                                                        "Location: "+self.report["Location"])