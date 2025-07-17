from lsm6ds3 import LSM6DS3
import time
import RPi.GPIO as GPIO

def read_acc(sent=0.00061):
  ax, ay, az, gx, gy, gz = lsm.get_readings()
  ax = ax * sent
  ay = ay * sent
  az = az * sent

  return ax, ay, az

def write_to_csv(filename, file_dict, data):
  file_folder = "data"
  file_path = f"{file_folder}/{file_dict}/{filename}"

  with open(file_path, 'a') as file:
    file.write(data)

def main():
  # Ask for FileNames
  file_dict = str(input("Enter the folder name for data storage: "))
  filename = str(input("Enter the filename for data storage: "))

  #Initialize GPIO
  global lsm
  lsm = LSM6DS3()

  # Initialize GPIO for button
  button = 17
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(button, GPIO.IN)

  lever = GPIO.input(button)

  while lever :
    ax, ay, az = read_acc()