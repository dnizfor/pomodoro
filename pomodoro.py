import sys
import time
import threading

from PyQt5 import QtWidgets ,QtCore,QtGui , QtMultimedia




class Window (QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()
        
    
        
      
        

    def init_ui(self):
        self.pomodoro = QtWidgets.QPushButton("Pomodoro")
        self.sort_break = QtWidgets.QPushButton("Sort Break")

        self.start_stop = QtWidgets.QPushButton("Start") 

        self.m ,self.s = 25,0
        self.time = QtWidgets.QLabel("{} : {}".format(self.m ,self.s))
        self.time.setAlignment(QtCore.Qt.AlignCenter)
       
        self.time.setStyleSheet(' font-size: 30px; ')

        v_box = QtWidgets.QVBoxLayout()
        h_box = QtWidgets.QHBoxLayout()

        h_box.addStretch()
        h_box.addWidget(self.pomodoro)
        h_box.addWidget(self.sort_break)
        h_box.addStretch()

        
        v_box.addLayout(h_box)  
        v_box.addWidget(self.time)
        v_box.addWidget(self.start_stop)
        

        self.setLayout(v_box)

        self.pomodoro.clicked.connect(self.click)     
        self.sort_break.clicked.connect(self.click)  
        self.start_stop.clicked.connect(lambda: threading.Thread(target=self.click).start())  

 

        self.show()
        
    def click(self):

        sender = self.sender()

        if sender.text() == "Pomodoro":   
            self.m = 25
            self.s = 0
            self.time.setText("{} : {}".format(self.m,self.s))

        elif sender.text() == "Sort Break":   
            self.m = 5
            self.s = 0
            self.time.setText("{} : {}".format(self.m,self.s))
        
        elif sender.text() == "Start" or "Stop" :   

            if self.start_stop.text() == "Start" :
                self.start_stop.setText("Stop")    
                self.timer()

            else :
                self.start_stop.setText("Start")

        

    def timer(self): 
        
           
        while self.start_stop.text() == "Stop" :
            if self.s <= 0 :
                self.m -= 1
                self.s = 60
            self.s -= 1
               
            self.time.setText("{} : {}".format(self.m,self.s))
            time.sleep(1)

            if self.s == 0 and self.m == 0 :
                         
                break
            
         

            
    


def pomo() :
    app = QtWidgets.QApplication(sys.argv)

    window = Window()
    window.setWindowTitle("Pomodoro")
    window.setWindowIcon(QtGui.QIcon("/media/pomo_ico.png"))
    window.setFixedSize(200,100)
    window.setStyleSheet("background-color :red")

 
    

    app.exec_()

pomo()




print("hadi")



       