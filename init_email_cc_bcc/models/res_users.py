# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models, _, fields
from odoo.exceptions import UserError


class Users(models.Model):
    _inherit = "res.users"

    outgoing_smtp_user = fields.Char(string='Username',
                                     help="Optional username for Outgoing Mail Servers authentication", copy=False)
    outgoing_smtp_pass = fields.Char(string='Password',
                                     help="Optional password for Outgoing Mail Servers authentication", copy=False)
    mail_server_id = fields.Many2one('ir.mail_server', 'Outgoing Mail Server', copy=False, readonly=True)
    incoming_fetch_mail_server_id = fields.Many2one('fetchmail.server', 'Incoming Mail Server', copy=False,
                                                    readonly=True)

    @api.model
    def create(self, vals):
        if vals.get('outgoing_smtp_user', False) and vals.get('outgoing_smtp_pass', False):
            mail_server_id = self.env['ir.mail_server'].create({
                'name': str(vals['name']) + ' Outgoing Mail Servers',
                'from_filter': str(vals['outgoing_smtp_user']).strip(''),
                'smtp_host': 'smtp.gmail.com',
                'smtp_port': 465,
                'smtp_encryption': 'ssl',
                'smtp_user': vals['outgoing_smtp_user'],
                'smtp_pass': vals['outgoing_smtp_pass'],
            })
            mail_server_id.test_smtp_connection()
            vals.update({'mail_server_id': mail_server_id.id})
        # else:
        #     raise UserError(_('Please set Username and Password for %s Outgoing Mail Servers.', vals['name']))
        res = super(Users, self).create(vals)
        return res

    def write(self, values):
        print('self', self._context)
        if not self.mail_server_id:
            mail_server_id = self.env['ir.mail_server'].sudo().search(
                [('smtp_user', '=', self.login), ('from_filter', '=', self.login)])
        else:
            mail_server_id = self.mail_server_id
        if values.get('outgoing_smtp_user', False):
            if not mail_server_id:
                mail_server_id = self.env['ir.mail_server'].create({
                    'name': str(self.name) + ' Outgoing Mail Servers',
                    'from_filter': str(values['outgoing_smtp_user']).strip(''),
                    'smtp_host': 'smtp.gmail.com',
                    'smtp_port': 465,
                    'smtp_encryption': 'ssl',
                    'smtp_user': values['outgoing_smtp_user'],
                })
            mail_server_id.write({'smtp_user': values['outgoing_smtp_user']})
        if values.get('outgoing_smtp_pass', False):
            mail_server_id.write({'smtp_pass': values['outgoing_smtp_pass']})
        if values.get('outgoing_smtp_pass', False) or values.get('outgoing_smtp_user', False):
            mail_server_id.test_smtp_connection()
            values.update({'mail_server_id': mail_server_id.id})
        res = super().write(values)
        return res

    def create_incoming_mail_server(self):
        for user in self:
            # mail_server_id = self.env['fetchmail.server'].create({
            #     'name': str(user.name) + ' Incoming Mail Servers',
            #     'server_type': 'pop',
            #     'server': 'pop.gmail.com',
            #     'port': 995,
            #     'is_ssl': True,
            #     'user': user.outgoing_smtp_user,
            #     'password': user.outgoing_smtp_pass,
            # })
            if user.mail_server_id and not user.incoming_fetch_mail_server_id:
                mail_server_id = self.env['fetchmail.server'].create({
                    'name': str(user.name) + ' Incoming Mail Servers IMAP',
                    'server_type': 'imap',
                    'server': 'imap.gmail.com',
                    'port': 993,
                    'is_ssl': True,
                    'user': user.outgoing_smtp_user,
                    'password': user.outgoing_smtp_pass,
                })
                mail_server_id.button_confirm_login()
                user.write({'incoming_fetch_mail_server_id': mail_server_id.id})
