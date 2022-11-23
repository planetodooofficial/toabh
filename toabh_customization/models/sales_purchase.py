from odoo import fields, models, api


class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'

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
            purchase_refs = ["<b><a href=# data-oe-model=purchase.order data-oe-id=%s>%s</a></b>" % (rec.id, rec.name) for rec in purchase_ids]
            sales_msg = "Purchase Order Created %s" % ','.join(purchase_refs)
            self.message_post(body=sales_msg)
        return res


class SaleOrderLineInherit(models.Model):
    _inherit = 'sale.order.line'

    vendor_id = fields.Many2one('res.partner', ondelete='restrict')
