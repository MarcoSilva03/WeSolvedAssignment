
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
import logging

_logger = logging.getLogger(__name__)


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    tech_category_id = fields.Many2one(
        'product.category.tech', string='Tech Category')

    def action_open_import_wizard(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Import Products',
            'res_model': 'product.template.import.wizard',
            'view_mode': 'form',
            'target': 'new',
        }
