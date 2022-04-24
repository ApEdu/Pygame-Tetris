from tetris import simulate
from components import NQueue,GameConf,CtrlConf,Board

# creating default objects
nqObj = NQueue(1)
gConf = GameConf()
cConf = CtrlConf()
board = Board()


simulate(nqObj,gConf,cConf,board)
