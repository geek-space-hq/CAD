from build123d import *
from ocp_vscode import show, show_object, reset_show, set_port, set_defaults, get_defaults
import yaml

PATH='Products\OSS_manaita_pc_case\settings.yaml'
BOARD_THIN=5

with open(PATH, encoding='utf-8') as file:
    settings=yaml.safe_load(file)

def make_board(name):
    #ATXマザーボード
    #板作成
    main_board=Box(settings[name]['X'],settings[name]['Y'],BOARD_THIN)
    #板を左下が原点になるように移動
    main_board=Pos(settings[name]['X']/2,settings[name]['Y']/2)*main_board
    if settings[name]['HOLE']!=None:
        for i,item in enumerate(settings[name]['HOLE']):
            main_board-=Pos(settings[name]['HOLE'][i]['x'],settings[name]['HOLE'][i]['y'])*Cylinder(settings[name]['HOLE_DIA'] / 2, height=BOARD_THIN)
    return main_board

def make_hole(work,name,offset_x,offset_y):
    #ワークに穴を開ける
    board=[
        (0,0,BOARD_THIN),
        (settings[name]['X'],0,BOARD_THIN),
        (settings[name]['X'],settings[name]['Y'],BOARD_THIN),
        (0,settings[name]['Y'],BOARD_THIN),
        (0,0,BOARD_THIN)
        ]
    l1=Polyline(*board)
    if settings[name]['HOLE']!=None:
        for i,item in enumerate(settings[name]['HOLE']):
            work-=Pos(settings[name]['HOLE'][i]['x']+offset_x,settings[name]['HOLE'][i]['y']+offset_y)*Cylinder(settings[name]['HOLE_DIA'] / 2, height=BOARD_THIN)
    return [work,l1]

atx_board=make_board('A3_BOARD')
atx_board=make_hole(atx_board,'ATX',0,0)
show_object(atx_board)

#2.5インチSSD