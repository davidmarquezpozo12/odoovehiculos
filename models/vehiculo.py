from odoo import models, fields


class Vehiculo(models.Model):
    """Modelo para la gestión de vehículos."""
    _name = 'vehiculo.management'
    _description = 'Gestión de vehículos'
    _rec_name = 'matricula'
    _order = 'matricula'

    matricula = fields.Char(string='Matrícula', required=True, index=True)
    marca = fields.Char(string='Marca', required=True, index=True)
    modelo = fields.Char(string='Modelo', required=True)
    activo = fields.Boolean(string='¿Activo?', default=True, index=True)

    _sql_constraints = [
        ('matricula_uniq', 'unique(matricula)', 'La matrícula debe ser única.'),
    ]
