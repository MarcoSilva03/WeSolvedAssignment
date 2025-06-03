from odoo.tests.common import TransactionCase

class TestProductImport(TransactionCase):

    def test_import_all_excel_wizard_records(self):
        Wizard = self.env['product.template.import.wizard']
        all_wizards = Wizard.search([])

        for wizard in all_wizards:
            self.assertTrue(wizard.excel_file, f"Missing file in wizard {wizard.id}")
            self.assertTrue(wizard.excel_file_name, f"Missing filename in wizard {wizard.id}")
            wizard.import_products()
