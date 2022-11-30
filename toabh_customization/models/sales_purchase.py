from odoo import fields, models, api


class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'

    weekly_id = fields.Many2one("weekly.appearance", "Week/Appearance/Performance/Film")
    partner_id = fields.Many2one("res.partner", 'Client Contact')
    brands_id = fields.Many2one("competitive.brands", "Competitive Brands")
    job_date_start = fields.Date("job_start_date")
    job_date_end = fields.Date("job_end_date")
    travel_dates_start = fields.Date("travel_start")
    travel_dates_end = fields.Date("travel_end")
    usage_start = fields.Date("usage_start")
    usage_end = fields.Date("usage_end")
    job_location = fields.Char()
    # added
    usage_country_id = fields.Many2one("res.country", string="Usage Country")
    exclusive = fields.Selection([("y", "Yes"), ("n", "No")], default="n")

    # talent_ids = fields.One2many('talents.pay', 'connection_id', string='Talents')

    @api.model
    def default_get(self, fields_list):
        res = super().default_get(fields_list)
        # print(res)
        res['note'] = "<strong>Note</strong> :-<br>" \
                      "Shoot duration is 12 hrs including hair & makeup and local travel to shoot location " \
                      "All payments need to be cleared within 15 days of shoot."
        return res

    # Inherited Base Action
    # On Confirm of Sale Order Purchase Order Should be created Automatically
    # Purchase Order should be created where vendor is set in sale.order.line
    def action_confirm(self):
        res = super(SaleOrderInherit, self).action_confirm()
        purchase_ids = self.env['purchase.order']
        for rec in self.order_line.filtered(lambda x: x.vendor_id):
            purchase_data = {'partner_id': rec.vendor_id.id,
                             'origin': self.name,
                             'order_line': [(0, 0, {
                                 'product_id': rec.product_id.id,
                                 'product_qty': rec.product_uom_qty,
                                 'sale_line_id': rec.id,
                             })]}
            purchase_id = purchase_ids.create(purchase_data)
            purchase_ids += purchase_id
            sales_ref = "<b><a href=# data-oe-model=sale.order data-oe-id=%s>%s</a></b>" % (self.id, self.name)
            purchase_msg = "Purchase Order Created from %s" % sales_ref
            purchase_id.message_post(body=purchase_msg)
        if purchase_ids:
            purchase_refs = ["<b><a href=# data-oe-model=purchase.order data-oe-id=%s>%s</a></b>" % (rec.id, rec.name)
                             for rec in purchase_ids]
            sales_msg = "Purchase Order Created %s" % ','.join(purchase_refs)
            self.message_post(body=sales_msg)
        return res


class SaleOrderLineInherit(models.Model):
    _inherit = 'sale.order.line'
    vendor_id = fields.Many2one('res.partner', ondelete='restrict')
    product_id = fields.Many2one('product.product')
    product_uom_qty = fields.Float()
    price_unit = fields.Float()
    tax_id = fields.Many2many('account.tax')
    product_template_id = fields.Many2one('product.template')
