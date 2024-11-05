# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class DestinationGroup(models.Model):
    _name = 'destination.group'
    _rec_name = 'name'
    _description = 'destination groups'

    name = fields.Char(string="Name", required=True)
    destination_group_ids = fields.One2many('hotel.hotel', 'destination_group_id', string="Destination Group")










