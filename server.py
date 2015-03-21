import web
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
led = 18

render = web.template.render('templates/')
        
urls = (
    '/led', 'blink',
    '/', 'index'
)
app = web.application(urls, globals())

class blink:        
    def GET(self):
        GPIO.setup(led, GPIO.OUT)
        GPIO.output(led, 1)
        time.sleep(1)
        GPIO.output(led, 0)
        GPIO.cleanup()

        return 'LED Working!'

class index:
    def GET(self):
        return render.netbot()

if __name__ == "__main__":
    app.run()
