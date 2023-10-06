# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "HR - Issue In Timesheets",
    "version": "10.0.1.0.0",
    "category": "HR",
    "summary": "Allow the user to select issue in a timesheet",
    "author": "SHS-AV s.r.l.",
    "website": "https://www.zeroincombenze.it/crm",
    "development_status": "Alpha",
    "license": "AGPL-3",
    "depends": [
        "project_issue_sheet",
        "hr_timesheet_task",
    ],
    "data": ["views/hr_timesheet_view.xml"],
    "maintainer": "Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>",
    "installable": True,
    "application": False,
}
