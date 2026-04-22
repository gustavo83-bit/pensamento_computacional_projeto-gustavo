'''
criar um sistema de biblioteca

class Livro

class biblioteca (main)

      (produtos)
      livros, periodicos, jornal, maps, gibis/mangás

      (processo / serviços)
       ler, pesquisar, emprestado-devolução
    atributos - metodos
    
'''
class Livro:
    def _init_ (self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True



    def __str__(self):
        status = "disponivel" if self.disponivel else "emprestado"
        return f"'{self.titulo}' - {self.autor}  {status}]"
    


    class Biblioteca:

        def _init_ (self):
            self.livros = []



        def adicionar_livro(self, livro):
            self.livros.append(livro)


        def emprestar_livro(self, titulo_proucurado):    
            for livro in self.livros:
                if livros.titulo == titulo_proucurado:
                    if livro.disponivel:
                        livro.disponivel = False
                        print(f"emprestimo de '{livro.titulo}'Realizado!")
                    else:
                        print(f"o livro, '{livro.titulo}' ja esta ocupado.")
                    return
            print("livros nao encontrado no acervo.")

        biblioteca_municipal = biblioteca()
        l1 = livros("dom quixote", "miguel de cervantes")
        l2 = livros("o principezinho", "antonine de saint-exupéry")
        l3 = livros("don casmmurro", "machado de assis")
        l4 = livros("it a coisa", "stephen king")

        biblioteca_municipal.adicionar_livro(l1)
        biblioteca_municipal.adicionar_livro(l2)

        print(l2)
        biblioteca_municipal.emprestar_livro("o principezinho")
        print(l2)