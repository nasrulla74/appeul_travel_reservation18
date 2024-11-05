# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class AccountMoveTravelReservation(models.Model):
    _name = 'account.move'
    _inherit = ['account.move', 'utm.mixin']


    profoma_invoice_ref = fields.Char(string="Profoma Invoice Ref")
    is_tax_invoice_received = fields.Boolean(string="Is Tax Invoice Received", default=False)
    booking_ref_id = fields.Many2one('sale.order', string="Booking/Order Id", domain="[('is_booking', '=', True)]")



    def write(self, vals):
        # import pdb;pdb.set_trace()
        res = super(AccountMoveTravelReservation, self).write(vals)
        if self.state == 'posted':
            for line in self.invoice_line_ids:
                line.sale_line_ids.order_id.bk_state = 'booked'

        if self.payment_state == 'paid':
            for line in self.invoice_line_ids:
                line.sale_line_ids.order_id.bk_state = 'booked'

        return res