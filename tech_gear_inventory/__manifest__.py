# -*- coding: utf-8 -*-

{
    'name': "Wesolved - Tech Gear Inventory Module",
    'author': "Wesolved",
    "version": "18.0.0.0",
    "category": "Tools",
    'summary': "",
    'description': "",
    'depends': ['product', 'stock', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_category_views.xml',
        'views/product_template_views.xml',
        'wizards/product_template_import_wizard_views.xml',
        'data/test_import_file.xml',

    ],
    'installable': True,
    'application': False,
}
