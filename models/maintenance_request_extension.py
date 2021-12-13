# -*- coding: utf-8 -*-
from odoo import models, fields


class RecurringMaintenance(models.Model):

    _inherit = "maintenance.request"
    _description = "recurring.maintenance"

    # The ID of the recurring maintenance request that created this request
    recurring_maintenance_id = fields.Integer()
    repeat_frequency = fields.Integer(string="Repeat Frequency")
    repeat_units = fields.Selection([("daily", "Days"),
                                     ("weekly", "Weeks"),
                                     ("monthly", "Months"), ],
                                    string="Repeat Frequency Units",
                                    copy=False)
