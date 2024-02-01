# -*- coding: utf-8 -*-

from odoo import models, fields



class station_model(models.Model):

    _name='station.model'
    _description='station_model_description'
    _rec_name = 'station_name'

    station_name=fields.Char('station name')
    # station_city=fields.Char('city')
    # station_state=fields.Char('state')
    # station_id=fields.Char('id of station')
