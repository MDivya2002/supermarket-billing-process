from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import *
import sys
from BillingAppUI import *


class Naveen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.billB.clicked.connect(self.bill)
        self.ui.resetB.clicked.connect(self.reset)
        self.ui.exitB.clicked.connect(self.exit)
    def bill(self):
        paniPuri= int(self.ui.pp.text())*20
        sevPuri = int(self.ui.sp.text())*40
        dahiPuri =  int(self.ui.dp.text())*30
        bhelPuri =  int(self.ui.bp.text())*20
        masalaPuri =  int(self.ui.mp.text())*30
        aaluPuri =  int(self.ui.ap.text())*40
        cutlet =  int(self.ui.ct.text())*40
        gobi =  int(self.ui.gm.text())*50
        samosaFry =  int(self.ui.sf.text())*50
        ragada =  int(self.ui.rg.text())*40
        dahiPapad =  int(self.ui.dpp.text())*30
        kachori =  int(self.ui.kch.text())*20
        coolDrinks =  int(self.ui.cd.text())*20

        bill = paniPuri+sevPuri+dahiPuri+bhelPuri+masalaPuri+aaluPuri+cutlet+gobi+samosaFry+ragada+dahiPapad+kachori+coolDrinks
        sgst = bill*0.045
        cgst = bill*0.045
        totBill= bill+sgst+cgst
        self.ui.label_17.setText(str(bill))
        self.ui.label_18.setText("{:.2f}".format(sgst))
        self.ui.label_20.setText("{:.2f}".format(cgst))
        self.ui.label_22.setText("{:.2f}".format(totBill))
        
    
    def reset(self):
        self.ui.pp.setText("0")
        self.ui.sp.setText("0")
        self.ui.dp.setText("0")
        self.ui.bp.setText("0")
        self.ui.mp.setText("0")
        self.ui.ap.setText("0")
        self.ui.ct.setText("0")
        self.ui.gm.setText("0")
        self.ui.sf.setText("0")
        self.ui.rg.setText("0")
        self.ui.dpp.setText("0")
        self.ui.kch.setText("0")
        self.ui.cd.setText("0")
        self.ui.label_17.clear()
        self.ui.label_18.clear()
        self.ui.label_20.clear()
        self.ui.label_22.clear()

        
        
        
    def exit(self):
        sys.exit()
        


if __name__=="__main__":
    app = QApplication(sys.argv)
    w = Naveen()
    w.show()
    sys.exit(app.exec_())

