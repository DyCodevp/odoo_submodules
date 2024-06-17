
from odoo import api, fields, models
from odoo.exceptions import UserError
from odoo.tools import format_amount
from datetime import datetime


class Ticket_Item(models.Model):
    _inherit = "helpdesk.ticket"
    
    evidence = fields.Binary(string="Evidencia")
    case_solution = fields.Html(string="Solucion del caso")
    #team_id_item = fields.Reference("team_id")
    item = fields.Many2one("item.item", string="Item")
    item_type = fields.Many2one("item.type", string="Tipo de item")
    item_category = fields.Many2one("item.category", string="Categoria de Item ")
    item_tags = fields.Many2many("item.tags", string="Tags Relacionados")
