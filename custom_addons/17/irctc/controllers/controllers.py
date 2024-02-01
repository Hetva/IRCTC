# -*- coding: utf-8 -*-
# from odoo import http


# class Irctc(http.Controller):
#     @http.route('/irctc/irctc', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/irctc/irctc/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('irctc.listing', {
#             'root': '/irctc/irctc',
#             'objects': http.request.env['irctc.irctc'].search([]),
#         })

#     @http.route('/irctc/irctc/objects/<model("irctc.irctc"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('irctc.object', {
#             'object': obj
#         })

