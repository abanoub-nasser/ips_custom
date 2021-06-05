from odoo import fields, models


class ProductCategory (models.Model):
    _inherit = 'product.category'

    user_ids = fields.Many2many('res.users', 'res_product_category_users_rel', 'cid', 'user_id')



class ResUsers (models.Model):
    _inherit = 'res.users'
    
    users_categories = fields.Many2many('product.category', 'res_product_category_users_rel', 'user_id', 'cid',
                     string='Categories to access')
