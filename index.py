import web

render = web.template.render('templates/')

class index:
    def GET(self, passwd):
        f = open("secret")
        secret = f.readline().strip()
        f.close()

        if passwd == secret:
            return render.netbot()
        else:
            return render.denied()
