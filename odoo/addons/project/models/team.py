from odoo import models, fields, api, _


class Team(models.Model):
    _name = 'project.team'
    _description = 'To create Team'

    name = fields.Char(string='Name')
    description = fields.Text(string="About of Team")
