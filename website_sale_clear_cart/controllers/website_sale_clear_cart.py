# -*- coding: utf-8 -*-
import werkzeug

from openerp.addons.web import http
from openerp.addons.web.http import request


class pos_website_sale(http.Controller):

    @http.route(['/shop/clear_cart'], type='json', auth="public", website=True)
    def clear_cart(self):
        order = request.website.sale_get_order()
        if order:
            for line in order.website_order_line:
                line.unlink()
