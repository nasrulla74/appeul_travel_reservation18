import datetime

from odoo.exceptions import ValidationError
from odoo import models, fields, api, _
from datetime import datetime, date, timedelta



class SaleOrderBooking(models.Model):
    _inherit = 'sale.order'

    @api.model
    def default_get(self, fields):
        res = super(SaleOrderBooking, self).default_get(fields)
        tdate = datetime.today()
        end_date = tdate + timedelta(days=7)
        arr_date1 = tdate.strftime("%Y-%m-%d") + " 09:00"
        dep_date2 = end_date.strftime("%Y-%m-%d") + " 06:00"

        res['check_in_date'] = arr_date1
        res['check_out_date'] = dep_date2
        return res

    booking_name = fields.Char('Booking Name', default='')
    booking_ref = fields.Char('Booking Ref')
    booking_no = fields.Char('Booking No')
    hotel_id = fields.Many2one('hotel.hotel', string="Hotel")
    check_in_date = fields.Datetime(string="Check In")
    check_out_date = fields.Datetime(string="Check Out")
    #room_type_id = fields.Many2one('product.product', string="Room Type", required=True)
    ## --------------Depricated - start!!
    room_type_id = fields.Many2one('product.product', string="Room Type")
    adults = fields.Integer(string="Adults", required=True, default="2", related="room_type_id.adults")
    childs = fields.Integer(string="Child", required=True, default="0", related="room_type_id.childs")
    infants = fields.Integer(string="Infants", required=True, default="0", related="room_type_id.infants")
    meal_id = fields.Many2one('hotel.meal', string="Meal", related="room_type_id.meal_id")
    ## --------------Depricated - end!!
    tot_pax = fields.Integer(string="Total Pax", default="0", compute="_compute_tot_pax")
    bk_method = fields.Selection(
        [('foreign-operator', 'Foreign tour operator'), ('local-operator', 'Local tour operator'),
         ('direct-fit', 'Direct booking/(FIT)'), ('ota', 'Online travel agent')],
        default='ota', string="Booking Method")
    bed_nights = fields.Integer('Bed Nights', compute="_compute_bed_nights")
    is_booking = fields.Boolean(string='Is Booking')
    bk_state = fields.Selection([
        ('draft', 'Draft'),
        ('reserved', 'Reserved'),
        ('verified', 'Verified'),
        ('booked', 'Booked'),
        ('check_in', 'Check-In'),
        ('check_out', 'Check-Out'),
        ('no_show', 'No Show'),
        ('cancelled', 'Cancelled'),
    ], string='State', readonly=True, copy=False, index=True, tracking=3, default='draft')
    room_type_details = fields.Text(string="Room Type Details")
    allocated_room_id = fields.Many2one('hotel.rooms', string="Allocated Room")
    arr_flight = fields.Char('Arrival Flight', default='')
    dep_flight = fields.Char('Departure Flight', default='')
    remarks = fields.Text('Special Request/Remarks', default='')

    @api.onchange('check_out_date', 'check_in_date')
    def _compute_bed_nights(self):
        for rec in self:
            if (rec.check_in_date and rec.check_out_date):
                rec.bed_nights = (rec.check_out_date - rec.check_in_date).days
                self.is_booking = True

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals['is_booking']:
                for ln in vals['order_line']:
                    product = self.env['product.product'].browse(ln[2]['product_id'])
                    if(product):
                        if(product['is_room_type']):
                            ln[2]['name'] = ln[2]['name'] + " Check-In: " + vals['check_in_date'][:10] + " Check-Out: " + vals['check_out_date'][:10]

        return super(SaleOrderBooking, self).create(vals_list)



    def write(self, vals):
        for val in self:
            print(val['is_booking'])
            if val['is_booking']:

                for ln in val['order_line']:
                    if(ln['product_id'].is_room_type):
                        ln['name'] = ln['product_id'].name + " Check-In: " + val['check_in_date'].strftime("%d-%b-%Y") + " Check-Out: " + val['check_out_date'].strftime("%d-%b-%Y")
        return super(SaleOrderBooking, self).write(vals)




        # bk_note = []
        # val = (0, 0, {
        #     'display_type': 'line_note',
        #     'name': 'My Note',
        # })
        # bk_note.append(val)
        # self.order_line = bk_note

## Add order line a section
    # new_lines = []
    # val = (0, 0, {
    #     'display_type': 'line_section',
    #     'name': 'SECTION NAME',
    # })
    # new_lines.append(val)
    # rec.order_line = new_lines




    # @api.model_create_multi
    # def create(self, vals_list):
    #     # default_hotel_id = self.env['ir.config_parameter'].sudo().get_param(
    #     #     'wt_hotel_reservation.default_booking_default_hotel_id')
    #     for vals in vals_list:
    #         if vals['is_booking']:
    #             vals['booking_no'] = (self.env['ir.sequence'].next_by_code('hotel.booking') or 'New')
    #
    #             return super().create(vals_list)
    #         else:
    #             return super().create(vals_list)

    @api.onchange('order_line')
    def _compute_tot_pax(self):
        tpax = 0
        room_details = ""
        for rec in self.order_line:
            if(rec.product_id.is_room_type):
                tpax += rec.product_id.adults + rec.product_id.childs + rec.product_id.infants
                room_details += rec.product_id.name + ', '

        self.tot_pax = tpax
        self.room_type_details = room_details


    def name_get(self):
        res = []
        for rec in self:
            name = rec.name
            if rec.booking_name:
                name = name + ' - ' + rec.booking_name
                res.append((rec.id, name))
        return res