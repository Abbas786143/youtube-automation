from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time
import string
import pyautogui
import urllib.request
from selenium.webdriver.chrome.options import Options
from PIL import Image
from pathlib import Path
urllist=[]
import os
import csv
import pyautogui

dir_path = "videos"

# list to store files
res = []
videoname=[]
i=0
# Iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        res.append(path)

import pandas as pd
chrome_options = Options()
chrome_options.add_argument("--user-data-dir=../googleProfile")
chrome_options.add_argument("--remote-debugging-port=9222")

browser = uc.Chrome(use_subprocess=True,options=chrome_options)
for name in res:
    print(name)
    browser.get("https://www.youtube.com/channel/UC_K98JQpIgISWoI-aXR2INQ")
    # implicit wait for 5 seconds
    browser.implicitly_wait(5)
    # maximize with maximize_window() 
    browser.maximize_window()

    uploadbtn=browser.find_element(by=By.XPATH,value='/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[3]/div[2]/ytd-topbar-menu-button-renderer[1]/div/a/yt-icon-button/button/yt-icon')
    browser.execute_script("arguments[0].click();", uploadbtn)
    uploadbtn2=browser.find_element(by=By.XPATH,value='/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer/div[2]/ytd-compact-link-renderer[1]/a/tp-yt-paper-item/div[2]/yt-formatted-string[1]')
    browser.execute_script("arguments[0].click();", uploadbtn2)
    
    filename =os.path.realpath("videos/"+name)
    
    pictureupload=browser.find_element(by=By.XPATH, value='/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-uploads-file-picker/div/input')
                                                 
    pictureupload.send_keys(filename)
    uploadbtn3=browser.find_element(by=By.XPATH,value='/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[5]/ytkc-made-for-kids-select/div[4]/tp-yt-paper-radio-group/tp-yt-paper-radio-button[1]/div[1]')
    browser.execute_script("arguments[0].click();", uploadbtn3)

    time.sleep(5)
    uploadbtn4=browser.find_element(by=By.XPATH,value='/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[2]/div/div[2]/ytcp-button[2]')
    browser.execute_script("arguments[0].click();", uploadbtn4)

    uploadbtn5=browser.find_element(by=By.XPATH,value='/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[2]/div/div[2]/ytcp-button[2]')
    browser.execute_script("arguments[0].click();", uploadbtn5)
    
    uploadbtn6=browser.find_element(by=By.XPATH,value='/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[2]/div/div[2]/ytcp-button[2]')
    browser.execute_script("arguments[0].click();", uploadbtn6)

    uploadbtn7=browser.find_element(by=By.XPATH,value='/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[2]/div/div[2]/ytcp-button[2]')
    browser.execute_script("arguments[0].click();", uploadbtn7)    

    
    uploadbtn8=browser.find_element(by=By.XPATH,value='/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-uploads-review/div[2]/div[1]/ytcp-video-visibility-select/div[2]/tp-yt-paper-radio-group/tp-yt-paper-radio-button[3]/div[1]/div[1]')
    browser.execute_script("arguments[0].click();", uploadbtn8)    

    


    uploadbtn9=browser.find_element(by=By.XPATH,value='/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[2]/div/div[2]/ytcp-button[3]')
    browser.execute_script("arguments[0].click();", uploadbtn9)



