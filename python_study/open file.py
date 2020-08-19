import easygui as g
import os
file_path = g.fileopenbox(default="*.txt")

with open(file_path) as old_file:
     title = os.path.basename(file_path)
     msg = '%s：\n' % title
     text =old_file.read()
     text_after = g.textbox(msg,title,text)
if text != text_after[:-1]:
     choice = g.buttonbox("have been changed!warning","warning",("fugai","cancel","another"))
     if choice == "fugai":
          with open(file_path,"w") as old_file:
               old_file.write(text_after[:-1])
     if choice == "cancel":
          pass
     if choice == "another":
          another_path = g.filesavebox(default="*.txt")
          if os.path.splitext(another_path)[1] !=".txt":
               another_path += '.txt'
          with open(another_path,"w") as new_file:
               new_file.write(text_after[:-1])

