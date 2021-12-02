import sys
import PyQt5
#Widget Library
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
#Web Engine
from PyQt5.QtWebEngineWidgets import *

#Main Window
class MainWindow(QMainWindow):
	def __init__(self):
		#Inherit from QMainWindow
		super(MainWindow, self).__init__()
		#Window Icon
		self.setWindowIcon(QIcon('Nano.png'))		
		#Browser
		self.browser = QWebEngineView()					
		self.browser.setUrl(QUrl('http://nanotechnologies.site'))		#Default Website
		self.setCentralWidget(self.browser)					#Sets Browser as Central Widget
		self.showMaximized()								#Maximises Window
		#Navigation Bar
		navbar = QToolBar()
		self.addToolBar(navbar)								#Set Class Toolbar
		#Back Button
		back_button = QAction('Back',self)						
		back_button.triggered.connect(self.browser.back)	#When Back Button Triggered,Connect to Browser and Go Back
		navbar.addAction(back_button)						#Add Back Button to Navbar
		#Forward Button
		forward_button = QAction('Forward',self)						
		forward_button.triggered.connect(self.browser.forward)	
		navbar.addAction(forward_button)						
		#Reload Button
		reload_button = QAction('Reload',self)						
		reload_button.triggered.connect(self.browser.reload)	
		navbar.addAction(reload_button)	
		#Home Button
		home_button = QAction('Home',self)						
		home_button.triggered.connect(self.navigate_home)	
		navbar.addAction(home_button)		
		#Url Line Editor
		self.url_bar = QLineEdit()
		self.url_bar.returnPressed.connect(self.navigate_to_url)	#When Return Key Pressed,Connect to Url of Called Function
		navbar.addWidget(self.url_bar)								#Add Line Editor Widget to Navbar
		self.browser.urlChanged.connect(self.update_url)			#When Url changes, Connect to Url of Called Function

	#Home Page
	def navigate_home(self):
		self.browser.setUrl(QUrl('http://google.com'))				#Takes Browser to Url

	#Navigate Url
	def navigate_to_url(self):
		url = self.url_bar.text()									#Get the URL from Line Editor
		self.browser.setUrl(QUrl(url))								#Takes Browser to Url

	#Update Url
	def update_url(self, newurl):
		self.url_bar.setText(newurl.toString())						#Updates Line Text to NewUrl

#Instance of QApplication Class
app = QApplication(sys.argv)
QApplication.setApplicationName('Nano Browser')
#Instance of Window Class 
window = MainWindow()
app.exec_()
