import RPi.GPIO as GPIO
import time
from picamera import PiCamera
camera = PiCamera()


import json
from watson_developer_cloud import VisualRecognitionV3

visual_recognition = VisualRecognitionV3(
    '2018-03-19',
    iam_apikey='f_Vj9MUo2GC2pKJO1FNHcIBaXaMXOCYcNSpW1zf98rZT')

sensor = 16
red = 18
blue = 15
green = 13

GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor,GPIO.IN)
GPIO.setup(red,GPIO.OUT)
GPIO.setup(blue,GPIO.OUT)
GPIO.setup(green,GPIO.OUT)

GPIO.output(red,False)
GPIO.output(blue,False)
GPIO.output(green),False)

try: 
   while True:
      if GPIO.input(sensor):
          #GPIO.output(buzzer,True)
          print("Box Detected")
          camera.start_preview()
          time.sleep(0.5)
          camera.capture('/home/pi/Color_based_object_sort/robotics/cap_images/image.jpg')
          camera.stop_preview()
          with open('/home/pi/Color_based_object_sort/robotics/cap_images/image.jpg', 'rb') as images_file:
            classes = visual_recognition.classify(
                images_file,
                threshold='0.6',
            classifier_ids='DefaultCustomModel_1218215954').get_result()
          print(json.dumps(classes, indent=2))

          Class = json.dumps(classes['images'][0]['classifiers'][0]['classes'][0]['class'])
          prob = json.dumps(classes['images'][0]['classifiers'][0]['classes'][0]['score'])
          print(Class,prob)

          if(prob>0.6):
              if(Class=="red_box"):
                  GPIO.output(red,True)
                  time.sleep(2)
                  GPIO.output(red,False)
              if(Class=="blue_box"):
                  GPIO.output(blue,True)
                  time.sleep(2)
                  GPIO.output(blue,False)
              if(Class=="green_box"):
                  GPIO.output(green,True)
                  time.sleep(2)
                  GPIO.output(green,False)
          while GPIO.input(sensor):
              time.sleep(0.2)


except KeyboardInterrupt:
    GPIO.cleanup()
