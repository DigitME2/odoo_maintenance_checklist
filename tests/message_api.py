import xmlrpc.client

url = "http://localhost:8069"
db = "odoo"
username = 'admin'
password = 'admin'

common = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/common')
uid = common.authenticate(db, username, password, {})
models = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/object')

result = models.execute_kw(db, uid, password,
                           'mail.message',
                           'create',
                           [{"body": "<p>Test Message</p>",
                             "model": "maintenance.request",
                             "res_id": 26,
                             "message_type": "comment",
                             "subtype_id": 2}])
print(result)
