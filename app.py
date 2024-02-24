import flet as ft
from models import Produto
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

connection_string =  "sqlite:///base_projeto.db"

engine = create_engine(connection_string, echo = True)
Session = sessionmaker(bind=engine)
session = Session()



def main(page: ft.Page):
    page.title = "Cadastro Produto Exemplo"
    page.bgcolor = 'white'
    lista_produtos = ft.ListView()
  
    def cadastrar(e):
      novo_produto = Produto(titulo=produto.value, preco=preco.value)
      session.add(novo_produto)
      session.commit()
      print('Produto salvo!!')
      produto.value = ''

    txt_titulo = ft.Text('Cadastro do Produto')    
    page.add(txt_titulo)
    
    produto = ft.TextField(label="Titulo do produto",text_align=ft.TextAlign.LEFT)
    preco = ft.TextField(label="Preço",text_align=ft.TextAlign.LEFT)

    btn_cadastrar = ft.ElevatedButton('Cadastrar', on_click=cadastrar)
    page.add(produto,preco,btn_cadastrar)
    for p in session.query(Produto).all():
        lista_produtos.controls.append(ft.Text(p.titulo))
    page.add(
        lista_produtos,
    )
ft.app(target=main)