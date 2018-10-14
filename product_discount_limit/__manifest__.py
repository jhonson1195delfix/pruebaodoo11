# -*- coding: utf-8 -*-
{
    'name': "Product Discount Limit",
    'summary': """Defines limits for discounts on products, specific to each salesman 
        """,
    'description': """        
        This module defines max limits for discounts per product 
        This module asociates those limits to a specific salesman
        
        ***Installing this module implies abc details***
        
    """,
    'author': "Delfix",
    'website': "http://www.delfixcr.com",
    'category': 'Dev',
    'version': '0.1',
    'depends': ['base', 'product', 'purchase','sale'],
    'data': [
        'views/product_template_inherit_views.xml',
        # 'views/inherit_product_template_view.xml',
        # 'views/sale_order_inherit.xml',
        # 'security/ir.model.access.csv',
    ],
}