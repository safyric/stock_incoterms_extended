# -*- coding: utf-8 -*-
{
    'name': "Delivery Points",
    'summary': """Incoterms Delivery Points""",
    'description': """This module adds list of delivery points for use with Incoterms in Sale Order""",
    'author': "Safyric Co., Ltd.",
    'website': "https://wwww.safyric.com",
    'category': 'Business',
    'version': '0.1',
    'depends': ['stock', 'product'],
    'data': [
        'data/stock_ports_data.xml',
        'views/stock_delivery_ports_views.xml',
    ],
    'installable': True,
}
