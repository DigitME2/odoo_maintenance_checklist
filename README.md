# Odoo Maintenance Scheduler

This module creates another type of maintenance request, a recurring request. If one of these is created, new maintenance requests will automatically be entered according to the rules in the recurring request

A new request will be created if:
 - A recurring request is set
 - There isn't a matching request marked as "done" within the recurring request period
 - There isn't an existing matching request, marked as "pending" or "overdue"

Developed for Odoo 15

# Installation

Add the module folder to Odoo's addon directory. In the Docker container this is /mnt/extra-addons

In Odoo, activate developer mode. Go to the apps list and click "Update Apps List" in the toolbar.
This addon is called Maintenance Scheduler. You may need to remove the "Apps" filter from the search bar.

When using the Maintenance app, there will now be another option under "Maintenance" in the toolbar: Recurring Maintenance.