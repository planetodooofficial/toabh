# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Toabh Customization',
    'version': '1.0',
    'sequence': 10,
    'category': 'Customizations',
    'website': 'https://www.planet-odoo.com/',
    'depends': ['sale', 'purchase'],
    'data': [
        'views/sales_purchase.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
