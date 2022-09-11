import webbrowser
import os
from filestack import Client

from fpdf import FPDF


class PdfReport:
    """
    Creates a pdf report about thr flatmates such as their names , their due amount and the period of the Bill
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pdf = FPDF(orientation='P', unit='pt', format='A4')

        pdf.add_page()
        pdf.image('flatmates_bill/img.png',w=30,h=30)
        pdf.set_font(family="Times", size=24, style='B')
        pdf.cell(w=0, h=80, txt='Flatmates Bill', border=1, align='C', ln=1)
        pdf.cell(w=100, h=40, txt='Period', border=1)
        pdf.cell(w=150, h=40, txt=bill.period, border=1, ln=1)


        pdf.set_font(family="Times", size=12)
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=25, txt=str(round(flatmate1.pays(bill,flatmate2),2)), border=0, ln=1)

        pdf.set_font(family="Times", size=12)
        pdf.cell(w=100, h=25, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=25, txt=str(round(flatmate2.pays(bill,flatmate1),2)), border=0, ln=1)

        os.chdir("files")
        pdf.output(self.filename)

        webbrowser.open(self.filename)

class FileSharer:

    def __init__(self,filepath,api_key='ABwmYTz4PSyyt400jwcycz'):
        self.filepath = filepath
        self.api_key=api_key

    def share(self):
        client=Client(self.api_key)
        new_filelink =client.upload(filepath=self.filepath)
        return new_filelink.url