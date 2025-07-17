from lsm6ds3 import LSM6DS3
import time
import RPi.GPIO as GPIO
import datetime
import csv

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
    writer = csv.writer(file)
    writer.writerow([data[0], data[1], data[2], data[3], data[4]])

def main():
  # Ask for FileNames
  file_dict = str(input("Enter the motion name for data storage: "))
  filename = str(input("Enter the filename for data storage: "))

  #Initialize GPIO
  global lsm
  lsm = LSM6DS3()

  # Initialize GPIO for button
  button = 17
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(button, GPIO.IN)
  
  #Button setup
  toggle_state = False
  last_state = GPIO.input(button)

  while True:
    current_state = GPIO.input(button)
    
    if last_state == True and current_state == False:
      toggle_state = not toggle_state
      if toggle_state == True:
        print("Recording data")
      else:
        print("Data off")
      
    last_state = current_state
    
    if toggle_state == True:
      ax, ay, az = read_acc()
      date = datetime.datetime.now()
      data = [date, ax, ay, az, file_dict]
      time.sleep(0.02)
      
      write_to_csv(filename, file_dict, data)

main()
