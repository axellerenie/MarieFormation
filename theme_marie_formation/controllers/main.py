# -*- coding: utf-8 -*-
from odoo import http, models, fields, _
from odoo.http import request

class WebsiteQweb(http.Controller):
    @http.route(['/with_controller'], type='http', auth="public", website=True, multilang=True)
    def page_with_controller(self):
        #some logics & return the template
        # in this example, it works only for admin user (or the right to read res.partner model)
        # it is possible to overwrite this rule by adding a .sudo() before the search method
        contacts = request.env['res.partner'].search([],order='name')
        return request.render('theme_marie_formation.page_with_controller',{'variable':'My 🤘 Variable','contacts':contacts})
