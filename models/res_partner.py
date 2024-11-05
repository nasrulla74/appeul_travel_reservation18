from odoo import api, fields, models, _


class BookingPartner(models.Model):
    _inherit = 'res.partner'

    is_booking_agent = fields.Boolean(string='Is Booking Agent')
    is_booking_client = fields.Boolean(string='Is Booking Client')
    x_suffix = fields.Char(string='Suffix')
    x_prefix = fields.Char(string='Prefix')
    x_next_number = fields.Char(string='Next Number')
    x_seq_name = fields.Char(string='Sequence Name')



