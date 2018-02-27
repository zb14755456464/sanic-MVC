from sanic import Sanic
from config import CONFIG
from utils.sanic_jinja2 import SanicJinja2
from views import html_bp,json_bp
import os


'''可以在工具中封装好一个模板，直接调用即可'''
print(SanicJinja2)

app = Sanic(__name__)
app.blueprint(json_bp)
app.blueprint(html_bp)
app.config.from_object(CONFIG)

# 配置静态路径
app.static('/statics',os.path.join(CONFIG.BASE_DIR,'static'))
jinjia = SanicJinja2(app)

@app.route('/')
async def index(request):
    context = {'name':'zhangbiao' ,"greetings":'Hello, sanic!'}
    return jinjia.render('index/index.html', request, **context)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000,debug=CONFIG.DEBUG)