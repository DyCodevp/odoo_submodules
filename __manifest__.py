##############################################################################
#
#    OpenERP, Open Source Management Solution
#    This module copyright (C) 2018 Marlon Falcon Hernandez
##############################################################################
{
    'name': 'Help desk items',
    'version': '17.0.1.0.0',
    'author': 'Dylan Chaves Potoy',
    'maintainer': 'Dylan Chaves Potoy',
    'website': 'https://github.com/Dycodevp',
    'license': 'AGPL-3',
    'category': 'Apps',
    'summary': 'Manage items for incidents in the helpdesk module',
    'depends': ['helpdesk'],
    'data': [
      
             'security/ir.model.access.csv',
              'views/views.xml',
              'views/item_category.xml',
              'views/item_tags.xml',
              'views/item_type.xml',
        
            ],
    
    'images': ['static/description/icon.png'],
}
