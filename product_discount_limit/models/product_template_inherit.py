# -*- coding: utf-8 -*-


from odoo import models, fields, api, _

class ProdcutTemplateInherit(models.Model):
	_inherit = "product.template"

	discount_limit = fields.Float(string="Limite de descuento",  required=False, default=0.0)