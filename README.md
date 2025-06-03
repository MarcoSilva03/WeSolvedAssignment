# WeSolvedAssignment

# Tech Gear Inventory – Odoo 18 Custom Module

## 📦 Overview

**Tech Gear Inventory** is a custom module for **Odoo 18 Enterprise**, designed to facilitate importing and organizing products using Excel files. It introduces a user-friendly wizard that allows administrators to upload an `.xlsx` file and have products automatically created or updated in the system.

This module was built for testing and demonstration purposes, especially showcasing how to:

- Use wizards with file uploads
- Parse Excel files with `openpyxl`
- Dynamically create or update product templates and categories
- Manage product inventory quantities using Odoo's internal tools
- Write and run automated tests for business features using Odoo's test framework

---

## ✅ Features

- 📁 Upload an Excel file via a wizard (`.xlsx` only)
- 📊 Automatically parses rows to create:
  - Product templates
  - Custom technical categories
  - Stock updates for each product
- 🧪 Includes unit tests to validate:
  - Correct parsing of Excel file
  - Accurate product creation
  - Inventory updates

---

## 📄 Example Excel Format

The Excel file should contain the following columns:

| Product Name           | Category       | Price  | Qty |
|------------------------|----------------|--------|-----|
| Samsung SM-A057 Galaxy | Smartphones    | 950.00 | 15  |
| Apple iPhone 14        | Smartphones    | 1200.00| 5   |

You can find a test Excel file in:  
**`tech_gear_inventory/data/test_import_file.xml`**  
(This file is base64-encoded and used in automated test cases.)

---

## 🧪 Testing

This module comes with a working test case using `TransactionCase`:

```bash
./odoo-bin -c odoo18.conf \
  --addons-path=odoo/addons,custom-addons/test_odoo18 \
  -d db_demo_v18 \
  -i tech_gear_inventory \
  --test-enable \
  --stop-after-init
