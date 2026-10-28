
import tkinter as tk
from tkinter import ttk, messagebox

# ---------------- CONFIGURACAO ----------------

produtos = ["Teclado", "Monitor", "Mouse"]

COR_FUNDO = "#F4F7FB"
COR_BRANCO = "#FFFFFF"
COR_AZUL = "#2563EB"
COR_AZUL_ESCURO = "#172554"
COR_TEXTO = "#1E293B"
COR_CINZA = "#64748B"
COR_VERDE = "#16A34A"
COR_VERMELHO = "#DC2626"

# ---------------- JANELA PRINCIPAL ----------------

janela = tk.Tk()
janela.title("Estoque Fácil | Gestão de Produtos")
janela.geometry("1000x650")
janela.minsize(850, 560)
janela.configure(bg=COR_FUNDO)

# ---------------- FUNCOES ----------------

def atualizar_tabela():
    """Atualiza a tabela e os indicadores do estoque."""
    for item in tabela.get_children():
        tabela.delete(item)

    for numero, produto in enumerate(produtos, start=1):
        tabela.insert(
            "",
            "end",
            values=(numero, produto)
        )

    total_label.config(text=str(len(produtos)))
    status_label.config(
        text=f"{len(produtos)} produto(s) cadastrado(s)"
    )


def limpar_campo():
    campo_produto.delete(0, tk.END)
    tabela.selection_remove(tabela.selection())
    campo_produto.focus()


def selecionar_produto(event=None):
    """Coloca o produto selecionado no campo de texto."""
    selecionados = tabela.selection()

    if selecionados:
        valores = tabela.item(selecionados[0], "values")
        campo_produto.delete(0, tk.END)
        campo_produto.insert(0, valores[1])


def cadastrar_produto():
    nome = campo_produto.get().strip()

    if not nome:
        messagebox.showwarning(
            "Atenção",
            "Digite o nome do produto."
        )
        campo_produto.focus()
        return

    # Evita nomes duplicados, ignorando maiúsculas/minúsculas.
    if any(p.lower() == nome.lower() for p in produtos):
        messagebox.showwarning(
            "Produto existente",
            "Esse produto já está cadastrado."
        )
        return

    produtos.append(nome.title())
    atualizar_tabela()
    limpar_campo()

    messagebox.showinfo(
        "Sucesso",
        "Produto cadastrado com sucesso!"
    )


def atualizar_produto():
    selecionados = tabela.selection()
    nome = campo_produto.get().strip()

    if not selecionados:
        messagebox.showwarning(
            "Atenção",
            "Selecione um produto na tabela para atualizar."
        )
        return

    if not nome:
        messagebox.showwarning(
            "Atenção",
            "Digite o novo nome do produto."
        )
        return

    item = selecionados[0]
    valores = tabela.item(item, "values")
    indice = int(valores[0]) - 1

    if any(
        i != indice and p.lower() == nome.lower()
        for i, p in enumerate(produtos)
    ):
        messagebox.showwarning(
            "Produto existente",
            "Já existe outro produto com esse nome."
        )
        return

    produtos[indice] = nome.title()
    atualizar_tabela()
    limpar_campo()

    messagebox.showinfo(
        "Sucesso",
        "Produto atualizado com sucesso!"
    )


def excluir_produto():
    selecionados = tabela.selection()

    if not selecionados:
        messagebox.showwarning(
            "Atenção",
            "Selecione um produto para excluir."
        )
        return

    item = selecionados[0]
    valores = tabela.item(item, "values")
    indice = int(valores[0]) - 1
    nome = produtos[indice]

    confirmar = messagebox.askyesno(
        "Confirmar exclusão",
        f"Deseja realmente excluir '{nome}'?"
    )

    if confirmar:
        produtos.pop(indice)
        atualizar_tabela()
        limpar_campo()

        messagebox.showinfo(
            "Sucesso",
            "Produto excluído com sucesso!"
        )


# ---------------- ESTILOS ----------------

