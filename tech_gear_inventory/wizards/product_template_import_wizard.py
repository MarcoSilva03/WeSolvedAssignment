
from odoo import api, models, fields, _
from odoo.exceptions import UserError
import base64
import io
import openpyxl


class ProductTemplateImportizard(models.TransientModel):

    _name = 'product.template.import.wizard'
    _description = 'Wizard to Import Products from Exel File'

    excel_file = fields.Binary('Excel File', required=True)
    excel_file_name = fields.Char('Filename')

    def import_products(self):
        if not self.excel_file_name or not self.excel_file_name.endswith('.xlsx'):
            raise UserError(
                "Please upload a valid .xlsx file with a proper filename.")

        file_data = base64.b64decode(self.excel_file)
        workbook = openpyxl.load_workbook(
            filename=io.BytesIO(file_data), data_only=True)
        sheet = workbook.active

        for idx, row in enumerate(sheet.iter_rows(min_row=2, values_only=True), start=2):
            name, category_name, price, qty = row

            if not name:
                raise UserError(f"Missing product name in row {idx}")

            category = self.env['product.category.tech'].search(
                [('name', '=', category_name)], limit=1)
            if not category:
                category = self.env['product.category.tech'].create(
                    {'name': category_name})

            product_template = self.env['product.template'].search(
                [('name', '=', name)], limit=1)

            if not product_template:
                product_template = self.env['product.template'].create({
                    'name': name,
                    'type': 'consu',
                    'tech_category_id': category.id,
                    'list_price': price or 0.0,
                    'is_storable': True,
                })

            if product_template.product_variant_id and qty:
                self._update_stock(product_template.product_variant_id, qty)

    def _update_stock(self, product, incoming_qty):
        current_qty = product.qty_available
        total_qty = current_qty + incoming_qty

        self.env['stock.change.product.qty'].create({
            'product_id': product.id,
            'product_tmpl_id': product.product_tmpl_id.id,
            'new_quantity': total_qty,
        }).change_product_qty()
