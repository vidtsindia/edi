# -*- coding: utf-8 -*-
# © 2016 Akretion (Alexis de Lattre <alexis.delattre@akretion.com>)
# © 2017-Today Serpent Consulting Services Pvt. Ltd.
#    (<http://www.serpentcs.com>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Sale Commercial Partner',
    'version': '9.0.1.0.0',
    'category': 'Sales Management',
    'license': 'AGPL-3',
    'summary': "Add stored related field 'Commercial Customer' on sale orders",
    'author': 'Akretion,Odoo Community Association (OCA)',
    'website': 'http://www.akretion.com',
    'depends': ['sale'],
    'data': [
        'views/sale.xml',
        'report/sale_report_view.xml',
    ],
    'installable': True,
}
