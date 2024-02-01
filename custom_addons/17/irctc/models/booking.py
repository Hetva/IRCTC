# -*- coding: utf-8 -*-

from odoo import models, fields
# from . import train

class booking_model(models.Model):

    _name='booking.model'
    _description='booking_model_description'
    _rec_name='booking_train_id'

    passenger_name_id=fields.Many2one('passengers.model',string='Passenger Name')
    ticket_id=fields.Char('Ticket Id')
    booking_train_id=fields.Many2one('train.model',string="Train Name")
    booking_start_station_id=fields.Many2one('station.model', string='Arrival')
    booking_dest_id=fields.Many2one('station.model', string='Destination')
    coach_number = fields.Char('Coach No.')
    seat_number = fields.Char('Seat No.')
    ticket_payment=fields.Boolean('Payment Details')
    # ticket_payment=fields.Char('Payment Details')

