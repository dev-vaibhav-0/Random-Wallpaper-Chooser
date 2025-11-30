# 🖼️ Random Wallpaper Chooser

A tiny Python script that grabs a random wallpaper from a website and lets you the option to do whatever with the file. No schedules, no cronjobs — pure chaos, pure vibes.

## 🚀 Features
- Picks **one random wallpaper** from a website 
- Works on **every OS**  
- Zero dependencies  
- Instant refresh when you're bored of your wallpaper

## 📦 Requirements
- Python 3.x
- Required Library
- Driver for your browser, for example — Firefox has it's own driver called Geckodriver
 
## 🛠️ Install
```bash
git clone https://github.com/dev-vaibhav-0/Random-Wallpaper-Chooser
cd Random-Wallpaper-Chooser
pip install -r requirements.txt
```
Be sure to change the path of the driver if its not in /usr/local/bin.

## 🚀 Run

Supported browsers are Safari,Chrome,Firefox and Edge and are given names for their .py files for easier understanding. You can also change the file path accordingly although it is recommended for Linux to put the driver in /usr/local/bin.

```bash
python <browser>.py
```
## Links
- Chrome Driver: https://developer.chrome.com/docs/chromedriver/downloads
- Gecko Driver: https://github.com/mozilla/geckodriver/releases
- Edge Driver: https://github.com/MicrosoftEdge/EdgeWebDriver
- Safari Driver: Safari and Safari Technology Preview each provide their own safaridriver executable. Make sure you already have the executable on your device: Safari’s executable is located at /usr/bin/safaridriver.
