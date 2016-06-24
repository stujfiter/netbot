import web
import RPi.GPIO as GPIO
import time
from index import index
from rrb2 import *

#GPIO.setmode(GPIO.BCM)
rr = RRB2()
led = 18

render = web.template.render('templates/')

urls = (
    '/led', 'blink',
    '/forward', 'forward',
    '/reverse', 'reverse',
    '/right', 'right',
    '/left', 'left',
    '/', 'home',
    '/(.*)', 'index'
)
app = web.application(urls, globals())

class blink:        
    def GET(self):
        GPIO.setup(led, GPIO.OUT)
        GPIO.output(led, 1)
        time.sleep(1)
        GPIO.output(led, 0)
        GPIO.cleanup()

        web.header('cache-control', 'private, max-age=0, no-cache', unique=True)
        return 'LED Working!'

class forward:
    def GET(self):
        rr.forward(1,1)

class reverse:
    def GET(self):
        rr.reverse(1,1)

class right:
    def GET(self):
        rr.right(1,1)

class left:
    def GET(self):
        rr.left(1,1)

if __name__ == "__main__":
    app.run()
