from odoo import fields, api, models, _


class MailActivityInherit(models.Model):
    _inherit = 'mail.activity'

    assigned_by = fields.Char('Assigned By', default=lambda self: self.env.user.name)

