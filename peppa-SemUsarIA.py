import glfw
from OpenGL.GL import *

def init():
    glClearColor(1, 1, 1, 1)

def render():
    glClear(GL_COLOR_BUFFER_BIT)
    # Céu
    glColor3f(0.35, 0.75, 1.0)
    glBegin(GL_QUADS)
    glVertex2f(-1.0, -1.0)
    glVertex2f( 1.0, -1.0)
    glVertex2f( 1.0,  1.0)
    glVertex2f(-1.0,  1.0)
    glEnd()

    # Sol (círculo aproximado) + raios
    glColor3f(1.0, 1.0, 0.0)
    glBegin(GL_POLYGON)
    glVertex2f(0.84, 0.72)
    glVertex2f(0.833, 0.755)
    glVertex2f(0.81, 0.79)
    glVertex2f(0.775, 0.813)
    glVertex2f(0.74, 0.82)
    glVertex2f(0.705, 0.813)
    glVertex2f(0.67, 0.79)
    glVertex2f(0.647, 0.755)
    glVertex2f(0.64, 0.72)
    glVertex2f(0.647, 0.685)
    glVertex2f(0.67, 0.65)
    glVertex2f(0.705, 0.627)
    glVertex2f(0.74, 0.62)
    glVertex2f(0.775, 0.627)
    glVertex2f(0.81, 0.65)
    glVertex2f(0.833, 0.685)
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(0.74, 0.82);  glVertex2f(0.74, 0.90)
    glVertex2f(0.84, 0.72);  glVertex2f(0.92, 0.72)
    glVertex2f(0.74, 0.62);  glVertex2f(0.74, 0.54)
    glVertex2f(0.64, 0.72);  glVertex2f(0.56, 0.72)
    glVertex2f(0.81, 0.79);  glVertex2f(0.87, 0.85)
    glVertex2f(0.67, 0.79);  glVertex2f(0.61, 0.85)
    glVertex2f(0.81, 0.65);  glVertex2f(0.87, 0.59)
    glVertex2f(0.67, 0.65);  glVertex2f(0.61, 0.59)
    glEnd()

    # Nuvem (quads sobrepostos)
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_QUADS)
    glVertex2f(-0.85, 0.68); glVertex2f(-0.70, 0.68); glVertex2f(-0.70, 0.78); glVertex2f(-0.85, 0.78)
    glEnd()
    glBegin(GL_QUADS)
    glVertex2f(-0.75, 0.62); glVertex2f(-0.58, 0.62); glVertex2f(-0.58, 0.76); glVertex2f(-0.75, 0.76)
    glEnd()
    glBegin(GL_QUADS)
    glVertex2f(-0.62, 0.66); glVertex2f(-0.45, 0.66); glVertex2f(-0.45, 0.80); glVertex2f(-0.62, 0.80)
    glEnd()

    # Colina (polígono com topo curvo)
    glColor3f(0.10, 0.80, 0.15)
    glBegin(GL_POLYGON)
    glVertex2f(-1.0, -1.0)
    glVertex2f( 1.0, -1.0)
    glVertex2f( 1.0, -0.45)
    glVertex2f( 0.70, -0.35)
    glVertex2f( 0.35, -0.28)
    glVertex2f( 0.00, -0.25)
    glVertex2f(-0.35, -0.28)
    glVertex2f(-0.70, -0.35)
    glVertex2f(-1.0, -0.45)
    glEnd()

    # Casa (frente) - amarelo
    glColor3f(1.0, 0.90, 0.35)
    glBegin(GL_QUADS)
    glVertex2f(-0.35, -0.45)
    glVertex2f( 0.15, -0.45)
    glVertex2f( 0.15,  0.20)
    glVertex2f(-0.35,  0.20)
    glEnd()

    # Casa (lateral direita) - amarelo um pouco mais escuro (efeito “2D+”)
    glColor3f(0.95, 0.82, 0.30)
    glBegin(GL_QUADS)
    glVertex2f(0.15, -0.45)
    glVertex2f(0.30, -0.38)
    glVertex2f(0.30,  0.25)
    glVertex2f(0.15,  0.20)
    glEnd()

    # Telhado (triângulo frontal) - laranja
    glColor3f(1.0, 0.55, 0.10)
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.42, 0.20)
    glVertex2f( 0.22, 0.20)
    glVertex2f(-0.10, 0.52)
    glEnd()

    # Aba do telhado (lateral) - laranja mais escuro
    glColor3f(0.95, 0.45, 0.08)
    glBegin(GL_QUADS)
    glVertex2f(0.22, 0.20)
    glVertex2f(0.34, 0.26)
    glVertex2f(0.02, 0.58)
    glVertex2f(-0.10, 0.52)
    glEnd()

    # Porta (na frente, inferior direita) - amarelo mais forte
    glColor3f(1.0, 0.82, 0.15)
    glBegin(GL_QUADS)
    glVertex2f(0.02, -0.45)
    glVertex2f(0.12, -0.45)
    glVertex2f(0.12, -0.12)
    glVertex2f(0.02, -0.12)
    glEnd()

    # Maçaneta
    glColor3f(0.0, 0.0, 0.0)
    glPointSize(4.0)
    glBegin(GL_POINTS)
    glVertex2f(0.10, -0.28)
    glEnd()
    glPointSize(1.0)

    # Função local de janela (moldura branca + vidro azul + cruz)
    def _janela(x0, y0, x1, y1):
        # Moldura
        glColor3f(1.0, 1.0, 1.0)
        glBegin(GL_QUADS)
        glVertex2f(x0, y0); glVertex2f(x1, y0); glVertex2f(x1, y1); glVertex2f(x0, y1)
        glEnd()

        # Vidro (inset)
        ix0, iy0 = x0 + 0.01, y0 + 0.01
        ix1, iy1 = x1 - 0.01, y1 - 0.01
        glColor3f(0.65, 0.85, 1.0)
        glBegin(GL_QUADS)
        glVertex2f(ix0, iy0); glVertex2f(ix1, iy0); glVertex2f(ix1, iy1); glVertex2f(ix0, iy1)
        glEnd()

        # Grades (cruz)
        glColor3f(1.0, 1.0, 1.0)
        mx, my = (ix0 + ix1) * 0.5, (iy0 + iy1) * 0.5
        glBegin(GL_LINES)
        glVertex2f(mx, iy0); glVertex2f(mx, iy1)
        glVertex2f(ix0, my); glVertex2f(ix1, my)
        glEnd()

    # Janelas (4 na fachada, estilo “quadradinhas”)
    _janela(-0.30, -0.36, -0.20, -0.26)  # inferior esquerda
    _janela(-0.16, -0.36, -0.06, -0.26)  # inferior meio
    _janela(-0.30, -0.12, -0.20, -0.02)  # superior esquerda
    _janela(-0.16, -0.12, -0.06, -0.02)  # superior meio

    # Janelas na “lateral” (2 para dar a ideia da imagem)
    _janela(0.18, -0.30, 0.26, -0.22)
    _janela(0.18, -0.06, 0.26,  0.02)

    # Antena (no topo do telhado)
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_LINES)
    glVertex2f(-0.10, 0.52); glVertex2f(-0.10, 0.70)   # haste
    glVertex2f(-0.16, 0.58); glVertex2f(-0.04, 0.58)   # barra 1
    glVertex2f(-0.17, 0.63); glVertex2f(-0.03, 0.63)   # barra 2
    glVertex2f(-0.18, 0.68); glVertex2f(-0.02, 0.68)   # barra 3
    glEnd()

def main(): 
    glfw.init()    #inicializa biblioteca glfw
    window = glfw.create_window(800, 600, "Minha primeira janela OpenGL/GLFW", None, None)  #cria janela
    glfw.make_context_current(window)   #cria o contexto
    init()
    while not glfw.window_should_close(window):     #roda enquanto náo fecha a janela
        glfw.poll_events()          #captura eventos
        render()
        glfw.swap_buffers(window)   #troca os buffers da janela  
    glfw.terminate()     #finaliza a biblioteca glfw

if __name__ == "__main__":
    main()