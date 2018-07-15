# -*- coding: utf-8 -*-
from odoo import http

# class TurkishIdvalidator(http.Controller):
#     @http.route('/turkish_idvalidator/turkish_idvalidator/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/turkish_idvalidator/turkish_idvalidator/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('turkish_idvalidator.listing', {
#             'root': '/turkish_idvalidator/turkish_idvalidator',
#             'objects': http.request.env['turkish_idvalidator.turkish_idvalidator'].search([]),
#         })

#     @http.route('/turkish_idvalidator/turkish_idvalidator/objects/<model("turkish_idvalidator.turkish_idvalidator"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('turkish_idvalidator.object', {
#             'object': obj
#         })