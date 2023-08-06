# Django CMS PDFembed 
This is a plugin for [django CMS](https://www.django-cms.org/) to let users embed a PDF file on webpages.

It uses django-filer for thje file upload handling.

## Installation

- Add `pdfembed` to `INSTALLED_APPS`.
- Run `manage.py migrate` to apply the needed migrations.

## Customization

The default template will render the PDF in an iframe with default width 100% and heigth 500px. These can be changed in the plugin creation wizard.

The template is located in `/templates/pdfembed/pdf_embed.html` and can also on that location be overwritten in your own project.