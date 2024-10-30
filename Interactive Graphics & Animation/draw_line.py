"""
File: draw_line.py
Name: Jason
-------------------------
TODO: draw a circle when first click,then draw a line when second click, and draw a circle later ....
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

window = GWindow(800, 500, title='draw_line')
SIZE = 5
#  make new_line define is newline or not
new_line = True
# #  saved first mouse_x and mouse_y be temp x and y
# temp_x = 0
# temp_y = 0
circle = GOval(SIZE, SIZE)


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw_line)


def draw_line(mouse):
    global new_line
    if new_line:
        circle.filled = False
        #  maek circle point at the middle
        window.add(circle, x=mouse.x - SIZE // 2, y=mouse.y - SIZE // 2)
        new_line = False
    else:
        window.remove(circle)
        line = GLine(circle.x, circle.y, mouse.x, mouse.y)
        # #  make temp_circle save first circle
        # temp_circle = window.get_object_at(Temp_x, Temp_y)
        window.add(line)
        new_line = True


if __name__ == "__main__":
    main()
