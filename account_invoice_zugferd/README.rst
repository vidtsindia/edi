.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

=======================
Account Invoice ZUGFeRD
=======================

With this module, the PDF customer invoices and refunds generated by the Qweb reporting engine of Odoo will comply with the `ZUGFeRD <http://www.pdflib.com/knowledge-base/pdfa/zugferd-invoices/>`_ standard at *Comfort* level. The ZUGFeRD standard is a standard based on `CII <http://tfig.unece.org/contents/cross-industry-invoice-cii.htm>`_ (Cross-Industry Invoice) for electronic invoicing. The great idea of the ZUGFeRD standard is to embed an XML file inside the PDF invoice to carry structured information about the invoice. So, with a ZUGFeRD PDF invoice :

* no need to change your habbits and those of your customers: you can still send your PDF invoices by email as usual.
* customers equiped with a modern accouting software will be able to import the invoice automatically as supplier invoice by taking advantage of the embedded XML file,
* customers with an ancient accounting software will just open the PDF file with their PDF reader and manually encode the document as supplier invoice in their accounting software.

The PDF invoices generated by this module have been validated by the `ZUGFeRD eInvoice validation portal <https://www.din-zugferd-validation.org>`_ and the validation system says that the invoices have 0 errors.

Installation
============

This module requires the Python library *PyPDF2*. To install it, run:

.. code::

  sudo pip install PyPDF2

Configuration
=============

You just need to do the configuration of the module *base_zugferd* (see the description of that module for more information).

Usage
=====

On the form view of a customer invoice/refund, just click on the *Print* button as usual to get the ZUGFeRD-compliant PDF file.

.. image:: https://odoo-community.org/website/image/ir.attachment/5784_f2813bd/datas
   :alt: Try me on Runbot
   :target: https://runbot.odoo-community.org/runbot/226/8.0

Known issues / Roadmap
======================

* Add a hook in the _run_wkhtmltopdf() of the report module to embed the XML file inside the PDF file just after its generation and before it is saved as attachment (and do the same for the report_aeroo module) and try to have the related pull request accepted in Odoo. The current inherit of the get_pdf() is not good because it is not called when selecting the invoice from the attachment. In the meantime, you should always use the *Print Invoice* button to have a ZUGFeRD compliant file.

* develop glue modules (or use hasattr() ?) to add to the XML file pieces of information that is carried out by fields defined in other modules such as sale or stock (customer order reference, incoterms, delivery address, etc...).

Bug Tracker
===========

Bugs are tracked on `GitHub Issues
<https://github.com/OCA/edi/issues>`_. In case of trouble, please
check there if your issue has already been reported. If you spotted it first,
help us smashing it by providing a detailed and welcomed feedback.

Credits
=======

Contributors
------------

* Alexis de Lattre <alexis.delattre@akretion.com>

Maintainer
----------

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

This module is maintained by the OCA.

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

To contribute to this module, please visit https://odoo-community.org.
