{
    'name': 'IBS custom',
    'version': '1.0',
    'summary': 'Customizations ... Adding security groups',
    'description': 'Customizations ... Adding security groups',
    'author': 'Abanoub Nasser',
    'depends': ['base','stock','stock_account','product'],
    'data': ['security/groups.xml',
             'security/ir_rule.xml',
             'views/users_inherited.xml'
             ,'views/hide_cost.xml'],
    'installable': True,
    'auto_install': False
}