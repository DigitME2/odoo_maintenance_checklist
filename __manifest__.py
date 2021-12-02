# -*- coding: utf-8 -*-
# noinspection PyStatementEffect
{
    'name': "Maintenance Scheduler",

    'author': "Sam Bannister",
    'installable': True,
    'application': True,

    'category': 'Sales/CRM',
    'version': '0.2',
    'depends': ['base',
                'maintenance'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/maintenance_menu_extension.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
