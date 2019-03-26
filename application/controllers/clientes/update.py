import config

class Update:

    def __init__(self):
        pass

    def GET(self, id_cliente):
        clientes = config.form_clientes()
        result = config.model.get_clientes(id_cliente)
        clientes.fill(result)
        return config.render.update(clientes)

    def POST(self, id_cliente):
        clientes = config.form_clientes()
        if clientes.validates():
            config.model.update_clientes(**clientes.d)
            raise config.web.seeother('/')
        else:
            return config.render.update(clientes)
