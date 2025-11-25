import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium import webdriver

s = Service('/usr/local/bin/geckodriver')
driver = webdriver.Firefox(service=s)

class Main:
    def __init__(self,height,width):
        self.height = height
        self.width = width
        choice = (int(input("""Choose today's style (input eg. 1 )):
            1) Grayscale Wallpaper
            2) Blurred Wallpaper
            3) Grayscale & Blurred Wallpaper
            4) Normal Square Wallpaper
            --> """)))
        if choice:
            print(self.perform_grayscale())
        elif choice == 2:
            print(self.perform_blur())
        elif choice == 3:
            print(self.perform_grayscale_and_blur())
        elif choice == 4:
            print(self.perform_normal())
        else:
            print("Choose between 1 to 4")

    def perform_grayscale(self):
        driver.get(f'https://picsum.photos/{self.width}/{self.height}?grayscale')
    def perform_blur(self):
        try:
            blur = int(input("Amount of blur (1-10)"))
            if blur in range(1,11):
                print(f"Amount {blur} has been chosen")
            else:
                print("Please choose between 1 to 10")
        except TypeError as e:
            print(f"Please input an integer: {e}")
        except Exception as e:
            print(f"An error occured: {e}")
        else:
            driver.get(f'https://picsum.photos/{self.width}/{self.height}/?blur={blur}')
    def perform_grayscale_and_blur(self):
        try:
            blur = int(input("Amount of blur (1-10)"))
            if blur in range(1,11):
                print(f"Amount {blur} has been chosen")
            else:
                print("Please choose between 1 to 10")

        except TypeError as e:
            print(f"Please input an integer: {e}")
        except Exception as e:
            print(f"An error occured: {e}")
        else:
            driver.get(f'https://picsum.photos/{self.width}/{self.height}/?grayscale&blur={blur}')

    def perform_normal(self):
        driver.get(f'https://picsum.photos/{self.height}')

        

width = int(input("Enter the width of the Wallpaper -->")) 
height = int(input("Enter the height of the Wallpaper -->")) 

run = Main(width=width,height=height)
if __name__ == "__main__":
    print(run)
