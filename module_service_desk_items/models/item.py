from odoo import api, fields, models
from odoo.exceptions import UserError
from odoo.tools import format_amount
from datetime import datetime


class Item(models.Model):
    _name = "item.item"

    _description = "manage Items in helpdesk"

    name = fields.Char("Descripcion")
    helpdesk_team = fields.Many2one("helpdesk.team", string="Equipo de soporte")
    item_type = fields.Many2one("item.type", string="Tipo de Item")
    item_category = fields.Many2one("item.category", string="Categoria de Item")
    item_tag_ids = fields.Many2many(
        'item.tags',  # Related model name
        'items_tags_rel',  # Table name for the relation
        'tags_id',              # Field name for this model
        'name',          # Field name for related model
        string='Tags Asociados'
    )
