# KB Customers App

Custom module untuk ERPNext yang digunakan untuk mengelola Customer Kawasan Berikat.

## Fitur

- **KB Customer**: DocType untuk mengelola data customer KB.
- **Packing List**: DocType untuk menyimpan data packing list, termasuk No Delivery Order, No Sales Invoice, No Purchase Order Customer, dan tabel items dengan nama item, deskripsi, qty, unit, berat item.
  - Dapat menarik data items dari Sales Invoice yang sudah di-submit.

## Instalasi

1. Pastikan Anda berada di direktori bench ERPNext Anda.
2. Jalankan perintah berikut untuk menginstall app:

   ```
   bench get-app kb_customers /path/to/kb_customers
   bench install-app kb_customers
   bench migrate
   ```

3. Restart bench:

   ```
   bench restart
   ```

## Penggunaan

Setelah instalasi, module "KB Customers" akan muncul di Desk ERPNext. Anda dapat membuat record "KB Customer" dan "Packing List".

Untuk Packing List, pilih Sales Invoice yang sudah di-submit, lalu gunakan method `get_items_from_sales_invoice` untuk mengisi tabel items.

## Struktur

- `kb_customers/doctype/kb_customer/`: DocType untuk KB Customer dengan fields dasar seperti nama, tipe, zona KB, dll.