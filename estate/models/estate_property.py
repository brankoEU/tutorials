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
    garden_area = fields.Integer(string="Garden Area (sqm)")
    garden_orientation = fields.Selection([('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')], string="Orientation")
    state = fields.Selection([('new', 'New'), ('offer_received', 'Offer Received'), ('sold', 'Sold')], string='State', default='new')
    buyer_id = fields.Many2one('res.partner', string='Buyer')
    salesman_id = fields.Many2one('res.users', string='Salesman')
    property_type_id = fields.Many2one('estate.property.type', string='Property Type')
    property_tag_id = fields.Many2many('estate.property.tag', string='Property Tag')
    offer_ids = fields.One2many("estate.property.offer", "property_id", string="Offers")
    total_area = fields.Float(compute="_compute_total", string='Total Area (sqm)')
    best_offer = fields.Float(compute="_compute_best_offer", string='Best Offer')

    @api.depends('living_area', 'garden_area')
    def _compute_total(self):
        for this in self:
            this.total_area = float(this.living_area + this.garden_area)

    @api.depends('offer_ids')
    def _compute_best_offer(self):
        for this in self:
            if not bool(this.offer_ids):
                this.best_offer = 0.00
            else:
                for offer in this.offer_ids:
                    if this.best_offer < offer.price:
                        this.best_offer = offer.price

    @api.onchange("garden")
    def _onchange_garden(self):
        if bool(self.garden):
            self.garden_orientation = 'north'
            self.garden_area = 10
        else:
            self.garden_orientation = False
            self.garden_area = 0.00
