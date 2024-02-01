# -*- coding: utf-8 -*-

from odoo import models, fields
# from . import booking
class train_model(models.Model):

    _name='train.model'
    _description='train_model_description'
    _rec_name = 'train_name'

    train_id = fields.Char('Train ID')
    train_name=fields.Char('Train Name')
    train_arrival_id=fields.Many2one("station.model", string='Arrival')
    train_arrival_time = fields.Char('Arrival Time')
    train_arrival_date = fields.Date('Arrival Date')
    train_destination_id = fields.Many2one("station.model", string='Destination')
    train_destination_time = fields.Char('Destination Time')
    train_destination_date = fields.Date('Destination Date')
    route=fields.One2many("timetable.model",'train_name_id', string="Route")
    # route_ids = fields.Many2many("station.model",'station_name', string="Route")
    ticket_data=fields.One2many('booking.model','booking_train_id',string='Passengers')
    # (comodel_name='booking.model', inverse_name=('booking_id', 'booking_train'), string = 'detail')
    # train_id=fields.Char('id of train')
    # train_class=fields.
