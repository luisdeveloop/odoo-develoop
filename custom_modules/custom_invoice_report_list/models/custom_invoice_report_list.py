# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import logging
from odoo import api, fields, models, exceptions, SUPERUSER_ID, _
from odoo.exceptions import AccessError, UserError, ValidationError
from odoo.tools import float_is_zero, float_compare
_logger = logging.getLogger(__name__)

class InvoiceReportListCustom(models.Model):

    _inherit = 'account.invoice.report'

    x_amount_untaxed_signed = fields.Monetary("Impuesto no incluido", compute="get_datas")
    x_amount_tax_signed = fields.Monetary(string='Impuesto', compute="get_datas")
    x_amount_total_signed = fields.Monetary(string='Total', compute="get_datas")
    x_residual_signed = fields.Monetary(string='Importe adeudado', compute="get_datas")


    def get_datas(self):
        for invoice in self:
            invoice.x_amount_untaxed_signed = invoice.invoice_id.amount_untaxed_signed
            invoice.x_amount_tax_signed = invoice.invoice_id.amount_tax
            invoice.x_amount_total_signed = invoice.invoice_id.amount_total_signed
            invoice.x_residual_signed = invoice.invoice_id.residual_signed


    @api.model
    def search_read(self, domain=None, fields=None, offset=0, limit=None, order=None):
        #data2 = super().search_read(domain=domain, fields=fields, offset=offset, limit=limit, order=order)
        if self._context.get('from_action', False) and self._context.get('from_action') == 'custom':
            # if self._context.get('params', False) == False or \
            #     (self._context.get('params',False) and self._context.get('params').get('view_type',False) and self._context.get('params').get('view_type') == 'list'):
            data = self.env['account.invoice.report2'].sudo().search_read(domain=domain, fields=fields, offset=offset, limit=limit, order=order)
            toreturn = []
            for record in data:
                new_data = {
                    'id': record.get('id', False),
                    'partner_id': record.get('partner_id', False),
                    'date': record.get('date',False),
                    'number': record.get('number',False),
                    'user_id': record.get('user_id',False),
                    'date_due': record.get('date_due',False),
                    'currency_id': record.get('currency_id',False),
                    'state': record.get('state',False),
                    'x_amount_untaxed_signed': record.get('x_amount_untaxed_signed',False),
                    'x_amount_tax_signed': record.get('x_amount_tax_signed',False),
                    'x_amount_total_signed': record.get('x_amount_total_signed',False),
                    'x_residual_signed': record.get('x_residual_signed',False),

                    'product_id': record.get('product_id',False),
                    'product_qty': record.get('product_qty',False),
                    'uom_name': record.get('uom_name',False),
                    'payment_term_id': record.get('payment_term_id', False),
                    'fiscal_position_id': record.get('fiscal_position_id', False),
                    'currency_id': record.get('currency_id',False),
                    'categ_id': record.get('categ_id',False),
                    'journal_id': record.get('categ_id',False),
                    'partner_id': record.get('partner_id',False),
                    'commercial_partner_id': record.get('commercial_partner_id',False),
                    'company_id': record.get('company_id',False),
                    'user_id': record.get('user_id',False),
                    'price_total': record.get('price_total',False),
                    'user_currency_price_total': record.get('user_currency_price_total',False),
                    'price_average': record.get('price_average',False),
                    'user_currency_price_average': record.get('user_currency_price_average',False),
                    'currency_rate': record.get('currency_rate',False),
                    'nbr': record.get('nbr',False),
                    'invoice_id': record.get('invoice_id',False),
                    'type': record.get('type',False),
                    'state': record.get('state',False),
                    'date_due': record.get('date_due',False),
                    'account_id': record.get('account_id',False),
                    'account_line_id': record.get('account_line_id',False),
                    'partner_bank_id': record.get('partner_bank_id',False),
                    'residual': record.get('residual',False),
                    'user_currency_residual': record.get('user_currency_residual',False),
                    'country_id': record.get('country_id',False),
                    'account_analytic_id': record.get('account_analytic_id',False),
                    'amount_total': record.get('amount_total',False),

                    'x_amount_untaxed_signed': record.get('x_amount_untaxed_signed',False),
                    'x_amount_tax_signed': record.get('x_amount_tax_signed',False),
                    'x_amount_total_signed': record.get('x_amount_total_signed',False),
                    'x_residual_signed': record.get('x_residual_signed',False),
                }
                toreturn.append(new_data)
            return toreturn
        else:        
            return super().search_read(domain=domain, fields=fields, offset=offset, limit=limit, order=order)