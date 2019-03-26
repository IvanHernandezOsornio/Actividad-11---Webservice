import web

"""db_host = 'localhost'
db_name = 'ferreteria_dbp'
db_user = 'quetzal'
db_pw = 'quetzal.2019'"""

db_host = 'er7lx9km02rjyf3n.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
db_name = 'l3xfh7abxcftmrsc'
db_user = 'js2dh3k1ico1x74g'
db_pw = 'fi9r1xnq2x7v9r9k'

db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw
    )