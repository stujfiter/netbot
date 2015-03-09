import web
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
led = 18

render = web.template.render('templates/')
        
urls = (
    '/netbot', 'netbot',
    '/(.*)', 'hello'
)
app = web.application(urls, globals())

class hello:        
    def GET(self, name):
	if not name:
            GPIO.setup(led, GPIO.OUT)
            GPIO.output(led, 1)
            time.sleep(5)
            GPIO.output(led, 0)
            GPIO.cleanup()

        return 'LED Working!'

class netbot:
    def GET(self):
        return render.netbot()

if __name__ == "__main__":
    app.run()
