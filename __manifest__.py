# -*- coding: utf-8 -*-
{
    'name': "Employee PlusZZ",
    'summary': """Employee Plus""",
    'description': """Employee Plus""",
    'category': 'Uncategorized',
    'website': "https://aum.vn",
    'author': 'TA',
    'version': '1.0',
    'depends': [
        'base', 'hr'
    ],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'wizard/experience_wizard.xml',
        'views/employee_plus.xml',
    ],

    'license': 'LGPL-3',
    'installable': True,
    'application': True,
}
