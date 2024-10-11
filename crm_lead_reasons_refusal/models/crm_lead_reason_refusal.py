# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields

class LeadRejectionReason(models.Model):
    _name = 'lead.rejection.reason'
    _description = 'Lead Rejection Reason'

    name = fields.Char(string='Reason', required=True)


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    rejection_reason_id = fields.Many2one(
        'lead.rejection.reason',
        string='Rejection Reason',
        help='Reason for rejecting the lead.'
    )






