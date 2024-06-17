
from odoo import api, fields, models
from odoo.exceptions import UserError
from odoo.tools import format_amount
from datetime import datetime


class Category_item(models.Model):
    _name = "item.category"

    name = fields.Char(string="Descripcion")
    item_type = fields.Many2one("item.type",strin="Tipo de item")
    

    
