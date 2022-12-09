from odoo import fields, api, models, _


class HrEmployeeInherit(models.Model):
    _inherit = 'hr.employee'

    _sql_constraints = [
        ('barcode_uniq', 'unique (barcode)', "The Badge ID must be unique, this one is already assigned to another employee."),
        ('user_uniq', 'CHECK(1=1)', "A user cannot be linked to multiple employees in the same company.")
    ]
