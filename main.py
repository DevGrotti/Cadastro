# Matheus Grotti Pereira / RA 310446 / GTI

# manipulação de interface gráfica
from tkinter import *
from tkinter import Tk, StringVar, ttk
from tkinter import messagebox
from tkinter import filedialog as fd


# processador de imagens
from PIL import Image, ImageTk

# calendário e entrada de data
from tkcalendar import Calendar, DateEntry
from datetime import date

#importando view
from view import *

cor1 = "#feffff" # branco
cor2 = "#4fa882" # verde
cor3 = "#38576b" # valor
cor4 = "#403d3d" # letra
cor5 = "#e06636" # profit
cor6 = "#038cfc" # azul
cor7 = "#3fbfb9" # verde
cor8 = "#263238" # mais verde
cor9 = "#e9edf5" # mais verde 2


# criando janela

janela = Tk()
janela.title("")
janela.geometry("900x600")
janela.configure(background=cor9)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use("clam")


# criando frames

frameCima = Frame(janela, width=1043, height=50, bg=cor1, relief=FLAT)
frameCima.grid(row=0, column=0)

frameMeio = Frame(janela, width=1043, height=303, bg=cor1, pady=20, relief=FLAT)
frameMeio.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frameBaixo = Frame(janela, width=1043, height=300, bg=cor1, relief=FLAT)
frameBaixo.grid(row=2, column=0, pady=0, padx=1, sticky=NSEW)


# criando funcoes
global tree

# funcao inserir
def inserir():
    global imagem, imagem_string, l_imagem

    nome = entrada_nome.get()
    genero = entrada_genero.get()
    altura = entrada_altura.get()
    peso = entrada_peso.get()
    datanasc = entrada_calendario.get()
    naturalidade = entrada_local.get()
    hobbies = entrada_hobbies.get()
    imagem = imagem_string

    lista_inserir = [nome, genero, altura, peso, datanasc, naturalidade, hobbies, imagem]

    for i in lista_inserir:
        if i=='':
            messagebox.showerror("Erro", "Preencha todos os campos")
            return
        
    inserir_form(lista_inserir)

    messagebox.showinfo("Sucesso", "Os dados foram adicionados com sucesso")

    entrada_nome.delete(0, "end")
    entrada_genero.delete(0, "end")
    entrada_altura.delete(0, "end")
    entrada_peso.delete(0, "end")
    entrada_calendario.delete(0, "end")
    entrada_local.delete(0, "end")
    entrada_hobbies.delete(0, "end")


    mostrar()

# funcao update

def atualizar():
    global imagem, imagem_string, l_imagem
    # tentar executar
    try:
        # funcao .focus() para focar em um único item, pegar o id dele e executar a tentativa
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario["values"]

        valor = treev_lista[0]

        entrada_nome.delete(0, "end")
        entrada_genero.delete(0, "end")
        entrada_altura.delete(0, "end")
        entrada_peso.delete(0, "end")
        entrada_calendario.delete(0, "end")
        entrada_local.delete(0, "end")
        entrada_hobbies.delete(0, "end")

        id = int(treev_lista[0])
        entrada_nome.insert(0, treev_lista[1])
        entrada_local.insert(0, treev_lista[2])
        entrada_genero.insert(0, treev_lista[3])
        entrada_calendario.insert(0, treev_lista[4])
        entrada_altura.insert(0, treev_lista[5])
        entrada_peso.insert(0, treev_lista[6])
        entrada_hobbies.insert(0, treev_lista[7])
        imagem_string = treev_lista[8]


        def update():
            global imagem, imagem_string, l_imagem

            nome = entrada_nome.get()
            genero = entrada_genero.get()
            altura = entrada_altura.get()
            peso = entrada_peso.get()
            datanasc = entrada_calendario.get()
            naturalidade = entrada_local.get()
            hobbies = entrada_hobbies.get()
            imagem = imagem_string

            if imagem =="":
                imagem = entrada_hobbies.insert(0, treev_lista[7])

            lista_att = [nome, genero, altura, peso, datanasc, naturalidade, hobbies, imagem, id]

            for i in lista_att:
                if i=="":
                    messagebox.showerror("Erro", "Preencha todos os campos")
                    return
                
            atualizar_(lista_att)
            messagebox.showinfo("Sucesso", "Os dados foram atualizados com sucesso")

            entrada_nome.delete(0, "end")
            entrada_genero.delete(0, "end")
            entrada_altura.delete(0, "end")
            entrada_peso.delete(0, "end")
            entrada_calendario.delete(0, "end")
            entrada_local.delete(0, "end")
            entrada_hobbies.delete(0, "end")

            botao_confirmar.destroy()

            mostrar()

        botao_confirmar = Button(frameMeio, command=update, width=13, text="  Confirmar".upper(), overrelief=RIDGE, font=("Ivy 8 bold"), bg=cor2, fg=cor1)
        botao_confirmar.place(x=331, y=185)

    # exceto quando houver *erro de indexação* (usuário não selecionou um dado na tabela)
    except IndexError:
        messagebox.showerror("Erro", "Selecione um dos dados na tabela")


