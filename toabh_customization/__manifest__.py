# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Toabh Customization',
    'version': '1.0',
    'sequence': 10,
    'category': 'Customizations',
    'website': 'https://www.planet-odoo.com/',
    'depends': ['sale', 'purchase', 'crm', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'views/sales_purchase.xml',
        'views/weekly_appearance_master.xml',
        'views/brands_master.xml',
        'views/crm_activities.xml',
        'wizard/mail_compose.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
