from utils import db


class Produto(db.Model):
    __tablename__ = 'pedidos'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    categoria = db.Column(db.String(200))
    quantidade = db.Column(db.Integer)
    valor = db.Column(db.Float)


    def __init__(self, nome, categoria, quantidade, valor):
        self.nome = nome
        self.categoria = categoria
        self.quantidade = quantidade
        self.valor = valor
    
    def __repr__(self):
        return "<Pedido {} - {} - {} - {}>".format(self.pedido.nome, self.pedido.categoria, self.pedido.quantidade, self.pedido.valor)