# funcao deletar
def deletar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario["values"]
        valor = treev_lista[0]

        deletar_form([valor])

        messagebox.showinfo("Sucesso", "Os dados foram deletados com sucesso")

        mostrar()

    except IndexError:
        messagebox.showerror("Erro", "Selecione um dos dados na tabela")



# funcao upload da imagem
global imagem, imagem_string, l_imagem

def escolher_imagem():
    global imagem, imagem_string, l_imagem

    imagem = fd.askopenfilename()
    imagem_string = imagem

    # abrindo imagem
    imagem = Image.open(imagem)
    imagem = imagem.resize((325,250))
    imagem = ImageTk.PhotoImage(imagem)


    label_imagem = Label(frameMeio, image=imagem, bg=cor1, fg=cor4)
    label_imagem.place(x=515, y=2)



# funcao ver foto
def ver_foto():
    global imagem, imagem_string, l_imagem

    treev_dados = tree.focus()
    treev_dicionario = tree.item(treev_dados)
    treev_lista = treev_dicionario["values"]

    valor = [int(treev_lista[0])]

    foto = ver_item(valor)

    imagem = foto[0][8]

    imagem = Image.open(imagem)
    imagem = imagem.resize((325,250))
    imagem = ImageTk.PhotoImage(imagem)


    label_imagem = Label(frameMeio, image=imagem, bg=cor1, fg=cor4)
    label_imagem.place(x=515, y=2)




# abrindo imagem

app_img = Image.open("IconeFormulario.png")
app_img = app_img.resize((45,45))
app_img = ImageTk.PhotoImage(app_img)


# criando a label "Cadastro"
app_logo = Label(frameCima, image=app_img, text=" Cadastro", width=900, compound=LEFT, relief=RAISED, anchor=NW, font=("Verdana 20 bold"), bg=cor1, fg=cor4)
app_logo.place(x=0, y=0)



# trabalhando no frame central

# label grotti
label_grotti = Label(frameCima, text="by Grotti", height=1, anchor=NW, font=("Ivy 10 bold italic"), bg=cor1, fg=cor4)
label_grotti.place(x=835, y=1)

# criando entradas

# entrada nome
label_nome = Label(frameMeio, text="Nome", height=1, anchor=NW, font=("Ivy 10 bold"), bg=cor1, fg=cor4)
label_nome.place(x=10, y=10)
entrada_nome = Entry(frameMeio, width=30, justify="left", relief=SOLID)
entrada_nome.place(x=130, y=11)


# entrada local
label_local = Label(frameMeio, text="Naturalidade", height=1, anchor=NW, font=("Ivy 10 bold"), bg=cor1, fg=cor4)
label_local.place(x=10, y=40)
entrada_local = Entry(frameMeio, width=30, justify="left", relief=SOLID)
entrada_local.place(x=130, y=41)


# entrada genero
label_genero = Label(frameMeio, text="Gênero", height=1, anchor=NW, font=("Ivy 10 bold"), bg=cor1, fg=cor4)
label_genero.place(x=10, y=70)
entrada_genero = Entry(frameMeio, width=30, justify="left", relief=SOLID)
entrada_genero.place(x=130, y=71)


# entrada data de nascimento
label_calendario = Label(frameMeio, text="Nascimento", height=1, anchor=NW, font=("Ivy 10 bold"), bg=cor1, fg=cor4)
label_calendario.place(x=10, y=100)
entrada_calendario = DateEntry(frameMeio, width=12, Background="darkblue", bordewidth=2, year=2023, relief=SOLID)
entrada_calendario.place(x=130, y=101)


# entrada altura
label_altura = Label(frameMeio, text="Altura (cm)", height=1, anchor=NW, font=("Ivy 10 bold"), bg=cor1, fg=cor4)
label_altura.place(x=10, y=130)
entrada_altura = Entry(frameMeio, width=30, justify="left", relief=SOLID)
entrada_altura.place(x=130, y=131)


