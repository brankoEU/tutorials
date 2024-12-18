# -*- coding: utf-8 -*-
{
    'name': "Real Estate",
    'author': "Biss",
    'website': "",
    'category': 'Tutorials/RealEstate',
    'version': '1.0',
    'application': True,
    'installable': True,
    'depends': ['base'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',

    ],
    # 'assets': {
    #     'web.assets_backend': [
    #         'estate/static/src/**/*',
    #     ],
    # },
}
