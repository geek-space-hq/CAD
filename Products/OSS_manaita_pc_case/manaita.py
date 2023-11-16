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
    #ボードの形状を表示する用のポリライン
    board=[
        (0+offset_x,0+offset_y,BOARD_THIN),
        (settings[name]['X']+offset_x,0+offset_y,BOARD_THIN),
        (settings[name]['X']+offset_x,settings[name]['Y']+offset_y,BOARD_THIN),
        (0+offset_x,settings[name]['Y']+offset_y,BOARD_THIN),
        (0+offset_x,0+offset_y,BOARD_THIN)
        ]
    l1=Polyline(*board)
    
    #穴あけ形状判定
    if settings[name]['HOLE']!=None:
        for i,item in enumerate(settings[name]['HOLE']):
            #オフセット分ずらして渡されたworkに穴あけ
            work-=Pos(settings[name]['HOLE'][i]['x']+offset_x,settings[name]['HOLE'][i]['y']+offset_y)*Cylinder(settings[name]['HOLE_DIA'] / 2, height=BOARD_THIN)
    return [work,l1]

atx_board=make_board('A3_BOARD')

atx_board=make_hole(
    work=atx_board,
    name='ATX',
    offset_x=0,
    offset_y=settings['A3_BOARD']['Y']-settings['ATX']['Y']
    )

show_object(atx_board)

#2.5インチSSD