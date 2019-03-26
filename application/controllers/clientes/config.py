import web
from web import form
import application.models.model_clientes

render = web.template.render('application/views/clientes/', base='master')
model = application.models.model_clientes

vemail = form.regexp(r".*@.*", "Must be a valid email address")
'''
Here we define the form fields for use in all the views
'''
form_clientes= form.Form(
            form.Textbox('id_cliente',description="Id_cliente", class_="form-control"),
            form.Textbox('nombre',description="Nombre", class_="form-control", required=True),
            form.Textbox('apellido_paterno',description="Apellido paterno", class_="form-control", required=True),
            form.Textbox('apellido_materno',description="Apellido materno", class_="form-control", required=True),
            form.Textbox('telefono',description="Telefono", class_="form-control", required=True),
            form.Textbox('email', vemail, description="Email", class_="form-control", required=True),
        )
        