# -*- coding: utf-8 -*-
{
    'name': "Student Profile",
    'summary': "Testing for trainee",
    'sequence': -100,
    'description': """
Long description of module's purpose
    """,

    'author': "Aktiv software",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        "views/student_view.xml",
        'views/views.xml',
        'views/templates.xml',
        'views/menu.xml',
        'views/sale_order.xml'
    ]
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}

