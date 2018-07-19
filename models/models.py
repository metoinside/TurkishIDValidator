# -*- coding: utf-8 -*-

from odoo import models, fields, api

class turkish_idvalidator(models.Model):
    _inherit = 'res.users'

    lastname= fields.Char(string="Last Name")
    birthYear = fields.Integer(string="Birth Year")
    turkishIdNumber = fields.Char(string="Turkish ID No")
    verification = fields.Boolean(string="Verification Status", default=True)
    validation = fields.Boolean(string="Validation Status", default=False)
