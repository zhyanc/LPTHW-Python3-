
import web
from flask import request

urls = (
    '/', 'index'
)

app = web.application(urls, globals())

class index:
    def GET(self):
        greeting  = "hello world"
        # return greeting
        return render.index(greeting = greeting)

render = web.template.render('templates/')

if __name__ == "__main__":
    app.run()
