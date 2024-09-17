from odoo import fields, models, api

class Experience_wizard(models.TransientModel):
    _name = 'experience.wizard'
    _description = 'Update years of experience for employees'
    # employee_ids = fields.Many2many('hr.employee', string="Employees")
    years_of_experience = fields.Integer(string="Years of Experience")
    # message = fields.Text(string="Message", default="Apply updating on the selected record(s)?")
    

    def set_experience(self):
        ids = self.env.context.get('active_ids')
        employees = self.env['hr.employee'].browse(ids)
        for employee in employees:
            employee.years_of_experience = self.years_of_experience