# -*- coding: utf-8 -*-
from odoo import http


class MaintenanceScheduler(http.Controller):
    @http.route('/maintenance_scheduler/test/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/maintenance_scheduler/recurring_maintenance/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('maintenance_checklist.listing', {
            'root': '/maintenance_checklist/maintenance_checklist',
            'objects': http.request.env['maintenance_checklist.maintenance_checklist'].search([]),
        })

    @http.route('/maintenance_checklist/maintenance_checklist/objects/', auth='public')
    def list2(self, **kw):
        return http.request.render('maintenance_checklist.listing', {
            'root': '/maintenance_checklist/maintenance_checklist',
            'objects': http.request.env['maintenance_checklist.maintenance_checklist'].search([]),
        })

    @http.route('/maintenance_checklist/maintenance_checklist/objects/<model("maintenance_checklist.maintenance_checklist"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('maintenance_checklist.object', {
            'object': obj
        })
