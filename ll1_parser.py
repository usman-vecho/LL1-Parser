import matplotlib.pyplot as plt
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

tab=dict()

#Grammer
'''
tab["S->iEtSS'"] =  "i"
tab["S->a"] =  "a"
tab["S'->eS"] = "e"  
tab["S'->ϵ"]  = 'ϵ'
tab['E->b'] = 'b'
'''
tab['E->T Er'] = ['E','id']
tab['ER->+ T ER'] = ['ER','+']
tab['ER->ϵ'] = ['ER','$']
tab['T->F TR'] = ['T','id']
tab['TR->* F TR'] = ['TR','*']
tab['TR->ϵ'] = ['TR','$']
tab['F->( E )'] = ['F','(']
tab['F->id'] = ['F','id']

non_terminals,firsts,keys = list() , list() , list()
for i,j in tab.items():
    keys.append(i)
    i = i.split('->')
    i = i[0]
    if j not in firsts:
        if j=='ϵ':
            pass
        else:
            firsts.append(j)
    if i not in non_terminals:
        non_terminals.append(i)
#firsts.append('$')
#non_terminals.insert(0,'')z
#firsts.insert(0,'')
#[print(i,end = "   ") for i in firsts]
#[print(i) for i in non_terminals]
print(non_terminals)
final_result = []
firsts_ = firsts
for i in range(len(non_terminals)):
    for k in range(len(firsts_)):
        first_latter_of_key = keys[k].split('->')
        first_latter_of_key = first_latter_of_key[0]

        #if first_latter_of_key==non_terminals[i]:
        #    if last_latter_of_key == 'ϵ':
        #        pass
        #    else:
        final_result.append((non_terminals.index(non_terminals[i]), firsts_.index(firsts_[k] ) ,keys[k]))
print(final_result)
class App(QWidget):
    def __init__(self,final_result,firsts,non_terminals):
        super().__init__()
        self.title = 'Lab Assignment -017 vecho'
        self.left = 0
        self.top = 0
        self.width = 630
        self.height = 170
        self.initUI()
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.createTable()
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget) 
        self.setLayout(self.layout) 
        self.show()
    def createTable(self):
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(len(non_terminals))
        self.tableWidget.setColumnCount(len(firsts))
        self.tableWidget.verticalHeader().setVisible(True);
        self.tableWidget.horizontalHeader().setVisible(True);
        self.tableWidget.setHorizontalHeaderLabels(firsts)
        self.tableWidget.setVerticalHeaderLabels(non_terminals)
        for i in range(len(firsts)):
            self.tableWidget.setItem(0,i, QTableWidgetItem(firsts[i]))
        for i in range(len(non_terminals)):
            self.tableWidget.setItem(i,0, QTableWidgetItem(non_terminals[i]))
        for i in final_result:
            fp   = i[0]
            sp   = i[1]
            item = i[2]
            self.tableWidget.setItem(fp,sp, QTableWidgetItem("{} {}{}".format(item,'','')))#fp,sp-1
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App(final_result,firsts,non_terminals)
    sys.exit(app.exec_())
