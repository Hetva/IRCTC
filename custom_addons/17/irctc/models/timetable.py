# # -*- coding: utf-8 -*-
from odoo import models, fields

class TimetableModel(models.Model):

    _name = 'timetable.model'
    _description = 'Timetable Model'

    train_id = fields.Char('Train ID')
    train_name_id=fields.Many2one("train.model", string="Train Name")
    station_name = fields.Char('Arrival')
    train_arrival_time = fields.Char('Arrival Time')
    train_arrival_date = fields.Date('Arrival Date')
    train_halt_time = fields.Char('Halt Time')
    train_departs = fields.Char('Departs')
    train_departs_time = fields.Char('Departs Time')
    train_departs_date = fields.Date('Departs Date')
