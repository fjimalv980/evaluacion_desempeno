from odoo import models, fields, api
from odoo.exceptions import ValidationError

class EvaluacionDesempeno(models.Model):
    _name = 'evaluacion.desempeno'
    _description = 'Evaluación del desempeño del Empleado'

    name = fields.Char(string='Evaluación de desempeño', required=True)
    description = fields.Text(string='Comentarios')
    assigned_to = fields.Many2one('hr.employee', string='Empleado')
    evaluation_date = fields.Date(string='Fecha de Evaluación', required=True)
    state = fields.Selection([
        ('draft', 'Pendiente'),
        ('in_progress', 'En Progreso'),
        ('done', 'Finalizado'),
    ], string='Estado', default='draft')
    score = fields.Integer(string='Puntuación', required=True, help='Puntuación del 1 al 10')

    @api.constrains('score')
    def _check_score(self):
        for record in self:
            if record.score < 1 or record.score > 10:
                raise ValidationError("La puntuación debe estar entre 1 y 10")

    def iniciar_evaluacion(self):
        self.write({'state': 'in_progress'})

    def finalizar_evaluacion(self):
        self.write({'state': 'done'})