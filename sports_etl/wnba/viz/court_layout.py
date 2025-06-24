import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Circle, Arc

def draw_rectangle(ax, xy, width, height, color='none', lw=2):
    rect = patches.Rectangle(xy, width, height, edgecolor='black', facecolor=color, lw=lw)
    ax.add_patch(rect)

def draw_line(ax, x_values, y_values, color='black', lw=2, linestyle='solid'):
    ax.plot(x_values, y_values, color=color, lw=lw, linestyle=linestyle)

def draw_arc(ax, xy, width, height, theta1, theta2, color='black', lw=2, linestyle='solid'):
    arc = Arc(xy, width, height, angle=0, theta1=theta1, theta2=theta2, color=color, lw=lw, linestyle=linestyle)
    ax.add_patch(arc)

def draw_circle(ax, xy, radius, color='black', fill=False, lw=2):
    circle = Circle(xy, radius, edgecolor=color, facecolor=color if fill else 'none', lw=lw)
    ax.add_patch(circle)

def create_basketball_court(fig_size=(12, 6.33), court_color='peachpuff', lw=2):
    fig, ax = plt.subplots(figsize=fig_size)

    # Court background
    draw_rectangle(ax, (0, 0), 94, 50, color=court_color, lw=0)
    draw_rectangle(ax, (0, 0), 94, 50, lw=lw)

    for x in [47]:
        draw_line(ax, [x, x], [31, 50], lw=lw)
        draw_line(ax, [x, x], [0, 19], lw=lw)

    for x in [0, 75]:
        draw_rectangle(ax, (x, 19), 19, 12, lw=lw)
        draw_rectangle(ax, (x, 17), 19, 16, lw=lw)

    for x in [19, 75]:
        draw_arc(ax, (x, 25), 12, 12, 270, 90, linestyle='solid' if x == 19 else 'dashed', lw=lw)
        draw_arc(ax, (x, 25), 12, 12, 90, 270, linestyle='dashed' if x == 19 else 'solid', lw=lw)

    draw_circle(ax, (47, 25), 6, lw=lw)

    tick_x_positions = [4, 5, 8, 11]
    for x in tick_x_positions:
        draw_line(ax, [x, x], [33, 34], lw=lw)
        draw_line(ax, [x, x], [17, 16], lw=lw)
        draw_line(ax, [94 - x, 94 - x], [33, 34], lw=lw)
        draw_line(ax, [94 - x, 94 - x], [17, 16], lw=lw)

    for x in [28, 66]:
        draw_line(ax, [x, x], [0, 3], lw=lw)
        draw_line(ax, [x, x], [50, 47], lw=lw)

    for x in [0, 93.5]:
        draw_line(ax, [x, x + 0.5], [13, 13], lw=lw)
        draw_line(ax, [x, x + 0.5], [37, 37], lw=lw)

    draw_arc(ax, (5.25, 25), 44.29, 44.29, 270, 90, lw=lw)
    draw_arc(ax, (88.75, 25), 44.29, 44.29, 90, 270, lw=lw)

    for x in [0, 88]:
        draw_line(ax, [x, x + 5], [2.8542, 2.8542], lw=lw)
        draw_line(ax, [x, x + 5], [47.1458, 47.1458], lw=lw)

    for x in [4, 90]:
        rim_x = x + 1.25 if x == 4 else x - 1.25
        draw_circle(ax, (rim_x, 25), 1, color='orange', lw=lw)
        draw_line(ax, [x, x], [22, 28], color='orange', lw=lw)
        draw_arc(ax, (rim_x, 25), 8, 8, 270 if x == 4 else 90, 90 if x == 4 else 270, lw=lw)

    ax.set_xlim(0, 94)
    ax.set_ylim(0, 50)
    ax.set_aspect('equal')
    plt.axis('off')

    return fig, ax