import cherrypy

from example.controllers.example import ExampleController

from example.models import create_all


create_all()


CP_CONFIG = {
    '/': {
        'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
    },
}


def application(environ, start_response):
    # Used with a WSGI server
    cherrypy.tree.mount(ExampleController(), '/api/example', config=CP_CONFIG)
    return cherrypy.tree(environ, start_response)

def start():
    # Used for development server
    cherrypy.tree.mount(ExampleController(), '/api/example', config=CP_CONFIG)
    cherrypy.engine.start()
    cherrypy.engine.block()


if __name__ == '__main__':
    start()
