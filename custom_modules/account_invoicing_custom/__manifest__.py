# -*- coding: utf-8 -*-
{
    'name': "account_invoicing_custom",

    'summary': """
        Edición factura para Develoop Software""",

    'description': """
        Modificaciones en el impreso factura para Develoop Software
    """,

    'author': "Develoop Software",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}