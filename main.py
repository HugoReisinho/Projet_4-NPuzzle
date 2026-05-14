# NPuzzle by Hugo Reisinho
import random


class NPuzzle:

    @staticmethod
    def cria_matriz():
        aux = list(range(1, 9)) + [0]
        npuzzle = ( tuple (aux[0:3]), tuple (aux[3:6]), tuple(aux[6:9]) )
        return npuzzle

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

    @staticmethod
    def successors():
        # deve devolver lista de (novo_estado, acao, custo)
        pass

    def aplicar_movimento(self):
        pass

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


if __name__ == "__main__":
    # Cria objeto
    npuzzle = NPuzzle(NPuzzle.cria_matriz())
    print(f'Original:\n{npuzzle}')

    baralhar=npuzzle.baralhar()
    npuzzle.estado = baralhar
    print(f'Baralhada:\n{npuzzle}')

    print( f'A matriz é final: {npuzzle.is_final(baralhar)}')

    estado_original = npuzzle.estado
    estado_baralhado = npuzzle.baralhar()

    print("Os mapas sao iguais" if npuzzle.is_equal(estado_original, estado_baralhado) else "Os mapas nao sao iguais")

        