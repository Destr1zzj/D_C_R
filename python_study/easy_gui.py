import easygui as g
import sys
while 1:
     g.msgbox('first gui game!')

     msg = 'learn witch?'
     title = 'xiaoyouxi'
     choices = ['1','x','dha']

     choice = g.choicebox(msg,title,choices)

     g.msgbox('your chioce:' + str(choice),'result')

     msg = ('restart?')
     title = ('restart')

     if g.ccbox(msg,title):
         pass
     else:
         sys.exit(0)
