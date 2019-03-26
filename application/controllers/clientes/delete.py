import config

class Delete:
    
    def __init__(self):
        pass

    def GET(self, id_cliente):
        clientes = config.form_clientes()
        result = config.model.get_clientes(id_cliente)
        clientes.fill(result)
        return config.render.delete(clientes)

    def POST(self, id_cliente):
        config.model.delete_clientes(id_cliente)
        raise config.web.seeother('/')
