#coding: utf-8

#########Import das bibliotecas usadas##########
import matplotlib.pyplot as plt
import matplotlib.animation as animation
################################################

########Variaveis e constatntes iniciais########
#Gravidade
g = -9.807
#Velocidade inicial
v0 = 10
#Altura inicial
h0 = 1
#Coeficiente de Restituição
e = 0.85
#Intervalo entre calculos
timestep = 1/60.0
################################################

#Velocidade Atual da particula
v = v0
#Altura inicial da particula
h = h0

#Array com Tempos da simulação
tempos = [0]
#Array com Alturas da Simulação
alturas = [h0]

########Pre calcula valores da simulação########
#Numero de quicadas
i = 0
#Enquanto a energia tota do sistema for maior que um limiar pequeno continua a calcular a simulação
while e ** i > 1e-15:
    #Atualiza velocidade da particula
    v += g * timestep
    #Atualiza altura da particula
    h += v * timestep

    #Verifica se a particula atingiu o chao para calcular a energia dissipada e devolvida pelo impacto
    if h <= 0:
        #Atualiza velocidade da particula pos impacto
        v *= -1 * e
        #Atualiza altura da particula pos impacto
        h = 0
        #Atualiza contador de quicadas
        i += 1

    #Registra dados de tempo
    tempos.append(tempos[-1] + timestep)
    #Registra dados de posição
    alturas.append(h)
################################################

#Printa a quantidade de quicadas
print("Quicadas: ", i)

#Plota grafico de Posição X Tempo
plt.plot(tempos, alturas)
plt.show()

#Define tamanho da particula no grafico
circleSize = max(alturas)/50
fig = plt.figure()

#Define região do grafico a exibir
x_lim = (-(max(alturas)+(circleSize*2)) / 2, (max(alturas)+(circleSize*2)) / 2)
y_lim = (0, max(alturas)+(circleSize*2))
ax = plt.axes(xlim=x_lim, ylim=y_lim)


#Cria particula
circle = plt.Circle((0, h0 + circleSize), circleSize)

#Posiciona particula e adiciona ao grafico
def init():
    circle.center = (0, h0 + circleSize)
    ax.add_patch(circle)
    return circle,

#Retorna posição da particula apos o frame "index"
def animate(index):
    _, y = circle.center
    y = alturas[index] + circleSize
    circle.center = (0, y)
    return circle,

#Efetua animação
anim = animation.FuncAnimation(fig, animate, init_func=init, interval=timestep*1000, frames=len(alturas), repeat=False)

#Exibe animação
plt.show()
