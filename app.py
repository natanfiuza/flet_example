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
    page.bgcolor = ''
    lista_produtos = ft.ListView()
  
    def cadastrar(e):
        try: 
            novo_produto = Produto(titulo=produto.value, preco=preco.value)
            session.add(novo_produto)
            session.commit()
            print('Produto salvo!!')
            lista_produtos.controls.append(
                ft.Container(
                    ft.Text(produto.value),
                    bgcolor=ft.colors.BLACK12,
                    padding=15,
                    alignment=ft.alignment.center,
                    margin=3,
                    border_radius=10,
                )
            )
            produto.value = ''
            preco.value = ''
            txt_error.visible = False
            txt_acerto.visible = True
        except:    
            txt_error.visible = True
            txt_acerto.visible = False
        page.update()


    txt_error = ft.Container(ft.Text('Erro ao cadastrar o produto!!'), visible=False, bgcolor=ft.colors.RED,padding=10, alignment=ft.alignment.center)
    txt_acerto = ft.Container(ft.Text('Produto salvo com sucesso!!'), visible=False, bgcolor=ft.colors.GREEN,padding=10, alignment=ft.alignment.center)
    txt_titulo = ft.Text('Cadastro do Produto')    
    page.add(txt_titulo)
    
    produto = ft.TextField(label="Titulo do produto",text_align=ft.TextAlign.LEFT)
    preco = ft.TextField(label="Preço",text_align=ft.TextAlign.LEFT)

    btn_cadastrar = ft.ElevatedButton('Cadastrar', on_click=cadastrar)
    page.add(
        txt_error,
        txt_acerto,
        produto,
        preco,
        btn_cadastrar
    )
    for p in session.query(Produto).all():
        lista_produtos.controls.append(
            ft.Container(
                ft.Text(p.titulo),
                bgcolor=ft.colors.BLACK12,
                padding=15,
                alignment=ft.alignment.center,
                margin=3,
                border_radius=10,
            )
        )
    page.add(
        lista_produtos,
    )
ft.app(target=main)