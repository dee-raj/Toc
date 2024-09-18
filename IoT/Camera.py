import piCamera as pCam
from time import sleep
camera = pCam.piCamera()
camera.start_preview()
sleep(5)
camera.capture('image.jpg')
camera.stop_preview()

"""
With labled Image
import piCamera
from time import sleep
camera = piCamera.piCamera()
camera.start_preView()
sleep(5)
camera.annotate_text='this image is taken from Raspberrypi'
camera.capture('image_with_text.jpg')
camera.stop_preview()
"""