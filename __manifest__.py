# -*- coding: utf-8 -*-
{
    'name': "Incoterms Extended",
    'summary': """This module extends the Incoterms to include destination ports/place"",
    'description': """This module extends the Incoterms to include destination ports/place""",
    'author': "Safyric Co., Ltd.",
    'website': "https://wwww.safyric.com",
    'category': 'Business',
    'version': '0.1',
    'depends': ['stock'],
    'data': [
        'security/ir.model.access.csv',
        'data/stock_delivery_place.xml',
        'views/stock_delivery_view.xml',
        'views/sale_order_view.xml',
    ],
    'installable': True,
}
