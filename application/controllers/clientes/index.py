import config

class Index:

    def __init__(self):
        pass

    def GET(self):
        result = config.model.get_all_clientes()
        return config.render.index(result)
    