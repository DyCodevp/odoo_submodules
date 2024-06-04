

from odoo import api, fields, models
from odoo.exceptions import UserError
from odoo.tools import format_amount
from datetime import datetime


class Type_item(models.Model):
    _name = "item.tags"

    name = fields.Char("Nombre")
    color = fields.Integer("Color")
    

    
