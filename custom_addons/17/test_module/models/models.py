# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo import fields, models

class Student(models.Model):
    _name = "wb.student"
    _description = "This is test_module profile."

    name = fields.Char("Name")
    # name1 = fields.Char("RollNo.")
    name2 = fields.Char("Subjects")
    name3 = fields.Char("Marks")
    name4 = fields.Char("Address")
    name5 = fields.Char("Division")
    value = fields.Integer("RollNo.")



# class new_module(models.Model):
#     _name = 'new_module.new_module'
#     _description = 'new_module.new_module'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

