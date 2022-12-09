from odoo import fields, models


class WeeklyAppearance(models.Model):
    _name = "weekly.appearance"
    name = fields.Char("Name")

