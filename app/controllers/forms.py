from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, FileField, DateField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from flask_wtf.file import FileRequired, FileAllowed

from app.models.usuario import Usuario


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    lembrar_me = BooleanField('Lembrar-me')
    acessar = SubmitField('Acessar')


class RegistrationForm(FlaskForm):
    nome = StringField('Nome*', validators=[DataRequired()])
    nascimento = DateField('Nascimento*')
    telefone = StringField('Telefone*')
    cpf = StringField('CPF*')

    email = StringField('Email*', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha*', validators=[DataRequired()])
    confirmar_senha = PasswordField(
        'Confirmar Senha*',
        validators=[DataRequired(), EqualTo('senha')]
    )

    cep = StringField('CEP*')
    logradouro = StringField('Logradouro*')
    numero = StringField('Número*')
    complemento = StringField('Complemento')
    referencia = StringField('Ponto de Referência')
    bairro = StringField('Bairro*')
    cidade = StringField('Cidade*')
    estado = StringField('Estado*')

    cadastrar = SubmitField('Cadastrar-se')

    def validar_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()

        if usuario is not None:
            raise ValidationError(
                'Este email já está em uso. Escolha um email diferente e tente novamente.')

class EditarDadosUsuarioForm(FlaskForm):
    nome = StringField('Nome*', validators=[DataRequired()])
    nascimento = DateField('Nascimento*')
    telefone = StringField('Telefone*')
    cpf = StringField('CPF*')

    email = StringField('Email*', validators=[DataRequired(), Email()])
    senha_atual = PasswordField('Senha atual*')
    nova_senha = PasswordField('Nova senha*')
    confirmar_nova_senha = PasswordField(
        'Confirmar nova senha*',
        validators=[EqualTo('nova_senha')]
    )

    cep = StringField('CEP*')
    logradouro = StringField('Logradouro*')
    numero = StringField('Número*')
    complemento = StringField('Complemento')
    referencia = StringField('Ponto de Referência')
    bairro = StringField('Bairro*')
    cidade = StringField('Cidade*')
    estado = StringField('Estado*')

    editarDadosUsuario = SubmitField('Salvar Alterações')


class CadastroProdutoForm(FlaskForm):
    descricao = StringField('Nome Produto', validators=[DataRequired()])
    quantidade = StringField('Quantidade', validators=[DataRequired()])
    preco = StringField('R$ Preço', validators=[DataRequired()])
    cadastrarProduto = SubmitField('Cadastrar Produto')


class EditarDadosProdutoForm(FlaskForm):
    descricao = StringField('Nome Produto', validators=[DataRequired()])
    quantidade = StringField('Quantidade', validators=[DataRequired()])
    preco = StringField('R$ Preço', validators=[DataRequired()])
    editarDadosProduto = SubmitField('Salvar Alterações')
