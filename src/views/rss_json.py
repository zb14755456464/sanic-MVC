
from sanic import Blueprint
from sanic.response import html, json

json_bp = Blueprint('rss_json', url_prefix='json')

@json_bp.route("/")
async def index(request):
    return json({'name':'zhangbiao'})
