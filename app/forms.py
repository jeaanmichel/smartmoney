from flask_wtf import FlaskForm
from wtforms import StringField, validators, SelectField, RadioField, IntegerField


class MovimentacaoForm(FlaskForm):
    nome_compra = StringField('Movimentacao', validators=[validators.required(message="Prencha este campo"),
                                                             validators.Length(min=1, max=50)])
    data_compra = StringField('Data', validators=[validators.required(),
                                                            validators.Length(min=1, max=10)])
    tipo_movimentacao = SelectField('Tipo da Movimentacao', choices=[("0", "Receita"), ("1", "Despesa")])
    valor_compra = StringField('Valor R$', validators=[validators.required(),
                                                                  validators.Length(min=1, max=20)])
    tipo_compra = SelectField('Pagamento', choices=[("0", "Cartao"),
                                                          ("1", "Dinheiro"),
                                                          ("2", "Debito")])
    tipo_parcela = RadioField('Tipo parcela', choices=[("0", "Varias parcelas"), ("1", "Parcela unica"),
                                                       ("2", "Parcela fixa")], default="1")
    total_parcelas = IntegerField('Total de parcelas')
    valor_parcela = StringField('Valor da parcela R$')
