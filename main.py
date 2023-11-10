import manage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ex
import time
import os
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5 import uic
from threading import Thread
from PyQt5.QtCore import QThread, pyqtSignal, QObject
from selenium.webdriver.firefox.options import Options



class SearchThread(QThread):
    search_complete = pyqtSignal(str)
    
    def __init__(self, text):
        super().__init__()
        self.text = text
        
    def run(self):
        options = Options()
        options.add_argument('-headless')
        driver = webdriver.Firefox(options=options)
<<<<<<< HEAD
        driver.get('https://digimovie52.pw/')
        
        result = ""
        substring = self.text.split('-')
        for i in substring:
            try:
=======
        driver.get('https://digimovie.vip/')

        result = ""
        substring = self.text.split('-')
        for i in substring:
           try:
>>>>>>> f0260ea4111f9937a2602fe1f1c95de4f23faa22
                search = i.capitalize()
                WebDriverWait(driver, 5).until(ex.presence_of_element_located((By.XPATH , '/html/body/div/div/header/div[3]/div/div/div[2]/form/input'))).send_keys(search + Keys.ENTER)
                WebDriverWait(driver, 5).until(ex.presence_of_element_located((By.PARTIAL_LINK_TEXT , search))).click()
                os.system('cls')
                imdb = WebDriverWait(driver, 5).until(ex.presence_of_element_located((By.CSS_SELECTOR, '.num_holder > strong'))).text
                WebDriverWait(driver, 5).until(ex.presence_of_element_located((By.XPATH, '//*[@id="accordion-group--0__accordion-btn--1"]'))).click()
                time.sleep(3)
                actor1 = driver.find_element(By.CSS_SELECTOR,'div.slick-current:nth-child(9) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1) > div:nth-child(2) > h3:nth-child(1)').text
                actor2 = driver.find_element(By.CSS_SELECTOR,'div.slick-active:nth-child(10) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1) > div:nth-child(2) > h3:nth-child(1)').text
                actor3 = driver.find_element(By.CSS_SELECTOR,'div.slick-active:nth-child(11) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1) > div:nth-child(2) > h3:nth-child(1)').text
                result += f'name: {search}\n'
                result += f'imdb: {imdb}\n'
                result += f'actor1: {actor1}\n'
                result += f'actor2: {actor2}\n'
                result += f'actor3: {actor3}\n'
                result += '----------------------\n'
<<<<<<< HEAD
            except Exception:
                result += f'Not Found\n'
=======
           except Exception:
            result += f'Not Found\n'

>>>>>>> f0260ea4111f9937a2602fe1f1c95de4f23faa22
        driver.quit()
        self.search_complete.emit(result)       
        
class CornometerThread(QThread):
    update_lcd = pyqtSignal(float)
    
    def __init__(self):
        super().__init__()
        self._stop_event = False
    
    def run(self):
        start_time = time.time()
        while not self._stop_event:
            elapsed_time = time.time() - start_time
            self.update_lcd.emit(elapsed_time)
            time.sleep(0.1)
    
    def stop(self):
        self._stop_event = True


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("view.ui",self)
        self.btnSearch.clicked.connect(self.start_search)
        
        self.lcdNumber.setDigitCount(5)
        
    def start_search(self):
        text = self.txtmovie.text()
        self.txtOutput.setPlainText('Please Wait...\n')
        self.thread = SearchThread(text)
        self.thread.search_complete.connect(self.display_result)
        

        # self.cornometer_thread = CornometerThread()
        # self.cornometer_thread.update_lcd.connect(self.update_lcd_display)
        # self.cornometer_thread.start()
        
        self.thread.start()
        
    def update_lcd_display(self, elapsed_time):
        self.lcdNumber.display("{:.1f}".format(elapsed_time))

    def display_result(self, result):
        self.txtOutput.setPlainText(result)
        self.cornometer_thread.stop()
        self.cornometer_thread.wait()
<<<<<<< HEAD
        
        
=======
>>>>>>> f0260ea4111f9937a2602fe1f1c95de4f23faa22

if __name__ == '__main__':
    manage.starter()
    print('ok')
    # Create the QApplication
    app = QApplication([])

    # Create the Window
    window = Window()
    window.show()

    # Run the event loop
    app.exec_()
