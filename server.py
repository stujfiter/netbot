import web
import RPi.GPIO as GPIO
import time
from index import index

GPIO.setmode(GPIO.BCM)
led = 18

render = web.template.render('templates/')

urls = (
    '/led', 'blink',
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

if __name__ == "__main__":
    app.run()
