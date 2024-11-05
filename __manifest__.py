# -*- coding: utf-8 -*-

{
    "name": "Appeul Travel Agency Reservation18 1.0.4",
    "version": "18.0.1.0.4",
    "category": "Appeul Travel Agency Reservation",
    "summary": "Appeul Travel Agency Reservation",
    "description": """
        For Appeul Travel Agency Reservations & Accounting, Invoicing, Sales
    """,
    "author": "Appeul - Solutions",
    "website": "http://appeul.com",
    "support": "info@appeul.com",
    "depends": ['base','base_setup', 'account', 'utm', 'rating', 'sale'],
    "data": [
        'security/ir.model.access.csv',
        # 'data/booking_number.xml',
        'data/hotel_type.xml',
        'data/feat_amenity.xml',
        'data/credit_cards.xml',
        'data/add_all_fac_categories.xml',
        'data/add_all_facilities.xml',
        # 'report/profoma_sale_report_inherite.xml',
        # 'report/booking_invoice_report_inherite.xml',
        'views/configuration_view.xml',
        'views/hotel_room_type.xml',
        'views/hotel_room_view.xml',
        'views/room_category.xml',
        'views/destination_groups.xml',
        'views/hotel_view.xml',
        'views/sale_booking_view.xml',
        'views/menus.xml',
        # 'views/pricelist.xml',
        # 'views/res_config.xml',
        # 'views/sales_order_inherit.xml',
        # 'views/booking_timeline.xml',
        # 'views/inherit_vendor_bill_form.xml',
        # 'views/login_page_inherit.xml',

    ],
    'assets': {
        "web.assets_backend": [
            "appeul_travel_reservation/static/src/js/user_menu_items.esm.js",

        ],
    },
    'qweb': [],
    "price": 250,
    'currency': 'USD',
    "images": ['static/images/appeul_logo.png'],
    "license": "OPL-1",
    "installable": True,
    "application": True,
    "auto_install": False,
    'external_dependencies': {},
}
