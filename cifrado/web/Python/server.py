# -*- coding: <UTF-8> -*-

from Cifrar import Cifrar
from AlfabetoMin import AlfabetoMin
from AlfabetoMay import AlfabetoMay
from Separar import Separar
import os, os.path
import random
import string
import simplejson as json


import cherrypy


class StringGenerator(object):
    @cherrypy.expose
    def index(self):
        return open('index.html')


@cherrypy.expose
class StringGeneratorWebService(object):

    @cherrypy.tools.accept(media='text/plain')
    def GET(self):
        return cherrypy.session['mystring']

    def POST(self, text, displacement, groups):
        encryption = Cifrar.cifrado(text, displacement, AlfabetoMay, AlfabetoMin)
        print(encryption)
        invert = text[::-1]
        if int(groups) > 0:
            groupsText = Separar.dividir(encryption, groups)
        else:
            groupsText = encryption
        resp = [encryption, invert, groupsText]
        return json.dumps(resp)

    def PUT(self, another_string):
        cherrypy.session['mystring'] = another_string

    def DELETE(self):
        cherrypy.session.pop('mystring', None)


if __name__ == '__main__':
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/generator': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain')],
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public'
        }
    }
    webapp = StringGenerator()
    webapp.generator = StringGeneratorWebService()
    cherrypy.quickstart(webapp, '/', conf)
