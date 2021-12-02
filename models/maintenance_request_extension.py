# -*- coding: utf-8 -*-
from odoo import models, fields


class RecurringMaintenance(models.Model):

    _inherit = "maintenance.request"
    _description = "recurring.maintenance"

    # The ID of the recurring maintenance request that created this request
    recurring_maintenance_id = fields.Integer()
