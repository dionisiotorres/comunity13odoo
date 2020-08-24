# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': "Hospital Management",
    'summary': "Management of patients and doctors",
    'author': "wint wint",
    'website': 'https://github.com/OCA/project',
    'category': 'Extra Tools',
    'version': '12.0.1.0.0',
    'license': 'AGPL-3',
    'depends': [],
    'data': [
        'security/ir.model.access.csv',
        'patient.xml'
    ],
    'sequence': 10,
    'application': True,
    # 'development_status': 'Beta',
    'installable': True,
    'auto_install': False
}
