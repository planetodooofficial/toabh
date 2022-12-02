# -*- coding: utf-8 -*-
{
    'name': 'Planet Odoo Email CC/BCC',
    'version': '16',
    'category': 'Extra Tools',
    'summary': 'Allow user can compose email with CC',
    'author': 'Planet Odoo',
    'support': 'info@planet-odoo.com',
    'website': 'https://planet-odoo.com',
    'license': 'LGPL-3',
    'price': '9',
    'currency': 'USD',
    'description': """
    We show CC/BCC input in compose email wizard, so that user can send email with CC/BCC recipients
    """,
    'depends': [
        "mail"
    ],
    'data': [
        'wizard/mail_compose.xml',
    ],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}