estilo = ttk.Style()
estilo.theme_use("clam")

estilo.configure(
    "Treeview",
    background=COR_BRANCO,
    foreground=COR_TEXTO,
    fieldbackground=COR_BRANCO,
    rowheight=42,
    font=("Segoe UI", 11),
    borderwidth=0
)

estilo.configure(
    "Treeview.Heading",
    background="#E8EEF8",
    foreground=COR_AZUL_ESCURO,
    font=("Segoe UI", 10, "bold"),
    padding=12,
    relief="flat"
)

estilo.map(
    "Treeview",
    background=[("selected", "#DBEAFE")],
    foreground=[("selected", COR_AZUL_ESCURO)]
)

# ---------------- MENU LATERAL ----------------

menu_lateral = tk.Frame(
    janela,
    bg=COR_AZUL_ESCURO,
    width=230
)
menu_lateral.pack(side="left", fill="y")
menu_lateral.pack_propagate(False)

tk.Label(
    menu_lateral,
    text="📦",
    font=("Segoe UI Emoji", 34),
    bg=COR_AZUL_ESCURO,
    fg="white"
).pack(anchor="w", padx=25, pady=(35, 0))

tk.Label(
    menu_lateral,
    text="Estoque Fácil",
    font=("Segoe UI", 20, "bold"),
    bg=COR_AZUL_ESCURO,
    fg="white"
).pack(anchor="w", padx=25, pady=(5, 0))

tk.Label(
    menu_lateral,
    text="GESTÃO DE PRODUTOS",
    font=("Segoe UI", 9, "bold"),
    bg=COR_AZUL_ESCURO,
    fg="#93C5FD"
).pack(anchor="w", padx=25, pady=(4, 35))

tk.Label(
    menu_lateral,
    text="  ▣   Painel de estoque",
    font=("Segoe UI", 11, "bold"),
    bg="#263B68",
    fg="white",
    padx=10,
    pady=14,
    anchor="w"
).pack(fill="x", padx=12)

tk.Label(
    menu_lateral,
    text="  ●   Produtos",
    font=("Segoe UI", 11),
    bg=COR_AZUL_ESCURO,
    fg="#CBD5E1",
    padx=10,
    pady=14,
    anchor="w"
).pack(fill="x", padx=12, pady=5)

tk.Frame(
    menu_lateral,
    bg="#33466D",
    height=1
).pack(fill="x", padx=22, pady=20)

tk.Label(
    menu_lateral,
    text="Controle seu estoque\ncom simplicidade.",
    font=("Segoe UI", 10),
    bg=COR_AZUL_ESCURO,
    fg="#CBD5E1",
    justify="left"
).pack(side="bottom", anchor="w", padx=25, pady=30)

# ---------------- AREA PRINCIPAL ----------------

principal = tk.Frame(janela, bg=COR_FUNDO)
principal.pack(side="left", fill="both", expand=True)

cabecalho = tk.Frame(principal, bg=COR_FUNDO)
cabecalho.pack(fill="x", padx=30, pady=(28, 20))

tk.Label(
    cabecalho,
    text="Painel de estoque",
    font=("Segoe UI", 23, "bold"),
    bg=COR_FUNDO,
    fg=COR_TEXTO
).pack(anchor="w")

tk.Label(
    cabecalho,
    text="Gerencie seus produtos de maneira simples e rápida.",
    font=("Segoe UI", 11),
    bg=COR_FUNDO,
    fg=COR_CINZA
).pack(anchor="w", pady=(5, 0))

# ---------------- CARTAO DE RESUMO ----------------

cartao = tk.Frame(
    principal,
    bg=COR_BRANCO,
    highlightbackground="#E2E8F0",
    highlightthickness=1
)
cartao.pack(fill="x", padx=30, pady=(0, 20))

tk.Label(
    cartao,
    text="TOTAL DE PRODUTOS",
    font=("Segoe UI", 10, "bold"),
    bg=COR_BRANCO,
    fg=COR_CINZA
).pack(anchor="w", padx=22, pady=(18, 4))

