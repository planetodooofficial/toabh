from odoo import fields, models


class CompetitiveBrands(models.Model):
    _name = "competitive.brands"
    name = fields.Char("Brand Name")

