"""
File: my_drawing.py
Name: Jason
----------------------
TODO:
"""

from campy.graphics.gobjects import GRect, GLabel, GPolygon
from campy.graphics.gwindow import GWindow

# init color
BG = '#b6e5db'
OUTLINE = '#323433'
EYE = '#323433'
MOUTH_C1 = '#d25189'
MOUTH_C2 = '#ff8cb5'
GREEN = '#63c965'
D_GREEN = '#559452'
WHITE = 'white'
GRAY = '#c9c9cb'
FACE_C = '#ffe7a5'
FACE_C2 = '#f4d37d'


def main():
    """
    #  online saw this picture then I use python to draw it，it's like Takashi Murakami(村上隆) Flower
    """
    window = GWindow(800, 800, title='My Little Flower')
    rect = GRect(window.width, window.height)
    rect.filled = True
    rect.color = BG
    rect.fill_color = BG
    window.add(rect)
    rect1_1 = GRect(40, 20)
    rect1_1.filled = True
    rect1_1.color = OUTLINE
    rect1_1.fill_color = OUTLINE
    window.add(rect1_1, 380, 150)
    rect1_3 = GRect(20, 20)
    rect1_3.filled = True
    rect1_3.color = OUTLINE
    rect1_3.fill_color = OUTLINE
    window.add(rect1_3, 360, 170)
    rect1_4 = GRect(20, 20)
    rect1_4.filled = True
    rect1_4.color = OUTLINE
    rect1_4.fill_color = OUTLINE
    window.add(rect1_4, 420, 170)
    rect1_7 = GRect(60, 20)
    rect1_7.filled = True
    rect1_7.color = OUTLINE
    rect1_7.fill_color = OUTLINE
    window.add(rect1_7, 260, 170)
    rect1_8 = GRect(60, 20)
    rect1_8.filled = True
    rect1_8.color = OUTLINE
    rect1_8.fill_color = OUTLINE
    window.add(rect1_8, 480, 170)
    #  green 1
    rect33 = GPolygon()
    rect33.add_vertex((380, 170))
    rect33.add_vertex((380, 190))
    rect33.add_vertex((360, 190))
    rect33.add_vertex((360, 230))
    rect33.add_vertex((380, 230))
    rect33.add_vertex((380, 250))
    rect33.add_vertex((420, 250))
    rect33.add_vertex((420, 230))
    rect33.add_vertex((440, 230))
    rect33.add_vertex((440, 190))
    rect33.add_vertex((420, 190))
    rect33.add_vertex((420, 170))
    rect33.filled = True
    rect33.color = GREEN
    rect33.fill_color = GREEN
    window.add(rect33)
    box = GRect(20, 20)
    box.filled = True
    box.color = D_GREEN
    box.fill_color = D_GREEN
    window.add(box, 360, 230)
    box = GRect(20, 20)
    box.filled = True
    box.color = D_GREEN
    box.fill_color = D_GREEN
    window.add(box, 420, 230)
    box15 = GRect(80, 20)
    box15.filled = True
    box15.color = OUTLINE
    box15.fill_color = OUTLINE
    window.add(box15, 360, 250)
    rect55 = GPolygon()
    rect55.add_vertex((320, 190))
    rect55.add_vertex((360, 190))
    rect55.add_vertex((360, 250))
    rect55.add_vertex((340, 250))
    rect55.add_vertex((340, 210))
    rect55.add_vertex((320, 210))
    rect55.filled = True
    rect55.color = OUTLINE
    rect55.fill_color = OUTLINE
    window.add(rect55)
    rect66 = GPolygon()
    rect66.add_vertex((440, 190))
    rect66.add_vertex((480, 190))
    rect66.add_vertex((480, 210))
    rect66.add_vertex((460, 210))
    rect66.add_vertex((460, 250))
    rect66.add_vertex((440, 250))
    rect66.filled = True
    rect66.color = OUTLINE
    rect66.fill_color = OUTLINE
    window.add(rect66)
    rect77 = GPolygon()
    rect77.add_vertex((540, 190))
    rect77.add_vertex((540, 250))
    rect77.add_vertex((600, 250))
    rect77.add_vertex((600, 230))
    rect77.add_vertex((560, 230))
    rect77.add_vertex((560, 190))
    rect77.filled = True
    rect77.color = OUTLINE
    rect77.fill_color = OUTLINE
    window.add(rect77)
    box = GRect(20, 60)
    box.filled = True
    box.color = OUTLINE
    box.fill_color = OUTLINE
    window.add(box, 600, 250)
    rect77 = GPolygon()
    rect77.add_vertex((580, 310))
    rect77.add_vertex((600, 310))
    rect77.add_vertex((600, 350))
    rect77.add_vertex((540, 350))
    rect77.add_vertex((540, 330))
    rect77.add_vertex((580, 330))
    rect77.filled = True
    rect77.color = OUTLINE
    rect77.fill_color = OUTLINE
    window.add(rect77)
    box = GRect(20, 40)
    box.filled = True
    box.color = OUTLINE
    box.fill_color = OUTLINE
    window.add(box, 500, 310)
    box = GRect(20, 100)
    box.filled = True
    box.color = OUTLINE
    box.fill_color = OUTLINE
    window.add(box, 520, 350)
    box = GRect(20, 20)
    box.filled = True
    box.color = OUTLINE
    box.fill_color = OUTLINE
    window.add(box, 600, 350)
    box = GRect(20, 40)
    box.filled = True
    box.color = OUTLINE
    box.fill_color = OUTLINE
    window.add(box, 620, 370)
    box = GRect(20, 20)
    box.filled = True
    box.color = OUTLINE
    box.fill_color = OUTLINE
    window.add(box, 600, 410)
    box = GRect(60, 20)
    box.filled = True
    box.color = OUTLINE
    box.fill_color = OUTLINE
    window.add(box, 540, 430)
    box = GRect(20, 20)
    box.filled = True
    box.color = OUTLINE
    box.fill_color = OUTLINE
    window.add(box, 580, 450)
    box = GRect(20, 60)
    box.filled = True
    box.color = OUTLINE
    box.fill_color = OUTLINE
    window.add(box, 600, 470)
    rect77 = GPolygon()
    rect77.add_vertex((540, 530))
    rect77.add_vertex((540, 590))
    rect77.add_vertex((560, 590))
    rect77.add_vertex((560, 550))
    rect77.add_vertex((600, 550))
    rect77.add_vertex((600, 530))
    rect77.filled = True
    rect77.color = OUTLINE
    rect77.fill_color = OUTLINE
    window.add(rect77)
    box = GRect(20, 20)
    box.filled = True
    box.color = OUTLINE
    box.fill_color = OUTLINE
    window.add(box, 520, 510)
    box = GRect(20, 20)
    box.filled = True
    box.color = OUTLINE
    box.fill_color = OUTLINE
    window.add(box, 500, 490)
    box = GRect(20, 20)
    box.filled = True
    box.color = OUTLINE
    box.fill_color = OUTLINE
    window.add(box, 480, 470)
    box = GRect(20, 20)
    box.filled = True
    box.color = OUTLINE
    box.fill_color = OUTLINE
    window.add(box, 500, 450)
    box = GRect(20, 20)
    box.filled = True
    box.color = OUTLINE
    box.fill_color = OUTLINE
    window.add(box, 460, 490)
    rect77 = GPolygon()
    rect77.add_vertex((320, 570))
    rect77.add_vertex((340, 570))
    rect77.add_vertex((340, 510))
    rect77.add_vertex((460, 510))
    rect77.add_vertex((460, 570))
    rect77.add_vertex((480, 570))
    rect77.add_vertex((480, 590))
    rect77.add_vertex((440, 590))
    rect77.add_vertex((440, 530))
    rect77.add_vertex((360, 530))
    rect77.add_vertex((360, 590))
    rect77.add_vertex((320, 590))
    rect77.filled = True
    rect77.color = OUTLINE
    rect77.fill_color = OUTLINE
    window.add(rect77)
    box = GRect(60, 20)
    box.filled = True
    box.color = OUTLINE
    box.fill_color = OUTLINE
    window.add(box, 480, 590)
    box = GRect(20, 20)
    box.filled = True
    box.color = OUTLINE
    box.fill_color = OUTLINE
    window.add(box, 360, 590)
    box = GRect(20, 20)
    box.filled = True
    box.color = OUTLINE
    box.fill_color = OUTLINE
    window.add(box, 420, 590)
    box = GRect(40, 20)
    box.filled = True
    box.color = OUTLINE
    box.fill_color = OUTLINE
    window.add(box, 380, 610)
    box = GRect(60, 20)
    box.filled = True
    box.color = OUTLINE
    box.fill_color = OUTLINE
    window.add(box, 260, 590)
    rect77 = GPolygon()
    rect77.add_vertex((200, 530))
    rect77.add_vertex((260, 530))
    rect77.add_vertex((260, 590))
    rect77.add_vertex((240, 590))
    rect77.add_vertex((240, 550))
    rect77.add_vertex((200, 550))
    rect77.filled = True
    rect77.color = OUTLINE
    rect77.fill_color = OUTLINE
    window.add(rect77)
    box = GRect(20, 20)
    box.filled = True
    box.color = OUTLINE
    box.fill_color = OUTLINE
    window.add(box, 260, 510)
    box = GRect(20, 20)
    box.filled = True
    box.color = OUTLINE
    box.fill_color = OUTLINE
    window.add(box, 280, 490)
    box = GRect(20, 20)
    box.filled = True
    box.color = OUTLINE
    box.fill_color = OUTLINE
    window.add(box, 300, 470)
    box = GRect(20, 20)
    box.filled = True
    box.color = OUTLINE
    box.fill_color = OUTLINE
    window.add(box, 280, 450)
    box = GRect(20, 20)
    box.filled = True
    box.color = OUTLINE
    box.fill_color = OUTLINE
    window.add(box, 320, 490)
    box = GRect(20, 60)
    box.filled = True
    box.color = OUTLINE
    box.fill_color = OUTLINE
    window.add(box, 180, 470)
    rect77 = GPolygon()
    rect77.add_vertex((200, 470))
    rect77.add_vertex((200, 430))
    rect77.add_vertex((260, 430))
    rect77.add_vertex((260, 350))
    rect77.add_vertex((280, 350))
    rect77.add_vertex((280, 450))
    rect77.add_vertex((220, 450))
    rect77.add_vertex((220, 470))
    rect77.filled = True
    rect77.color = OUTLINE
    rect77.fill_color = OUTLINE
    window.add(rect77)
    box = GRect(20, 20)
    box.filled = True
    box.color = OUTLINE
    box.fill_color = OUTLINE
    window.add(box, 180, 410)
    box = GRect(20, 40)
    box.filled = True
    box.color = OUTLINE
    box.fill_color = OUTLINE
    window.add(box, 160, 370)
    box = GRect(20, 20)
    box.filled = True
    box.color = OUTLINE
    box.fill_color = OUTLINE
    window.add(box, 180, 350)
    box = GRect(20, 20)
    box.filled = True
    box.color = OUTLINE
    box.fill_color = OUTLINE
    window.add(box, 200, 310)
    box = GRect(20, 60)
    box.filled = True
    box.color = OUTLINE
    box.fill_color = OUTLINE
    window.add(box, 180, 250)
    box = GRect(60, 20)
    box.filled = True
    box.color = OUTLINE
    box.fill_color = OUTLINE
    window.add(box, 200, 330)
    box = GRect(20, 40)
    box.filled = True
    box.color = OUTLINE
    box.fill_color = OUTLINE
    window.add(box, 280, 310)
    box = GRect(60, 20)
    box.filled = True
    box.color = OUTLINE
    box.fill_color = OUTLINE
    window.add(box, 200, 230)
    box = GRect(20, 40)
    box.filled = True
    box.color = OUTLINE
    box.fill_color = OUTLINE
    window.add(box, 240, 190)
    box = GRect(20, 20)
    box.filled = True
    box.color = OUTLINE
    box.fill_color = OUTLINE
    window.add(box, 260, 250)
    box = GRect(20, 20)
    box.filled = True
    box.color = OUTLINE
    box.fill_color = OUTLINE
    window.add(box, 280, 270)
    box = GRect(20, 20)
    box.filled = True
    box.color = OUTLINE
    box.fill_color = OUTLINE
    window.add(box, 300, 290)
    box = GRect(40, 20)
    box.filled = True
    box.color = OUTLINE
    box.fill_color = OUTLINE
    window.add(box, 320, 270)
    face = GPolygon()
    face.add_vertex((360, 270))
    face.add_vertex((440, 270))
    face.add_vertex((440, 290))
    face.add_vertex((480, 290))
    face.add_vertex((480, 310))
    face.add_vertex((500, 310))
    face.add_vertex((500, 350))
    face.add_vertex((520, 350))
    face.add_vertex((520, 450))
    face.add_vertex((500, 450))
    face.add_vertex((500, 470))
    face.add_vertex((480, 470))
    face.add_vertex((480, 490))
    face.add_vertex((460, 490))
    face.add_vertex((460, 510))
    face.add_vertex((340, 510))
    face.add_vertex((340, 490))
    face.add_vertex((320, 490))
    face.add_vertex((320, 470))
    face.add_vertex((300, 470))
    face.add_vertex((300, 450))
    face.add_vertex((280, 450))
    face.add_vertex((280, 350))
    face.add_vertex((300, 350))
    face.add_vertex((300, 310))
    face.add_vertex((320, 310))
    face.add_vertex((320, 290))
    face.add_vertex((360, 290))
    face.filled = True
    face.color = FACE_C
    face.fill_color = FACE_C
    window.add(face)

    eye = GRect(20, 60)
    eye.filled = True
    eye.color = EYE
    eye.fill_color = EYE
    window.add(eye, 340, 330)
    eye = GRect(20, 60)
    eye.filled = True
    eye.color = EYE
    eye.fill_color = EYE
    window.add(eye, 440, 330)

    mouth = GPolygon()
    mouth.add_vertex((320, 410))
    mouth.add_vertex((480, 410))
    mouth.add_vertex((480, 450))
    mouth.add_vertex((460, 450))
    mouth.add_vertex((460, 430))
    mouth.add_vertex((340, 430))
    mouth.add_vertex((340, 450))
    mouth.add_vertex((320, 450))
    mouth.filled = True
    mouth.color = OUTLINE
    mouth.fill_color = OUTLINE
    window.add(mouth)
    mouth = GRect(20, 20)
    mouth.filled = True
    mouth.color = OUTLINE
    mouth.fill_color = OUTLINE
    window.add(mouth, 340, 450)
    mouth = GRect(20, 20)
    mouth.filled = True
    mouth.color = OUTLINE
    mouth.fill_color = OUTLINE
    window.add(mouth, 440, 450)
    mouth = GRect(120, 20)
    mouth.filled = True
    mouth.color = MOUTH_C1
    mouth.fill_color = MOUTH_C1
    window.add(mouth, 340, 430)
    mouth = GRect(80, 20)
    mouth.filled = True
    mouth.color = MOUTH_C2
    mouth.fill_color = MOUTH_C2
    window.add(mouth, 360, 450)
    mouth = GRect(80, 20)
    mouth.filled = True
    mouth.color = OUTLINE
    mouth.fill_color = OUTLINE
    window.add(mouth, 360, 470)
    face = GRect(20, 20)
    face.filled = True
    face.color = FACE_C2
    face.fill_color = FACE_C2
    window.add(face, 320, 290)
    face = GRect(20, 20)
    face.filled = True
    face.color = FACE_C2
    face.fill_color = FACE_C2
    window.add(face, 300, 310)
    face = GRect(20, 20)
    face.filled = True
    face.color = FACE_C2
    face.fill_color = FACE_C2
    window.add(face, 280, 350)
    face = GRect(20, 20)
    face.filled = True
    face.color = FACE_C2
    face.fill_color = FACE_C2
    window.add(face, 280, 430)
    face = GRect(20, 20)
    face.filled = True
    face.color = FACE_C2
    face.fill_color = FACE_C2
    window.add(face, 300, 450)
    face = GRect(20, 20)
    face.filled = True
    face.color = FACE_C2
    face.fill_color = FACE_C2
    window.add(face, 320, 470)
    face = GRect(20, 20)
    face.filled = True
    face.color = FACE_C2
    face.fill_color = FACE_C2
    window.add(face, 340, 490)
    face = GRect(20, 20)
    face.filled = True
    face.color = FACE_C2
    face.fill_color = FACE_C2
    window.add(face, 440, 490)
    face = GRect(20, 20)
    face.filled = True
    face.color = FACE_C2
    face.fill_color = FACE_C2
    window.add(face, 460, 470)
    face = GRect(20, 20)
    face.filled = True
    face.color = FACE_C2
    face.fill_color = FACE_C2
    window.add(face, 480, 450)
    face = GRect(20, 20)
    face.filled = True
    face.color = FACE_C2
    face.fill_color = FACE_C2
    window.add(face, 500, 430)
    face = GRect(20, 20)
    face.filled = True
    face.color = FACE_C2
    face.fill_color = FACE_C2
    window.add(face, 500, 350)
    face = GRect(20, 20)
    face.filled = True
    face.color = FACE_C2
    face.fill_color = FACE_C2
    window.add(face, 480, 310)
    face = GRect(20, 20)
    face.filled = True
    face.color = FACE_C2
    face.fill_color = FACE_C2
    window.add(face, 460, 290)
    # oclock 2 flower
    rect77 = GPolygon()
    rect77.add_vertex((520, 270))
    rect77.add_vertex((540, 270))
    rect77.add_vertex((540, 250))
    rect77.add_vertex((600, 250))
    rect77.add_vertex((600, 310))
    rect77.add_vertex((560, 310))
    rect77.add_vertex((560, 330))
    rect77.add_vertex((540, 330))
    rect77.add_vertex((540, 310))
    rect77.add_vertex((520, 310))
    rect77.filled = True
    rect77.color = GREEN
    rect77.fill_color = GREEN
    window.add(rect77)
    box = GRect(20, 40)
    box.filled = True
    box.color = D_GREEN
    box.fill_color = D_GREEN
    window.add(box, 520, 310)
    box = GRect(20, 20)
    box.filled = True
    box.color = D_GREEN
    box.fill_color = D_GREEN
    window.add(box, 560, 310)
    box = GRect(20, 20)
    box.filled = True
    box.color = D_GREEN
    box.fill_color = D_GREEN
    window.add(box, 500, 290)
    # oclock 3 flower
    rect77 = GPolygon()
    rect77.add_vertex((540, 350))
    rect77.add_vertex((600, 350))
    rect77.add_vertex((600, 370))
    rect77.add_vertex((620, 370))
    rect77.add_vertex((620, 410))
    rect77.add_vertex((600, 410))
    rect77.add_vertex((600, 430))
    rect77.add_vertex((540, 430))
    rect77.filled = True
    rect77.color = WHITE
    rect77.fill_color = WHITE
    window.add(rect77)
    box = GRect(20, 20)
    box.filled = True
    box.color = GRAY
    box.fill_color = GRAY
    window.add(box, 540, 350)
    box = GRect(20, 20)
    box.filled = True
    box.color = GRAY
    box.fill_color = GRAY
    window.add(box, 540, 410)
    # oclock 4 flower
    rect77 = GPolygon()
    rect77.add_vertex((520, 450))
    rect77.add_vertex((580, 450))
    rect77.add_vertex((580, 470))
    rect77.add_vertex((600, 470))
    rect77.add_vertex((600, 530))
    rect77.add_vertex((540, 530))
    rect77.add_vertex((540, 510))
    rect77.add_vertex((520, 510))
    rect77.filled = True
    rect77.color = GREEN
    rect77.fill_color = GREEN
    window.add(rect77)
    box = GRect(20, 20)
    box.filled = True
    box.color = D_GREEN
    box.fill_color = D_GREEN
    window.add(box, 520, 450)
    box = GRect(20, 20)
    box.filled = True
    box.color = D_GREEN
    box.fill_color = D_GREEN
    window.add(box, 500, 470)
    # oclock 4 flower
    rect77 = GPolygon()
    rect77.add_vertex((520, 510))
    rect77.add_vertex((520, 530))
    rect77.add_vertex((540, 530))
    rect77.add_vertex((540, 590))
    rect77.add_vertex((480, 590))
    rect77.add_vertex((480, 570))
    rect77.add_vertex((460, 570))
    rect77.add_vertex((460, 510))
    rect77.add_vertex((480, 510))
    rect77.filled = True
    rect77.color = WHITE
    rect77.fill_color = WHITE
    window.add(rect77)
    box = GRect(20, 20)
    box.filled = True
    box.color = GRAY
    box.fill_color = GRAY
    window.add(box, 460, 510)
    box = GRect(20, 20)
    box.filled = True
    box.color = GRAY
    box.fill_color = GRAY
    window.add(box, 480, 490)
    # Oclock 6 flower
    rect77 = GPolygon()
    rect77.add_vertex((440, 530))
    rect77.add_vertex((440, 590))
    rect77.add_vertex((420, 590))
    rect77.add_vertex((420, 610))
    rect77.add_vertex((380, 610))
    rect77.add_vertex((380, 590))
    rect77.add_vertex((360, 590))
    rect77.add_vertex((360, 530))
    rect77.filled = True
    rect77.color = GREEN
    rect77.fill_color = GREEN
    window.add(rect77)
    box = GRect(20, 20)
    box.filled = True
    box.color = D_GREEN
    box.fill_color = D_GREEN
    window.add(box, 360, 530)
    box = GRect(20, 20)
    box.filled = True
    box.color = D_GREEN
    box.fill_color = D_GREEN
    window.add(box, 420, 530)
    # oclock 7 flower
    rect77 = GPolygon()
    rect77.add_vertex((280, 510))
    rect77.add_vertex((340, 510))
    rect77.add_vertex((340, 570))
    rect77.add_vertex((320, 570))
    rect77.add_vertex((320, 590))
    rect77.add_vertex((260, 590))
    rect77.add_vertex((260, 530))
    rect77.add_vertex((280, 530))
    rect77.filled = True
    rect77.color = WHITE
    rect77.fill_color = WHITE
    window.add(rect77)
    box = GRect(20, 20)
    box.filled = True
    box.color = GRAY
    box.fill_color = GRAY
    window.add(box, 320, 510)
    box = GRect(20, 20)
    box.filled = True
    box.color = GRAY
    box.fill_color = GRAY
    window.add(box, 300, 490)
    # oclock 8 flower
    rect77 = GPolygon()
    rect77.add_vertex((280, 510))
    rect77.add_vertex((260, 510))
    rect77.add_vertex((260, 530))
    rect77.add_vertex((200, 530))
    rect77.add_vertex((200, 470))
    rect77.add_vertex((220, 470))
    rect77.add_vertex((220, 450))
    rect77.add_vertex((280, 450))
    rect77.filled = True
    rect77.color = GREEN
    rect77.fill_color = GREEN
    window.add(rect77)
    box = GRect(20, 20)
    box.filled = True
    box.color = D_GREEN
    box.fill_color = D_GREEN
    window.add(box, 260, 450)
    box = GRect(20, 20)
    box.filled = True
    box.color = D_GREEN
    box.fill_color = D_GREEN
    window.add(box, 280, 470)
    # oclock 9 flower
    rect77 = GPolygon()
    rect77.add_vertex((200, 350))
    rect77.add_vertex((260, 350))
    rect77.add_vertex((260, 430))
    rect77.add_vertex((200, 430))
    rect77.add_vertex((200, 410))
    rect77.add_vertex((180, 410))
    rect77.add_vertex((180, 370))
    rect77.add_vertex((200, 370))
    rect77.filled = True
    rect77.color = WHITE
    rect77.fill_color = WHITE
    window.add(rect77)
    box = GRect(20, 20)
    box.filled = True
    box.color = GRAY
    box.fill_color = GRAY
    window.add(box, 240, 350)
    box = GRect(20, 20)
    box.filled = True
    box.color = GRAY
    box.fill_color = GRAY
    window.add(box, 240, 410)
    # oclock 10 flower
    rect77 = GPolygon()
    rect77.add_vertex((200, 250))
    rect77.add_vertex((260, 250))
    rect77.add_vertex((260, 270))
    rect77.add_vertex((280, 270))
    rect77.add_vertex((280, 310))
    rect77.add_vertex((200, 310))
    rect77.filled = True
    rect77.color = GREEN
    rect77.fill_color = GREEN
    window.add(rect77)
    box = GRect(20, 20)
    box.filled = True
    box.color = D_GREEN
    box.fill_color = D_GREEN
    window.add(box, 220, 310)
    box = GRect(20, 20)
    box.filled = True
    box.color = GREEN
    box.fill_color = GREEN
    window.add(box, 240, 310)
    box = GRect(20, 40)
    box.filled = True
    box.color = D_GREEN
    box.fill_color = D_GREEN
    window.add(box, 260, 310)
    box = GRect(20, 20)
    box.filled = True
    box.color = D_GREEN
    box.fill_color = D_GREEN
    window.add(box, 280, 290)
    # oclock 11 flower
    rect77 = GPolygon()
    rect77.add_vertex((260, 190))
    rect77.add_vertex((320, 190))
    rect77.add_vertex((320, 210))
    rect77.add_vertex((340, 210))
    rect77.add_vertex((340, 270))
    rect77.add_vertex((280, 270))
    rect77.add_vertex((280, 250))
    rect77.add_vertex((260, 250))
    rect77.filled = True
    rect77.color = WHITE
    rect77.fill_color = WHITE
    window.add(rect77)
    box = GRect(20, 20)
    box.filled = True
    box.color = GRAY
    box.fill_color = GRAY
    window.add(box, 300, 270)
    box = GRect(20, 20)
    box.filled = True
    box.color = GRAY
    box.fill_color = GRAY
    window.add(box, 340, 250)
    # oclock 12 flower
    box = GRect(40, 20)
    box.filled = True
    box.color = OUTLINE
    box.fill_color = OUTLINE
    window.add(box, 440, 270)
    box = GRect(20, 20)
    box.filled = True
    box.color = GRAY
    box.fill_color = GRAY
    window.add(box, 440, 250)
    box = GRect(20, 20)
    box.filled = True
    box.color = GRAY
    box.fill_color = GRAY
    window.add(box, 480, 270)
    box = GRect(20, 20)
    box.filled = True
    box.color = OUTLINE
    box.fill_color = OUTLINE
    window.add(box, 480, 290)
    box = GRect(20, 20)
    box.filled = True
    box.color = OUTLINE
    box.fill_color = OUTLINE
    window.add(box, 500, 270)
    box = GRect(20, 20)
    box.filled = True
    box.color = OUTLINE
    box.fill_color = OUTLINE
    window.add(box, 520, 250)
    rect77 = GPolygon()
    rect77.add_vertex((520, 270))
    rect77.add_vertex((520, 250))
    rect77.add_vertex((540, 250))
    rect77.add_vertex((540, 190))
    rect77.add_vertex((480, 190))
    rect77.add_vertex((480, 210))
    rect77.add_vertex((460, 210))
    rect77.add_vertex((460, 270))
    rect77.filled = True
    rect77.color = WHITE
    rect77.fill_color = WHITE
    window.add(rect77)
    label = GLabel('My Little Flower')
    label.font = "SansSerif-50-bold"
    label.color = 'pink'
    window.add(label, x=(window.width - label.width) / 2, y=750)
    label = GLabel('inspired by Takashi Murakami(村上隆)')
    label.font = "SansSerif-10-bold"
    label.color = 'black'
    window.add(label, x=(window.width - label.width)-50, y=(window.height - label.height-5))


if __name__ == '__main__':
    main()
