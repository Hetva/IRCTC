# -*- coding: utf-8 -*-

from odoo import models, fields


class passengers_model(models.Model):

    _name='passengers.model'
    _description='passengers_model_description'
    _rec_name='passengers_name'

    passengers_id = fields.Char('ID')
    passengers_name=fields.Char('Name')
    passengers_age=fields.Integer('Age')
    passengers_dob = fields.Integer('DOB')
    passengers_gender = fields.Char('Gender')
    passengers_contact = fields.Integer('Contact')
    passengers_email=fields.Char('Email')
    # passengers_address = fields.Char('Address')
    # passengers_pincode = fields.Integer('PIN Code')




