#!/usr/bin/env python
import sys
from sanic import Blueprint
from sanic.response import text

html_bp = Blueprint('rss_html', url_prefix='html')

@html_bp.route("/index")
async def rss_html(request):

    return text('hello')
