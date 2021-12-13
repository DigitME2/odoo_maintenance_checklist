# -*- coding: utf-8 -*-
from datetime import datetime, timedelta

from odoo import models, fields

PENDING_STAGE = 1
DONE_STAGE = 2


class RecurringMaintenance(models.Model):
    _name = "recurring.maintenance"
    _inherit = "maintenance.request"
    _description = "recurring.maintenance"

    repeat_frequency = fields.Integer(string="Repeat Frequency")
    repeat_units = fields.Selection([("daily", "Days"),
                                     ("weekly", "Weeks"),
                                     ("monthly", "Months"), ],
                                    string="Repeat Frequency Units",
                                    copy=False)

    def create_maintenance_requests(self):
        now = datetime.now()
        self.repeat_units = "4"

        # Get all of the recurring requests
        recurring_requests = self.search([])
        for recurring_request in recurring_requests:

            # Check if there is a completed request in the eligible time period
            if recurring_request.repeat_units == "daily":
                days = recurring_request.repeat_frequency
            elif recurring_request.repeat_units == "monthly":
                days = recurring_request.repeat_frequency * 7
            elif recurring_request.repeat_units == "monthly":
                days = recurring_request.repeat_frequency * 30
            else:
                days = 0

            last_eligible_date = (now - timedelta(days=days)).date()
            domain = [
                ('recurring_maintenance_id', "=", recurring_request.id),
                ('stage_id', '=', DONE_STAGE),
                ('close_date', '>', last_eligible_date.strftime("%Y-%m-%d")),
            ]
            completed_requests = self.env['maintenance.request'].search(args=domain)
            if completed_requests:
                continue

            # Check if there is already a pending request
            domain = [
                ('recurring_maintenance_id', "=", recurring_request.id),
                ('stage_id', 'in', [PENDING_STAGE])
            ]
            pending_requests = self.env['maintenance.request'].search(args=domain)
            if pending_requests:
                continue

            self.env['maintenance.request'].create({
                'name': recurring_request.name,
                'request_date': now,
                'schedule_date': now,
                'category_id': recurring_request.category_id.id,
                'maintenance_type': 'preventive',
                'recurring_maintenance_id': recurring_request.id,
                'user_id': recurring_request.user_id.id,
                'maintenance_team_id': recurring_request.maintenance_team_id.id,
                'repeat_frequency': recurring_request.repeat_frequency,
                'repeat_units': recurring_request.repeat_units
            })
