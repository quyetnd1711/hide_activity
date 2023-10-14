# -*- coding: utf-8 -*-
{
    'name': "Hide Activity",
    'license': 'AGPL-3',
    'summary': """Hide icon Activity from header""",
    'description': """
        Hide icon Activity from header
    """,
    'version': "16.0",
    'author': "Duc Quyet",
    'support': 'nquyet76@gmail.com',
    'images': ['static/description/icon.png'],
    'category': 'tools',
    'depends': ['base'],
    'data': [

    ],
    'assets': {
        'web.assets_backend': [
            'hide_activity/static/src/xml/*.xml',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
}
