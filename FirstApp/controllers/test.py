# -*- coding: utf-8 -*-
# try something like
def index():
    import cgi
    x = request.vars
    return "<html><body><h1> %s </h1></body></html>" %cgi.escape(str(x))
