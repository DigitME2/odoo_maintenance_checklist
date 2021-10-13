from odoo import models, fields, api


class MaintenanceExtension(models.Model):

    _inherit = "maintenance.equipment"

    repeat_frequency = fields.Char(string="Repeat Frequency (days)")


    # @api.model
    # def create(self, vals):
    #     #todo Add maintenance requests according to frequency
    #     return super(MaintenanceExtension, self).create(vals)
