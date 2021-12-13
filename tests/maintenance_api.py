import xmlrpc.client

url = "http://localhost:8069"
db = "odoo"
username = 'admin'
password = 'admin'

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
uid = common.authenticate(db, username, password, {})
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))


# Get the IDs of all maintenance requests that have stage_id of 1 (ready)
ids = models.execute_kw(db, uid, password,
    'maintenance.request', 'search',
    [[['stage_id', '=', 1]]],
    {'limit': 10})

# Get the names of the tasks we just found
result = models.execute_kw(db, uid, password,
    'maintenance.request', 'read', [ids], {'fields': ['name']})

print(result)

# Mark the tasks as done (stage_id 4)
edit_id = ids[0]
models.execute_kw(db, uid, password, 'maintenance.request', 'write', [[edit_id], {'stage_id': 4}])


# Get the IDs of all maintenance requests that have stage_id of 1 (ready)
ids = models.execute_kw(db, uid, password,
    'maintenance.request', 'search',
    [[['stage_id', '=', 1]]],
    {'limit': 10})

# Get the names of the tasks we just found
result = models.execute_kw(db, uid, password,
    'maintenance.request', 'read', [ids], {'fields': ['name']})

print(result)
