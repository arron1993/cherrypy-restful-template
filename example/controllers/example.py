import cherrypy

from sqlalchemy.orm import sessionmaker, scoped_session

from example.models import engine
from example.models.example import Example

session = scoped_session(sessionmaker(bind=engine))


@cherrypy.expose
@cherrypy.popargs('example_id')
class ExampleController():
    @cherrypy.tools.json_out()
    def GET(self, example_id=None):
        return "GET"

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def POST(self):
        return "POST"

    @cherrypy.tools.json_out()
    def DELETE(self, example_id):
        return "DELETE"

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def PUT(self):
        return "PUT"
