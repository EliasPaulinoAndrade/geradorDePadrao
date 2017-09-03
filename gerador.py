import os, sys
from PIL import Image
#Codigo Feito Por: Elias Paulino

class RepresentacaoFrame:
       def __init__(self, bitsLinhas, bitsColuns):
              self.bitsLinhas = bitsLinhas
              self.bitsColuns = bitsColuns
class GeradorDePadrao:
       def __init__(self, painelDePixels, cores, largura, altura):
              self.frames = [RepresentacaoFrame(255, 0) for i in range(8)]
              self.painelDePixels = painelDePixels
              self.cores = cores
              self.altura = altura
              self.largura = largura
       def gerarFrames(self):
              for linha in range(self.altura):
                     entrou = False
                     for coluna in range(self.largura):
                            if self.painelDePixels[coluna, linha] in self.cores:
                                   self.frames[coluna].bitsLinhas -= 2**linha
              for coluna in range(self.largura):
                     self.frames[coluna].bitsColuns += 2**coluna
       def getFramesLinhasEmBinario(self):
              return [bin(frame.bitsLinhas) for frame in self.frames]
       def getFramesColunasEmBinario(self):
              return [bin(frame.bitsColuns) for frame in self.frames]
     
print("O padrao Gerado Vai Ser Salvo Em Arquivos .PTN Na Mesma Pasta Onde Está o Código")
nomeImagem = input(">>> Digite o link da imagem: ")
imagem = Image.open(nomeImagem)
sizeX, sizeY = imagem.size
painelDePixels = imagem.load()

if(sizeX > 8 or sizeY > 8):
        sys.exit()

gerador = GeradorDePadrao(painelDePixels, [(0,0,0,255), (0,0,0)], sizeX, sizeY)
gerador.gerarFrames()

arquivo = open(nomeImagem[:-4]+"linhas.PTN", "w")
arquivo.write(";Codigo Feito Por: Elias Paulino\n"+' ,'.join(gerador.getFramesLinhasEmBinario()))
arquivo.close()
arquivo = open(nomeImagem[:-4]+"colunas.PTN", "w")
arquivo.write(";Codigo Feito Por: Elias Paulino\n"+' ,'.join(gerador.getFramesColunasEmBinario()))
arquivo.close()
