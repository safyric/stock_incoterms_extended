# -*- coding: utf-8 -*-

{
    "name": "Incoterms Extended",
    "version": "12.0.1.0.0",
    "author": "Safyric Co., Ltd.",

    "category": "Stock",
    "website": "https://www.safyric.com",
    "license": "AGPL-3",
    'data': [
        'security/ir.model.access.csv',
        'data/stock_delivery_place.xml',
        'views/sale_order_view.xml',
        'views/stock_delivery_view.xml'
    ],
    "depends": [
        "stock",
    ],
    "installable": True,
}
