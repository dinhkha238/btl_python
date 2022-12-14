# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uiProcessImg.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from turtle import width
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog,QVBoxLayout,QFormLayout,QLineEdit,QDialogButtonBox,QDialog,QApplication
from PyQt5.QtGui import QImage
import cv2, imutils
import numpy as np

# from test import click_event

# from test import click_event

class Dialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        dlgLayout = QVBoxLayout()
        self.formLayout = QFormLayout()
        self.entry1 = QtWidgets.QLineEdit()
        self.formLayout.labelForField(self.entry1)
        self.formLayout.addRow(self.entry1, QtWidgets.QLineEdit())
        
        dlgLayout.addLayout(self.formLayout)
        btns = QDialogButtonBox()
        btns.setStandardButtons(
            QDialogButtonBox.Ok
        )
        dlgLayout.addWidget(btns)
        self.setLayout(dlgLayout)
        btns.accepted.connect(self.accept)   

    def accept(self):
        i, j = self.formLayout.getWidgetPosition(self.entry1)
        widget_item_i = self.formLayout.itemAt(i, j)
        widget_i = widget_item_i.widget()
        widget_item_j = self.formLayout.itemAt(i, j+1)
        widget_j = widget_item_j.widget()
        text_i = widget_i.text()
        text_j = widget_j.text()
        ui.inputSize(text_i,text_j)
        dlg.close()
class Ui_MainWindow(object):
    #----------------------------------------------------------------------
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Cửa sổ ảnh")
        MainWindow.resize(700,700)
        self.window_name = "MainWindow"
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("                                                                                                  NHẬP ẢNH")
        # self.label.setPixmap(QtGui.QPixmap("img/R.jpg"))
        self.label.setStyleSheet("background-color: white; border: 1px solid black;")
        self.label.setObjectName("label")

        self.horizontalLayout_3.addWidget(self.label)
      
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

    #-------------------------------------------------------------------------------------------------------

        self.verticalSlider_3 = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider_3.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_3.setObjectName("verticalSlider_3")
        self.horizontalLayout.addWidget(self.verticalSlider_3)

        self.verticalSlider_2 = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_2.setObjectName("verticalSlider_2")
        self.horizontalLayout.addWidget(self.verticalSlider_2)
        #-------------------------------------------------------------------------------------------------------------

        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.horizontalLayout_3,0, 0, 1, 2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        
        # -----------------------------------button----------------------------------------------------------------------------------

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_4.addWidget(self.pushButton_2)
        self.pushButton_2.setStyleSheet("background-color: lightyellow;")
        

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.pushButton.setStyleSheet("background-color: lightyellow")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_3.setStyleSheet("background-color: lightyellow")

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_4.setStyleSheet("background-color: lightyellow")
        
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        self.pushButton_5.setStyleSheet("background-color: lightyellow")

        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_2.addWidget(self.pushButton_6)
        self.pushButton_6.setStyleSheet("background-color: lightyellow")

        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_2.addWidget(self.pushButton_7)
        self.pushButton_7.setStyleSheet("background-color: lightyellow")

        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_2.addWidget(self.pushButton_8)
        self.pushButton_8.setStyleSheet("background-color: lightyellow")

        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_2.addWidget(self.pushButton_9)
        self.pushButton_9.setStyleSheet("background-color: lightyellow")

        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout_2.addWidget(self.pushButton_10)
        self.pushButton_10.setStyleSheet("background-color: lightyellow")

        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setObjectName("pushButton_11")
        self.horizontalLayout_2.addWidget(self.pushButton_11)
        self.pushButton_11.setStyleSheet("background-color: lightyellow")

        #----------------------------------het phan button -------------------------------------------------------

        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 0, 2, 2)
        
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
    #--------------------------------------sap xep layout -------------------------------------------------------------

        self.retranslateUi(MainWindow)
        self.pushButton_2.clicked.connect(self.loadImage) 
        self.pushButton_3.clicked.connect(self.resizeActive) 
        self.pushButton.clicked.connect(self.savePhoto) 
        self.pushButton_4.clicked.connect(self.cropActive) 
        self.pushButton_6.clicked.connect(self.turnRightActive) 
        self.pushButton_5.clicked.connect(self.turnLeftActive)
        self.pushButton_7.clicked.connect(self.gaussActive)
        self.pushButton_8.clicked.connect(self.noiseActive)
        self.pushButton_9.clicked.connect(self.contrastActive)
        self.pushButton_10.clicked.connect(self.sharpenActive)
        self.pushButton_11.clicked.connect(self.defaultActive)
    
        
