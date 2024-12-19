# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields, models, api, _

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Property"
    _order = "id"

    name = fields.Char(string="Title", required=True)
    description = fields.Text(string="Description")
    postcode = fields.Char(string="Postcode")
    date_availability = fields.Date(string="Available From")
    expected_price = fields.Float(string="Expected Price", required=True)
    selling_price = fields.Float(string="Selling Price")
    bedrooms = fields.Integer(string="Bedrooms")
    living_area = fields.Integer(string="Living Area (sqm)")
    facades = fields.Integer(string="Facades")
    garage = fields.Boolean(string="Garage", default=True)
    garden = fields.Boolean(string="Garden", default=False)
    garden_area = fields.Integer(string="Garden Area")
    garden_orientation = fields.Selection([('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')], string="Orientation")
    state = fields.Selection([('new', 'New'), ('offer_received', 'Offer Received'), ('sold', 'Sold')], string='State', default='new')
    buyer_id = fields.Many2one('res.partner', string='Buyer')
    salesman_id = fields.Many2one('res.users', string='Salesman')
    property_type_id = fields.Many2one('estate.property.type', string='Property Type')
    property_tag_id = fields.Many2many('estate.property.tag', string='Property Tag')
