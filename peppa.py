import glfw
from OpenGL.GL import *

def init():
    glClearColor(1, 1, 1, 1)

def render():
    glClear(GL_COLOR_BUFFER_BIT)
    
    # 1. Base da casa (Parede) - Primitiva: Quadrilátero
    glColor3f(0.8, 0.8, 0.8) # Cor: Cinza
    glBegin(GL_QUADS)
    glVertex2f(-0.5, -0.5)  # Inferior esquerdo
    glVertex2f(0.5, -0.5)   # Inferior direito
    glVertex2f(0.5, 0.2)    # Superior direito
    glVertex2f(-0.5, 0.2)   # Superior esquerdo
    glEnd()
    
    # 2. Telhado - Primitiva: Triângulo
    glColor3f(0.8, 0.2, 0.2) # Cor: Vermelho
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.6, 0.2)   # Vértice esquerdo
    glVertex2f(0.6, 0.2)    # Vértice direito
    glVertex2f(0.0, 0.7)    # Ápice (topo)
    glEnd()
    
    # 3. Porta - Primitiva: Quadrilátero
    glColor3f(0.4, 0.2, 0.1) # Cor: Marrom
    glBegin(GL_QUADS)
    glVertex2f(-0.15, -0.5) # Inferior esquerdo
    glVertex2f(0.15, -0.5)  # Inferior direito
    glVertex2f(0.15, -0.1)  # Superior direito
    glVertex2f(-0.15, -0.1) # Superior esquerdo
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