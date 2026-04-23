"""Interface grafica (janela) para rotina de Kaprekar com CRUD."""

import tkinter as tk
from tkinter import messagebox, ttk

from src.crud_execucoes import (
    atualizar_observacao,
    criar_registro,
    excluir_registro,
    listar_registros,
)
from src.kaprekar import executar_rotina_kaprekar


class KaprekarApp:
    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title("Kaprekar Routine Analyzer")
        self.raiz.geometry("980x640")

        self.modo_var = tk.StringVar(value="4")
        self.numero_var = tk.StringVar()
        self.id_var = tk.StringVar()
        self.obs_var = tk.StringVar()

        self._montar_tela()
        self.recarregar_lista()

    def _montar_tela(self):
        topo = ttk.LabelFrame(self.raiz, text="Nova execucao")
        topo.pack(fill="x", padx=12, pady=8)

        ttk.Label(topo, text="Modo:").grid(row=0, column=0, padx=6, pady=8, sticky="w")
        ttk.Radiobutton(topo, text="4 digitos (6174)", variable=self.modo_var, value="4").grid(
            row=0, column=1, padx=6, pady=8, sticky="w"
        )
        ttk.Radiobutton(topo, text="3 digitos (495)", variable=self.modo_var, value="3").grid(
            row=0, column=2, padx=6, pady=8, sticky="w"
        )

        ttk.Label(topo, text="Numero:").grid(row=1, column=0, padx=6, pady=8, sticky="w")
        ttk.Entry(topo, textvariable=self.numero_var, width=20).grid(
            row=1, column=1, padx=6, pady=8, sticky="w"
        )
        ttk.Button(topo, text="Executar e salvar", command=self.executar).grid(
            row=1, column=2, padx=6, pady=8, sticky="w"
        )

        meio = ttk.LabelFrame(self.raiz, text="Saida da execucao")
        meio.pack(fill="both", expand=False, padx=12, pady=8)
        self.saida = tk.Text(meio, height=10, wrap="word")
        self.saida.pack(fill="both", expand=True, padx=8, pady=8)

        crud = ttk.LabelFrame(self.raiz, text="CRUD de registros")
        crud.pack(fill="both", expand=True, padx=12, pady=8)

        colunas = ("id", "numero", "modo", "sucesso", "iteracoes", "criado_em", "observacao")
        self.tabela = ttk.Treeview(crud, columns=colunas, show="headings", height=10)
        for coluna in colunas:
            self.tabela.heading(coluna, text=coluna.upper())
            largura = 110
            if coluna == "observacao":
                largura = 260
            self.tabela.column(coluna, width=largura, anchor="w")
        self.tabela.pack(fill="both", expand=True, padx=8, pady=8)
        self.tabela.bind("<<TreeviewSelect>>", self.ao_selecionar)

        acoes = ttk.Frame(crud)
        acoes.pack(fill="x", padx=8, pady=8)
        ttk.Label(acoes, text="ID:").pack(side="left", padx=4)
        ttk.Entry(acoes, textvariable=self.id_var, width=8).pack(side="left", padx=4)
        ttk.Label(acoes, text="Observacao:").pack(side="left", padx=4)
        ttk.Entry(acoes, textvariable=self.obs_var, width=45).pack(side="left", padx=4)
        ttk.Button(acoes, text="Atualizar", command=self.atualizar).pack(side="left", padx=4)
        ttk.Button(acoes, text="Excluir", command=self.excluir).pack(side="left", padx=4)
        ttk.Button(acoes, text="Recarregar", command=self.recarregar_lista).pack(side="left", padx=4)

    def executar(self):
        entrada = self.numero_var.get().strip()
        try:
            numero = int(entrada)
        except ValueError:
            messagebox.showerror("Erro", "Informe um numero inteiro valido.")
            return

        digitos = int(self.modo_var.get())
        sucesso, mensagem, iteracoes = executar_rotina_kaprekar(numero, digitos)
        criar_registro(numero, digitos, sucesso, iteracoes, mensagem)

        self.saida.delete("1.0", tk.END)
        self.saida.insert(tk.END, f"Numero informado: {numero}\n\n{mensagem}")
        self.recarregar_lista()

    def recarregar_lista(self):
        for item in self.tabela.get_children():
            self.tabela.delete(item)

        for registro in listar_registros():
            self.tabela.insert(
                "",
                tk.END,
                values=(
                    registro["id"],
                    registro["numero"],
                    registro["digitos"],
                    "sim" if registro["sucesso"] else "nao",
                    registro["iteracoes"],
                    registro["criado_em"],
                    registro["observacao"],
                ),
            )

    def ao_selecionar(self, _event):
        selecionados = self.tabela.selection()
        if not selecionados:
            return
        valores = self.tabela.item(selecionados[0], "values")
        self.id_var.set(str(valores[0]))
        self.obs_var.set(str(valores[6]))

    def atualizar(self):
        try:
            registro_id = int(self.id_var.get().strip())
        except ValueError:
            messagebox.showerror("Erro", "ID invalido.")
            return

        ok = atualizar_observacao(registro_id, self.obs_var.get().strip())
        if not ok:
            messagebox.showwarning("Aviso", "Registro nao encontrado.")
            return
        self.recarregar_lista()
        messagebox.showinfo("Sucesso", "Registro atualizado.")

    def excluir(self):
        try:
            registro_id = int(self.id_var.get().strip())
        except ValueError:
            messagebox.showerror("Erro", "ID invalido.")
            return

        ok = excluir_registro(registro_id)
        if not ok:
            messagebox.showwarning("Aviso", "Registro nao encontrado.")
            return
        self.id_var.set("")
        self.obs_var.set("")
        self.recarregar_lista()
        messagebox.showinfo("Sucesso", "Registro excluido.")


def main():
    raiz = tk.Tk()
    KaprekarApp(raiz)
    raiz.mainloop()


if __name__ == "__main__":
    main()
