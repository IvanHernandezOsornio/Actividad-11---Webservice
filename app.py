#Author : Salvador Hernandez Mendoza
#Email  : salvadorhm@gmail.com
#Twitter: @salvadorhm
import web
import application

ssl = False #activate ssl certificate 

if ssl == True:
    from web.wsgiserver import CherryPyWSGIServer
    CherryPyWSGIServer.ssl_certificate = "ssl/server.crt" 
    CherryPyWSGIServer.ssl_private_key = "ssl/server.key"

urls = (
    '/', 'application.controllers.clientes.index.Index',
    '/insert', 'application.controllers.clientes.insert.Insert',
    '/update/(.+)', 'application.controllers.clientes.update.Update',
    '/view/(.+)', 'application.controllers.clientes.view.View',
    '/delete/(.+)', 'application.controllers.clientes.delete.Delete',
    '/api_clientes/?', 'application.api.clientes.api_clientes.Api_clientes'
)

if __name__ == "__main__":
    app = web.application(urls, globals())
    web.config.debug = False
    app.run()
