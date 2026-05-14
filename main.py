# NPuzzle by Hugo Reisinho
import random


class NPuzzle:

    # Construtor
    def __init__(self, matriz):
        self.estado = matriz
        # Informa tamanho da matriz (linha, coluna)
        self.linhas = len(matriz)
        self.colunas = len(matriz[0])

        # define estado final
        self.estado_final = ( (1, 2, 3), (4, 5, 6), (7, 8, 0) )

    #  __str__ o método herdado do objecto. Nao imprime endereços de mememoria
    def __str__(self):
        linhas = []
        for linha in self.estado:
            linha_str = []
            for x in linha:
                linha_str.append(str(x))
            linhas.append(" ".join(linha_str))
        return "\n".join(linhas)

    def is_final(self, matriz):
        for i in range(self.linhas):
            for j in range(self.colunas):
                if matriz[i][j] != self.estado_final[i][j]:
                    return False
        return True

    def is_equal(self, matriz_a, matriz_b):

        # Compara dimensao
        if len(matriz_a) != len(matriz_b):
            return False

        # Compara conteudo da linha
        for i in range(len(matriz_a)):
            if len(matriz_a[i]) != len(matriz_b[i]):
                return False
            # Compara os numeros da linha
            for j in range(len(matriz_a[i])):
                if matriz_a[i][j] != matriz_b[i][j]:
                    return False

        return True

    # Minhas ******************************************************************************************************
    # Cria matriz **************************************************************************************************
    @staticmethod
    def cria_matriz():
        aux = list(range(1, 9)) + [0]
        npuzzle = ( tuple (aux[0:3]), tuple (aux[3:6]), tuple(aux[6:9]) )
        return npuzzle

    # Mostra matriz - prettify ***************************************************************************************
    def prettify(self, estado):
        s = ""
        for i in estado:
            s += "+---+---+---+\n"
            s += "|"
            for v in i:
                if v == 0:
                    s += "   |"
                else:
                    s += f" {v} |"
            s += "\n"
        s += "+---+---+---+\n"
        return s

    # Percentagem Conclusao ***************************************************************************************
    def percentagem_conclusao(self, matriz) :
        correta, total = 0, 0

        for i in range(len(matriz)):
            for j in range(len(matriz[0])):
                if self.estado_final[i][j] != 0:
                    total += 1
                    if matriz[i][j] == self.estado_final[i][j]:
                        correta += 1

        return (correta / total) * 100

    # Baralhar respeitando a paridade ********************************************************************************
    def baralhar(self):
        while True:

            linhas = []
            for l in self.estado:
                nova_linha = list(l)
                linhas.append(nova_linha)

            random.shuffle(linhas)   # baralhar linhas inteiras

            novo = tuple(tuple(l) for l in linhas)

            # garantir que não é igual ao original
            if novo != self.estado:
                return novo

    # MENU
    def escolhe_dificuldade():
        baralhado = False   # flag para saber se ja foi baralha ou nao

        while True:
            print("\n=== Escolhe a dificuldade ===")
            print("1 - Fácil 2 - Médio 3 - Difícil")

            opcao = input("Opção: ").strip()

            if opcao == "1":
                return "facil", 10
            if opcao == "2":
                return "media", 25
            if opcao == "3":
                return "dificil", 40

            print("Opção inválida, dificuldade média.")
            return "media", 25

    # Minhas ******************************************************************************************************

    @staticmethod
    def successors():
        # deve devolver lista de (novo_estado, acao, custo)
        pass

    def aplicar_movimento(self):
        pass



if __name__ == "__main__":

    # Cria objeto
    npuzzle = NPuzzle(NPuzzle.cria_matriz())

    npuzzle.estado = npuzzle.baralhar() # baralha matriz
    print(f'Estado:\n{npuzzle.prettify(npuzzle.estado)}')

    percentagem = npuzzle.percentagem_conclusao(npuzzle.estado)
    #passos = escolhe_dificuldade()

    dificuldade, passos = NPuzzle.escolhe_dificuldade()
    print(f"Percentagem de conclusão: {percentagem:.2f}%  Didiculdade: {dificuldade } Passos: {passos}")
        