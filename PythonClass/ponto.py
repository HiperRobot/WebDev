# pylint: disable=missing-module-docstring

class Ponto:
    ''' classe Ponto: representa e manipula coordenadas x,y '''
    def __init__(self,x=0,y=0):
        ''' cria um novo ponto (x,y) '''
        self.x = x
        self.y = y
        return
    
    def exibir(self):
        ''' exibe o ponto no formato(x,y) '''
        print ("(%.2f,%.2f)"%(self.x, self.y))

    def distanciaDaOrigem(self):
        ''' calcula distância do ponto à origem '''
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5 
    
    def distanciaEntrePontos(self, outro):
        ''' calcula distância do ponto à origem '''
        return (((self.x-outro.x) ** 2)+((self.y-outro.y)** 2))**0.5
    
    def quadrante(self):
        ''' retorna o nº do quadrante de um ponto ou 'origem' '''
        if self.x>=0:
            if self.y>0:
                return 1
            elif self.y<0:
                return 4
            else:
                return 'origem'
        elif self.y>0:
            return 2
        else:
            return 3
    
    def desloca(self, n):
        ''' desloca as coordenadas do ponto n unidades '''
        self.x +=n
        self.y +=n

p1 = Ponto()
p2 = Ponto(3,4)
p3 = Ponto(3)
p4 = Ponto(y=4)
p5 = Ponto(y=6,x=4)
p6 = Ponto(8,-3)
print('Ponto 5 está no quadrante: ',p5.quadrante())
print('Ponto 6 está no quadrante: ',p6.quadrante())
