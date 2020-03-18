# -*- coding: utf-8 -*-

from odoo import fields, models

class SaleOrder(models.Model):
    _name = "sale.order"

    delivery_place = fields.Many2one('stock.delivery.place', 'Incoterms Port', 'Incoterms Extended: ports')
