from sanic.views import HTTPMethodView
from sanic.response import text
from utils.sanic_jinja2 import SanicJinja2
from sanic import Sanic
from urllib.parse import parse_qs
from database import MotorBase

try:
    from ujson import dumps as json_dumps
except:
    from json import dumps as json_dumps

app = Sanic()
jinjia = SanicJinja2(app)


@app.listener('before_server_start')
def setup_db(operate_bp, loop):
    global motor_base
    motor_base = MotorBase()


@app.listener('after_server_stop')
def close_connection(operate_bp, loop):
    motor_base = None


class SimpleView(HTTPMethodView):

    async def get(self, request):
        return jinjia.render('form.html', request)

    async def post(self, request):
        data = parse_qs(request.body.decode())
        # data = str(request.body) 这个时候接受的是一个字符串类型
        # name=data.get('name')

        name = data.get('name')

        mobile = data.get('mobile')
        pwd = data.get('pwd')

        motor_db = motor_base.get_db()
        data = {
            "name": name,
            "password": pwd,
            "mobile": mobile,
        }

        motor_db = motor_base.get_db()

        # result=motor_db.user.insert(data)
        # 注意这里要是不加上异步的语法，async是查询不出来结果的
        data = await motor_db.user.find_one({'name': name})
        print(type(data))
        print(data.get('name'))
        return text(data)


app.add_route(SimpleView.as_view(), '/')

if __name__ == '__main__':
    app.run()
