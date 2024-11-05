# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class roomcategory(models.Model):
    _name = "room.category"
    _description = "room category"

    name = fields.Char(string="Room Category", required=True)
    size = fields.Char(string="Room Size")
    featured_image = fields.Image(string="Room Featured Image")
    room_type_ids = fields.One2many('product.product', 'hotel_id', string="Room Type", domain="[('is_room_type', '=', True)]")
    hotel_id = fields.Many2one('hotel.hotel', string="Hotel", ondelete='cascade', required=True)
    room_amenities_ids = fields.Many2many('room.amenities', string="Amenities")
    room_image_ids = fields.One2many('room.cat.image', 'room_cat_id', string="Room Images")
    description = fields.Html(string="Description")




class HotelRooms(models.Model):
    _name = "hotel.rooms"
    _description = "Rooms"

    name = fields.Char(string="Room No", required=True)
    hotel_id = fields.Many2one('hotel.hotel', string="Hotel", ondelete='cascade')
    room_category_id = fields.Many2one('room.category', string="Room Category", ondelete='cascade')
    room_state = fields.Selection([
        ('vacant', 'Vacant'),
        ('occupied', 'Occupied'),
    ], string='Room State', copy=False, default='vacant')



class ProductPricelist(models.Model):
    _inherit = "product.pricelist"

    is_allow_on_booking = fields.Boolean(string="Is Allow On Booking")



class RoomImage(models.Model):
    _name = 'room.image'
    _description = "Room Image"

    image_1920 = fields.Image(required=True)
    product_variant_id = fields.Many2one('product.product', "Product Variant", index=True)



class RoomCatImage(models.Model):
    _name = 'room.cat.image'
    _description = "Room Category Image"

    image_1920 = fields.Image(required=True)
    room_cat_id = fields.Many2one('room.category', "Room Category", index=True)

