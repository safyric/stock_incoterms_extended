# -*- coding: utf-8 -*-

from odoo import fields, models

class DeliveryPorts(models.Model):
    _name = "stock.delivery.points"
    _description = "Stock Delivery Points"

    name = fields.Char(
        'Name', required=True, translate=True,
        help="Delivery points are generally used with Incoterms to distinguish responsibilities.")
    code = fields.Char(
        'Code', required=True,
        help="Ports Standard Code")
    active = fields.Boolean(
        'Active', default=True,
        help="By unchecking the active field, you may hide a delivery point you will not use.")
