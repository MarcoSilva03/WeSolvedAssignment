
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
import logging

_logger = logging.getLogger(__name__)


class ProductCategoryTech(models.Model):
    _name = 'product.category.tech'
    _description = 'Product Category Tech'

    name = fields.Char(required=True)
    description = fields.Text()