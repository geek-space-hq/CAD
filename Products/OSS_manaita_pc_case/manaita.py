from build123d import *
from ocp_vscode import show, show_object, reset_show, set_port, set_defaults, get_defaults
import settings

BOARD_THIN=5

#板作成
main_board=Box(settings.ATX['X'],settings.ATX['Y'],BOARD_THIN)
#板を左下が原点になるように移動
main_board=Pos(settings.ATX['X']/2,settings.ATX['Y']/2)*main_board
print(settings.ATX['HOLE'][0])
for i,item in enumerate(settings.ATX['HOLE']):
    main_board-=Pos(settings.ATX['HOLE'][i]['x'],settings.ATX['HOLE'][i]['y'])*Cylinder(settings.ATX['HOLE_DIA'] / 2, height=BOARD_THIN)
show_object(main_board)