total_label = tk.Label(
    cartao,
    text="0",
    font=("Segoe UI", 28, "bold"),
    bg=COR_BRANCO,
    fg=COR_AZUL
)
total_label.pack(anchor="w", padx=22)

status_label = tk.Label(
    cartao,
    text="0 produto(s) cadastrado(s)",
    font=("Segoe UI", 10),
    bg=COR_BRANCO,
    fg=COR_CINZA
)
status_label.pack(anchor="w", padx=22, pady=(0, 18))

# ---------------- FORMULARIO ----------------

formulario = tk.Frame(principal, bg=COR_FUNDO)
formulario.pack(fill="x", padx=30, pady=(0, 20))

tk.Label(
    formulario,
    text="Nome do produto",
    font=("Segoe UI", 10, "bold"),
    bg=COR_FUNDO,
    fg=COR_TEXTO
).pack(anchor="w", pady=(0, 7))

campo_produto = tk.Entry(
    formulario,
    font=("Segoe UI", 12),
    bg=COR_BRANCO,
    fg=COR_TEXTO,
    relief="flat",
    highlightthickness=1,
    highlightbackground="#CBD5E1",
    highlightcolor=COR_AZUL
)
campo_produto.pack(fill="x", ipady=10)

# ---------------- BOTOES ----------------

botoes = tk.Frame(formulario, bg=COR_FUNDO)
botoes.pack(fill="x", pady=(12, 0))


def criar_botao(texto, cor, comando):
    return tk.Button(
        botoes,
        text=texto,
        command=comando,
        font=("Segoe UI", 10, "bold"),
        bg=cor,
        fg="white",
        activebackground=cor,
        activeforeground="white",
        relief="flat",
        bd=0,
        cursor="hand2",
        padx=14,
        pady=10
    )


criar_botao(
    "+ Cadastrar",
    COR_AZUL,
    cadastrar_produto
).pack(side="left", padx=(0, 8))

criar_botao(
    "✎ Atualizar",
    COR_VERDE,
    atualizar_produto
).pack(side="left", padx=(0, 8))

criar_botao(
    "✕ Excluir",
    COR_VERMELHO,
    excluir_produto
).pack(side="left", padx=(0, 8))

criar_botao(
    "Limpar",
    "#64748B",
    limpar_campo
).pack(side="left")

# ---------------- TABELA DE PRODUTOS ----------------

area_tabela = tk.Frame(
    principal,
    bg=COR_BRANCO,
    highlightbackground="#E2E8F0",
    highlightthickness=1
)
area_tabela.pack(
    fill="both",
    expand=True,
    padx=30,
    pady=(0, 25)
)

tk.Label(
    area_tabela,
    text="Produtos cadastrados",
    font=("Segoe UI", 13, "bold"),
    bg=COR_BRANCO,
    fg=COR_TEXTO
).pack(anchor="w", padx=18, pady=(16, 12))

tabela_frame = tk.Frame(area_tabela, bg=COR_BRANCO)
tabela_frame.pack(fill="both", expand=True, padx=15, pady=(0, 15))

tabela = ttk.Treeview(
    tabela_frame,
    columns=("numero", "produto"),
    show="headings",
    selectmode="browse"
)

tabela.heading("numero", text="Nº")
tabela.heading("produto", text="NOME DO PRODUTO")

tabela.column("numero", width=65, anchor="center", stretch=False)
tabela.column("produto", width=400, anchor="w")

barra = ttk.Scrollbar(
    tabela_frame,
    orient="vertical",
    command=tabela.yview
)
tabela.configure(yscrollcommand=barra.set)

tabela.pack(side="left", fill="both", expand=True)
barra.pack(side="right", fill="y")

tabela.bind("<<TreeviewSelect>>", selecionar_produto)
campo_produto.bind("<Return>", lambda event: cadastrar_produto())

# ---------------- INICIALIZACAO ----------------

atualizar_tabela()
campo_produto.focus()

janela.mainloop()
