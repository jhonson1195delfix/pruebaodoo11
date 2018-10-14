# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class SaleOrderLineInherit(models.Model):
	_inherit = "sale.order.line"

	#Valida el descuento ingresado por el usuario para que no sea mayor al del limite del porducto
	@api.onchange('discount')
	def _onchange_discount_sale_man(self):
		if self.discount:
			if not self.user_has_groups('sales_team.group_sale_manager'):
				if self.product_id.discount_limit != -1 and self.product_id.discount_limit < self.discount:
					return {'value': {'discount': self.product_id.discount_limit}, 'warning': {'title': 'Atención',
																							   'message': 'Este producto tiene un maximo de descuento de: ' + str(self.product_id.discount_limit) + '%'}}
	#Pone el limite de descuento del producto
	@api.onchange('product_id', 'price_unit', 'product_uom', 'product_uom_qty', 'tax_id')
	def _onchange_discount_d(self):
		if self.product_id:
			discount = self.product_id.discount_limit
			if discount < -1:
				self.discount = 0
			else:
				self.discount = self.product_id.discount_limit