#-----------------------------------------------click --------------------------------------------------
        

        self.verticalSlider_3.valueChanged['int'].connect(self.brightness_value)
        self.verticalSlider_2.valueChanged['int'].connect(self.blur_value)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
#----------------------------------kéo thả  ----------------------------------------------------------    
  

    # Add code here
        self.fileName = None    # Tổ chức vị trí địa chỉ của ảnh
        self.tmp = None         # Ảnh tạm thời để trưng bày
        self.bright_value_now = 0   # Cập nhật giá trị độ sáng
        self.blur_value_now = 0     # Cập nhật giá trị độ mờ
        self.angle_value = 0
        self.img_changed = None
        self.default = None

    #--------------------------------------------------------------------setup------------------------------\
    
    def loadImage(self):
        self.fileName = QFileDialog.getOpenFileName(filter="Image (*.*)")[0]
        self.image = cv2.imread(self.fileName)
        # self.image = cv2.resize(self.image,dsize=(900,600))
        self.setPhoto(self.image)
        self.bright_value_now = 0   # Cập nhật giá trị độ sáng
        self.blur_value_now = 0   # Cập nhật giá trị độ mờ
        self.angle_value = 0  
        self.img_changed = self.image
        self.default = self.image
        self.setDefault = self.image
        self.checkBright =1

    #------------------------------------------------------------------load anh -------------------

    def gauss(self,img):
        
        img_canny = cv2.Canny(img,80,80)
        return img_canny
    def gaussActive(self):
        img = self.gauss(self.img_changed)
        self.default = self.gauss(self.default)
        self.img_changed = img
        self.setPhoto(self.img_changed)
        self.checkBright = 0

    #-------------------------------------------------ve vien bang thuat toan gauss------------------------------------

    def Noise(self,img):
        blur = cv2.medianBlur(img,5)
        return blur
    def noiseActive(self):
        img = self.Noise(self.img_changed)
        self.default = self.Noise(self.default)
        self.img_changed = img
        self.setPhoto(self.img_changed)

    #------------------------------------------------khu noise------------------------------------
        
    
    def contrast(self,img):
        new_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        return new_img
    def contrastActive(self):
        img = self.contrast(self.img_changed)
        self.default = self.contrast(self.default)
        self.img_changed = img
        self.setPhoto(self.img_changed)
        self.checkBright = 0

    #----------------------------trang den------------------------------------------------
    
    def sharpen(self,img):
        kernel3 = np.array([[0, -1,  0],
                           [-1,  5, -1],
                            [0, -1,  0]])
        sharp_img = cv2.filter2D(src=img, ddepth=-1, kernel=kernel3)
        return sharp_img
    def sharpenActive(self):
        img = self.sharpen(self.img_changed)
        self.default = self.sharpen(self.default)
        self.img_changed = img
        self.setPhoto(self.img_changed)

    #-----------------------------làm nét-------------------------------------------
    
    def turnRightImage(self,img):
        height, width = img.shape[:2] # lấy kích thước chiều cao và chiều rộng của ảnh
        center = (width/2, height/2)
        self.angle_value = -90
        rotate_matrix = cv2.getRotationMatrix2D(center=center, angle=self.angle_value, scale=1)
        rotated_image = cv2.warpAffine(src=img, M=rotate_matrix, dsize=(width, height))
        return rotated_image
    def turnRightActive(self):
        img = self.turnRightImage(self.img_changed)
        self.default = self.turnRightImage(self.default)
       
        self.img_changed = img
        self.setPhoto(self.img_changed)

    #------------------------------------------------------quay anh trai qua phai--------------------------
    def turnLeftImage(self,img):
        height, width = img.shape[:2] # lấy kích thước chiều cao và chiều rộng của ảnh
        center = (width/2, height/2)
        self.angle_value = 90
        rotate_matrix = cv2.getRotationMatrix2D(center=center, angle=self.angle_value, scale=1)
        rotated_image = cv2.warpAffine(src=img, M=rotate_matrix, dsize=(width, height))
        return rotated_image
    def turnLeftActive(self):
        img = self.turnLeftImage(self.img_changed)
        self.default = self.turnLeftImage(self.default)
        self.img_changed = img
        self.setPhoto(self.img_changed)

    #-----------------------------------xoay anh phai qua trai -------------------------------------------
    # def cropImage(self,img):
    #     img_crop = img[0:400, 0:720]  # [ y1:y2 , x1:x2 ]
    #     return img_crop

    def cropImage(self,img,x1,y1,x2,y2):
        img_crop = img[y1:y2, x1:x2]  # [ y1:y2 , x1:x2 ]
        return img_crop
    def click_event(self,event, x, y, flags, params):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.x1 = x
            self.y1 = y
            print(x, ' ', y)
            
        if event==cv2.EVENT_LBUTTONUP:
            print(x, ' ', y)
            cv2.destroyWindow("image")
            img = self.cropImage(self.img_changed,self.x1,self.y1,x,y)
            self.default = self.cropImage(self.default,self.x1,self.y1,x,y)
            self.img_changed = img
            self.setPhoto(self.img_changed)

    def cropActive(self):
        # img = self.cropImage(self.img_changed)
        # self.default = self.cropImage(self.default)
        # self.img_changed = img
        # self.setPhoto(self.img_changed)
        img = cv2.imread(self.fileName)
        # imgSeted = cv2.resize(img,(640, 640))
        cv2.imshow('image', img)
        cv2.setMouseCallback('image',self.click_event)


    #--------------------------------------------------crop -------------------------------------------------
    

    def resizeImage(self,img,w,h):
        new_width = int(w)  # 800
        new_height = int(h)  # 400
        img_resized = cv2.resize(img, dsize=(new_width, new_height))
        return img_resized

    def resizeActive(self):
        dlg.show()  

    def inputSize(self,width,height):
        img = self.resizeImage(self.img_changed,width,height)
        self.default = self.resizeImage(self.default,width,height)
        self.img_changed = img
        self.setPhoto(self.img_changed)

    #--------------------------------------------------------resize ---------------------------------------------------
    def setPhoto(self, image):
        self.tmp = image
        image = imutils.resize(image,width = 550) #set lại chiều rộng cho ảnh
        frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # convert color từ image sang color_BGR2RGB
        image = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0],QImage.Format_RGB888)
        self.label.setPixmap(QtGui.QPixmap.fromImage(image))
    #----------------------------------------setPhoto-------------------------------------------------------

    def brightness_value(self,value):
        self.bright_value_now = value
        if self.checkBright == 1:
            img = self.changeBrightness(self.default,self.bright_value_now)
            img = self.changeBlur(img,self.blur_value_now)

            self.img_changed = img
            self.setPhoto(img)
        
        
    def changeBrightness(self,img,value):
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsv)
        lim = 255 - value
        v[v > lim] = 255
        v[v <= lim] += value
        final_hsv = cv2.merge((h, s, v))
        img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
        return img

        

    def blur_value(self,value):
        self.blur_value_now = value
        img = self.changeBlur(self.default,self.blur_value_now)
        if self.checkBright == 1:
            img = self.changeBrightness(img,self.bright_value_now)
        
        self.img_changed = img
        self.setPhoto(img)

    def changeBlur(self,img,value):
        kernel_size = (value + 1,value+1)
        img = cv2.blur(img,kernel_size)
        return img
    # 
    def defaultActive(self):
        self.setPhoto(self.setDefault)
        self.bright_value_now = 0   # Cập nhật giá trị độ sáng
        self.blur_value_now = 0   # Cập nhật giá trị độ mờ
        self.angle_value = 0  
        self.img_changed = self.image
        self.default = self.image
        self.setDefault = self.image
        self.checkBright =1
    

    def update(self,img):
        self.setPhoto(img)
        return img

    def savePhoto(self):
        filename = QFileDialog.getSaveFileName(filter="JPG(*.jpg);;PNG(*.png);;TIFF(*.tiff);;BMP(*.bmp)")[0]
        cv2.imwrite(filename,self.tmp)
        print('Image saved as:',filename)

#----------------------------------------name phim ------------------------------------------------------
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "Open"))
        self.pushButton.setText(_translate("MainWindow", "Save"))
        self.pushButton_3.setText(_translate("MainWindow", "Resize"))
        self.pushButton_4.setText(_translate("MainWindow", "Crop"))
        self.pushButton_5.setText(_translate("MainWindow", "Turn left"))
        self.pushButton_6.setText(_translate("MainWindow", "Turn right"))
        self.pushButton_7.setText(_translate("MainWindow", "Vẽ viền"))
        self.pushButton_8.setText(_translate("MainWindow", "Nhiễu"))
        self.pushButton_9.setText(_translate("MainWindow", "Đen trắng"))
        self.pushButton_10.setText(_translate("MainWindow", "Làm nét"))
        self.pushButton_11.setText(_translate("MainWindow", "Mặc định"))

        # self.pushButton_11.setText(_translate("MainWindow", "Làm mờ"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    
    dlg = Dialog()
    
    # cv2.setMouseCallback('image',self.click_event)

	# wait for a key to be pressed to exit
	# cv2.waitKey(0)

	# close the window
	# cv2.destroyAllWindows()
    sys.exit(app.exec_())
