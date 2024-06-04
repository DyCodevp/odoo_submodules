
from odoo import api, fields, models
from odoo.exceptions import UserError
from odoo.tools import format_amount
from datetime import datetime


class Category_item(models.Model):
    _name = "item.category"

    name = fields.Char("Descripcion")
    

    