# entrada peso
label_peso = Label(frameMeio, text="Peso (KG)", height=1, anchor=NW, font=("Ivy 10 bold"), bg=cor1, fg=cor4)
label_peso.place(x=10, y=160)
entrada_peso = Entry(frameMeio, width=30, justify="left", relief=SOLID)
entrada_peso.place(x=130, y=161)


# entrada hobbies
label_hobbies = Label(frameMeio, text="Hobbies", height=1, anchor=NW, font=("Ivy 10 bold"), bg=cor1, fg=cor4)
label_hobbies.place(x=10, y=190)
entrada_hobbies = Entry(frameMeio, width=30, justify="left", relief=SOLID)
entrada_hobbies.place(x=130, y=191)


# criando botoes

# botao de upload

# abrindo icone upload
img_upload = Image.open("uploadbutton.png")
img_upload = img_upload.resize((20,20))
img_upload = ImageTk.PhotoImage(img_upload)

# label upload
label_foto = Label(frameMeio, text="Foto 3x4", height=1, anchor=NW, font=("Ivy 10 bold"), bg=cor1, fg=cor4)
label_foto.place(x=10, y=225)

# botao de upload
botao_foto = Button(frameMeio, command=escolher_imagem, image=img_upload, width=177, text="           Fazer Upload".upper(), compound=LEFT, anchor=NW, overrelief=RIDGE, font=("Ivy 8"), bg=cor1, fg=cor4)
botao_foto.place(x=130, y=221)

# botao inserir

# abrindo icone adicionar
img_add = Image.open("addbutton.png")
img_add = img_add.resize((20,20))
img_add = ImageTk.PhotoImage(img_add)

# botao adicionar
botao_add = Button(frameMeio, command=inserir, image=img_add, width=95, text="  Adicionar".upper(), compound=LEFT, anchor=NW, overrelief=RIDGE, font=("Ivy 8"), bg=cor1, fg=cor4)
botao_add.place(x=330, y=10)

# botao atualizar

# abrindo icone de update
img_att = Image.open("attbutton.png")
img_att = img_att.resize((20,20))
img_att = ImageTk.PhotoImage(img_att)

# botao de update
botao_att = Button(frameMeio, command=atualizar, image=img_att, width=95, text="  Atualizar".upper(), compound=LEFT, anchor=NW, overrelief=RIDGE, font=("Ivy 8"), bg=cor1, fg=cor4)
botao_att.place(x=330, y=50)

# botao deletar

# abrindo icone deletar
img_del = Image.open("deletebutton.png")
img_del = img_del.resize((20,20))
img_del = ImageTk.PhotoImage(img_del)

# botao deletar
botao_del = Button(frameMeio, command=deletar, image=img_del, width=95, text="  Deletar".upper(), compound=LEFT, anchor=NW, overrelief=RIDGE, font=("Ivy 8"), bg=cor1, fg=cor4)
botao_del.place(x=330, y=90)

# botao ver foto

# abrindo icone ver foto
img_fotoview = Image.open("fotoview.png")
img_fotoview = img_fotoview.resize((20,20))
img_fotoview = ImageTk.PhotoImage(img_fotoview)

# botao ver foto
botao_del = Button(frameMeio, command=ver_foto, image=img_fotoview, width=95, text="  Ver foto".upper(), compound=LEFT, anchor=NW, overrelief=RIDGE, font=("Ivy 8"), bg=cor1, fg=cor4)
botao_del.place(x=330, y=221)


# criando tabela head
def mostrar():
    global tree

    # criando lista de usuários

    tabela_head = ['ID','Nome', 'Naturalidade','Gênero', 'Data de Nascimento', 'Altura','Peso', 'Hobbies']

    lista_usuarios = ver_form()

    # criando tabela (tree)
    tree = ttk.Treeview(frameBaixo, selectmode="extended",columns=tabela_head, show="headings")

    # barra de scroll vertical
    vsb = ttk.Scrollbar(frameBaixo, orient="vertical", command=tree.yview)

    # barra de scroll horizontal
    hsb = ttk.Scrollbar(frameBaixo, orient="horizontal", command=tree.xview)

    # configurando as duas barras
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')
    frameBaixo.grid_rowconfigure(0, weight=12)

    # posicionando os espaços e colunas
    hd=["center","center","center","center","center","center","center", 'center']
    h=[40,170,170,90,120,60,50, 180]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        tree.column(col, width=h[n],anchor=hd[n])
        n+=1


    # inserindo os usuarios dentro da tabela

    for usuario in lista_usuarios:
        tree.insert('', 'end', values=usuario)


    quantidade = [8888,88]

    for usuarios in lista_usuarios:
        quantidade.append(usuarios[6])

mostrar()



janela.mainloop()