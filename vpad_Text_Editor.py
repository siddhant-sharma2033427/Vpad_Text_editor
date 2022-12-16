import tkinter as tk
from tkinter import ttk
from tkinter import font , colorchooser,filedialog, messagebox
import os

main_application = tk.Tk()
main_application.geometry('1200x800')
main_application.title('Vpad text editor')

############################################# MAIN MENU START ##########################################

main_menu=tk.Menu()

# FILE ICPNS
file = tk.Menu(main_menu,tearoff=False)
new_icon = tk.PhotoImage(file = 'F:\\python pro\\project stuff\\icons2\\new.png')
open_icon = tk.PhotoImage(file ='F:\\python pro\\project stuff\\icons2\\open.png')
save_icon = tk.PhotoImage(file ='F:\\python pro\\project stuff\\icons2\\save.png')
save_as_icon = tk.PhotoImage(file ='F:\\python pro\\project stuff\\icons2\\save_as.png')
exit_icon = tk.PhotoImage(file ='F:\\python pro\\project stuff\\icons2\\exit.png')

# EDIT ICONS
edit = tk.Menu(main_menu,tearoff=False)
copy_icon = tk.PhotoImage(file = 'F:\\python pro\\project stuff\\icons2\\copy.png')
paste_icon = tk.PhotoImage(file = 'F:\\python pro\\project stuff\\icons2\\paste.png')
cut_icon = tk.PhotoImage(file = 'F:\\python pro\\project stuff\\icons2\\cut.png')
find_icon = tk.PhotoImage(file = 'F:\\python pro\\project stuff\\icons2\\find.png')
clear_all_icon = tk.PhotoImage(file = 'F:\\python pro\\project stuff\\icons2\\clear_all.png')

# VIEW ICON
view = tk.Menu(main_menu,tearoff=False)
tool_bar_icon = tk.PhotoImage(file = 'F:\\python pro\\project stuff\\icons2\\tool_bar.png')
status_bar_icon = tk.PhotoImage(file = 'F:\\python pro\\project stuff\\icons2\\status_bar.png')

# COLOUR THEME ICON
light_default_icon = tk.PhotoImage(file = 'F:\\python pro\\project stuff\\icons2\\light_default.png')
light_plus_icon = tk.PhotoImage(file = 'F:\\python pro\\project stuff\\icons2\\light_plus.png')
dark_icon = tk.PhotoImage(file = 'F:\\python pro\\project stuff\\icons2\\dark.png')
red_icon = tk.PhotoImage(file = 'F:\\python pro\\project stuff\\icons2\\red.png')
monokai_icon = tk.PhotoImage(file = 'F:\\python pro\\project stuff\\icons2\\monokai.png')
night_blue_icon = tk.PhotoImage(file = 'F:\\python pro\\project stuff\\icons2\\night_blue.png')




colour_theme = tk.Menu(main_menu,tearoff = False)

theme_choice=tk.StringVar()
colour_icons = (light_default_icon,light_plus_icon,dark_icon,red_icon,monokai_icon,night_blue_icon)

colour_dict = {
'light default' : ('#000000','#ffffff'),
'light plus' : ('#474747','e0e0e0'),
'Dark' : ('#c4c4c4','#2d2d2d'),
'Light Pink' : ('#2d2d2d','#ffe8e8'),
'Monokai' : ('#d3b774','#474747'),
'Night Blue' : ('#ededed','#6b9dc2')
    }

#cascade
main_menu.add_cascade(label = 'File',menu = file)
main_menu.add_cascade(label = 'Edit',menu = edit)
main_menu.add_cascade(label = 'View',menu = view)
main_menu.add_cascade(label = 'Colour Theme',menu = colour_theme)

#☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺ MAIN MENU END ☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺

############################################# TOOL BAR START ##########################################

tool_bar = ttk.Label(main_application)
tool_bar.pack(side = tk.TOP,fill = tk.X)

# FONT_BOX
font_touple = tk.font.families()
font_family = tk.StringVar()
font_box = ttk.Combobox(tool_bar,width = 35, textvariable = font_family,state = 'readonly')
font_box['values'] = font_touple
font_box.current(font_touple.index('Arial'))
font_box.grid(row = 0 ,column= 0,padx=5)

# SIZE BOX

size_var = tk.IntVar()
font_size = ttk.Combobox(tool_bar , width = 14, textvariable = size_var, state = 'readonly')
font_size['values'] = tuple(range(8,80,2))
font_size.current(2)
font_size.grid(row = 0,column = 1,padx = 5)

# BOLD BUTTON
bold_icon = tk.PhotoImage(file = 'F:\\python pro\\project stuff\\icons2\\bold.png')
bold_btn = ttk.Button(tool_bar,image = bold_icon)
bold_btn.grid(row = 0,column = 3,padx = 5)

# ITALIC BUTTON

italic_icon = tk.PhotoImage(file = 'F:\\python pro\\project stuff\\icons2\\italic.png')
italic_btn = ttk.Button(tool_bar,image = italic_icon)
italic_btn.grid(row = 0,column = 4,padx = 5)

#UNDERLINE BUTTON
underline_icon = tk.PhotoImage(file = 'F:\\python pro\\project stuff\\icons2\\underline.png')
underline_btn = ttk.Button(tool_bar ,image=underline_icon)
underline_btn.grid(row = 0,column = 5,padx = 5)

# FONT COLOUR BUTTON
font_colour_icon = tk.PhotoImage(file = 'F:\\python pro\\project stuff\\icons2\\font_color.png')
font_colour_btn = ttk.Button(tool_bar,image = font_colour_icon)
font_colour_btn.grid(row = 0,column = 6,padx = 5)

# ALINE ICON
aline_left_icon= tk.PhotoImage(file = 'F:\\python pro\\project stuff\\icons2\\align_left.png')
aline_center_icon= tk.PhotoImage(file = 'F:\\python pro\\project stuff\\icons2\\align_center.png')
aline_right_icon= tk.PhotoImage(file = 'F:\\python pro\\project stuff\\icons2\\align_right.png')

# ALINE BUTTON
aline_left_btn = ttk.Button(tool_bar,image = aline_left_icon)
aline_left_btn.grid(row = 0,column = 7,padx =5 )

aline_center_btn = ttk.Button(tool_bar,image = aline_center_icon)
aline_center_btn.grid(row = 0,column = 8,padx =5 )

aline_right_btn = ttk.Button(tool_bar,image = aline_right_icon)
aline_right_btn.grid(row = 0,column = 9,padx =5 )

#☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺ TOOL BAR END ☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺

############################################# TEXT EDITOR START ##########################################

text_editor = tk.Text(main_application)
text_editor.config(wrap = 'word',relief = tk.FLAT)

# SCROLL BAR
scroll_bar = tk.Scrollbar(main_application)
text_editor.focus_set()
scroll_bar.pack(side = tk.RIGHT,fill = tk.Y)
text_editor.pack(fill = tk.BOTH, expand = True)
scroll_bar.config(command = text_editor.yview)
text_editor.config(yscrollcommand = scroll_bar.set)

#FONT FAMILY AND FONT SIZE FUNCATIONALITY

current_font_family = 'Arial'
current_font_size = 12

def change_font(main_application):
    global current_font_family
    current_font_family = font_family.get()
    text_editor.config(font = (current_font_family,current_font_size))

def change_fontsize(main_application):
    global current_font_size
    current_font_size = size_var.get()
    text_editor.config(font = (current_font_family,current_font_size))


font_box.bind('<<ComboboxSelected>>',change_font)
font_size.bind('<<ComboboxSelected>>',change_fontsize)

# BOLD BUTTON FUNCATIONANLITY
def change_bold():
    text_property = tk.font.Font(font = text_editor['font'])
    if text_property.actual()['weight'] == 'normal':
        text_editor.configure(font = (current_font_family,current_font_size,'bold'))
    if text_property.actual()['weight'] == 'bold':
        text_editor.configure(font = (current_font_family,current_font_size,'normal'))

bold_btn.configure(command = change_bold)

# ITALIC FUNCATIONALITY

def change_italic():
    text_property = tk.font.Font(font = text_editor['font'])
    if text_property.actual()['slant'] == 'roman':
        text_editor.configure(font = (current_font_family,current_font_size,'italic'))
    if text_property.actual()['slant'] == 'italic':
        text_editor.configure(font = (current_font_family,current_font_size,'normal'))

italic_btn.configure(command = change_italic)

# UNDERLINE FUNCATIONALITY

def change_underline():
    text_property = tk.font.Font(font = text_editor['font'])
    if text_property.actual()['underline'] == 0:
        text_editor.configure(font = (current_font_family,current_font_size,'underline'))
    if text_property.actual()['slant'] == '1':
        text_editor.configure(font = (current_font_family,current_font_size,'normal'))

underline_btn.configure(command = change_underline)

# FONT COLOUR FUNCATIONALITY

def change_font_colour():
    colour_var = tk.colorchooser.askcolor()
    text_editor.configure(fg = colour_var[1])
    
font_colour_btn.configure(command = change_font_colour)

# ALINE FUNCATIONALITY
def aline_left():
    text_content = text_editor.get(1.0,'end')
    text_editor.tag_config('left',justify = tk.LEFT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'left')

aline_left_btn.configure(command=aline_left)

def aline_center():
    text_content = text_editor.get(1.0,'end')
    text_editor.tag_config('center',justify = tk.CENTER)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'center')

aline_center_btn.configure(command=aline_center)

def aline_right():
    text_content = text_editor.get(1.0,'end')
    text_editor.tag_config('right',justify = tk.RIGHT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'right')

aline_right_btn.configure(command=aline_right)


text_editor.config(font = ('Arial',12))
#☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺ TEXT EDITOR END ☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺

############################################# STATUS BAR START ##########################################

status_bar = ttk.Label(main_application,text = 'Status Bar')
status_bar.pack(side = tk.BOTTOM)

text_changed = False
def change(event = None):
    global text_changed
    if text_editor.edit_modified():
        text_changed = True
        words = len(text_editor.get(1.0,'end-1c').split())
        characters = len(text_editor.get(1.0,'end-1c'))
        status_bar.config(text = f'sharacters :{characters} words : {words}')
    text_editor.edit_modified(False)

text_editor.bind('<<Modified>>',change)


#☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺ STATUS BAR END ☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺

############################################# MAIN MENU FUNCTIONALITY START ##########################################

# VARIABLE
url = ''

##NEW FUNCATIONALITY

def new_file(event = None):
    global url
    url = ''
    text_editor.delete(1.0,tk.END)

#OPEN FUNCATIONALITY

def open_file(event = None):
    global url
    url = filedialog.askopenfilename(initialdir = os.getcwd(),title = 'Select File',filetypes=(('Text File','*.txt'),('All files','*.*')))
    try:
        with open(url,'r') as fr:
            text_editor.delete(1.0,tk.END)
            text_editor.insert(1.0,fr.read())
    except FileNotFoundError:
        return
    except:
        return
    main_application.title(os.path.basename(url))

##SAVE FUNCATIONALITY

def save_file(event = None):
    global url
    try:
        if url:
            content = str(text_editor.get(1.0,tk.END))
            with open(url,'w',encoding = 'utf-8') as fw:
                fw.write(content)
        else:
            url = filedialog.asksaveasfile(mode = 'w',defaultextension = '.txt',filetypes = (('Text Files','*.txt'),('All files','*.*')))
            content2 = text_editor.get(1.0,tk.END)
            url.write(content2)
            url.close()
            
    except:
        return

# SAVE AS FUNCATIONALITY
def save_as(event = None):
    global url
    try:
            content = str(text_editor.get(1.0,tk.END))
            url = filedialog.asksaveasfile(mode = 'w',defaultextension = '.txt',filetypes = (('Text Files','*.txt'),('All files','*.*')))
            url.write(content)
            url.close()            
    except:
            return


#EXIT FUNCATIONALITY

def exit_func(event=None):
    global url, text_changed
    try:
        if text_changed:
            mbox = messagebox.askyesnocancel('Warning', 'Do you want to save the file ?')
            if mbox is True:
                if url:
                    content = text_editor.get(1.0, tk.END)
                    with open(url, 'w', encoding='utf-8') as fw:
                        fw.write(content)
                        main_application.destroy()
                else:
                    content2 = str(text_editor.get(1.0, tk.END))
                    url = filedialog.asksaveasfile(mode = 'w', defaultextension='.txt', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
                    url.write(content2)
                    url.close()
                    main_application.destroy()
            elif mbox is False:
                main_application.destroy()
        else:
            main_application.destroy()
    except:
        return 



# FILE COMMAND
file.add_command(label = 'New',image = new_icon,compound = tk.LEFT,accelerator = 'ctrl+N',command = new_file)
file.add_command(label = 'Open',image = open_icon,compound = tk.LEFT,accelerator = 'ctrl+O',command = open_file)
file.add_command(label = 'Save',image = save_icon,compound = tk.LEFT,accelerator = 'ctrl+S',command = save_file)
file.add_command(label = 'save As',image = save_as_icon,compound = tk.LEFT,accelerator = 'ctrl+Alt+s',command = save_as)
file.add_command(label = 'Exit',image = exit_icon,compound = tk.LEFT,accelerator = 'ctrl+Q',command = exit_func)

# EDIT FUNCATIONALITY

#FIND FUNCATIONALITY

def find_func(event=None):

    def find():
        word = find_input.get()
        text_editor.tag_remove('match', '1.0', tk.END)
        matches = 0
        if word:
            start_pos = '1.0'
            while True:
                start_pos = text_editor.search(word, start_pos, stopindex=tk.END)
                if not start_pos:
                    break  
                end_pos = f'{start_pos}+{len(word)}c'
                text_editor.tag_add('match', start_pos, end_pos)
                matches += 1
                start_pos = end_pos
                text_editor.tag_config('match', foreground='red', background='yellow')
    
    def replace():
        word = find_input.get()
        replace_text = replace_input.get()
        content = text_editor.get(1.0, tk.END)
        new_content = content.replace(word, replace_text)
        text_editor.delete(1.0, tk.END)
        text_editor.insert(1.0, new_content)

    find_dialogue = tk.Toplevel()
    find_dialogue.geometry('450x250+500+200')
    find_dialogue.title('Find')
    find_dialogue.resizable(0,0)

    ## frame 
    find_frame = ttk.LabelFrame(find_dialogue, text='Find/Replace')
    find_frame.pack(pady=20)

    ## labels
    text_find_label = ttk.Label(find_frame, text='Find : ')
    text_replace_label = ttk.Label(find_frame, text= 'Replace')

    ## entry 
    find_input = ttk.Entry(find_frame, width=30)
    replace_input = ttk.Entry(find_frame, width=30)

    ## button 
    find_button = ttk.Button(find_frame, text='Find', command=find)
    replace_button = ttk.Button(find_frame, text= 'Replace', command=replace)

    ## label grid 
    text_find_label.grid(row=0, column=0, padx=4, pady=4)
    text_replace_label.grid(row=1, column=0, padx=4, pady=4)

    ## entry grid 
    find_input.grid(row=0, column=1, padx=4, pady=4)
    replace_input.grid(row=1, column=1, padx=4, pady=4)

    ## button grid 
    find_button.grid(row=2, column=0, padx=8, pady=4)
    replace_button.grid(row=2, column=1, padx=8, pady=4)

    find_dialogue.mainloop()
# EDIT COMMAND
edit.add_command(label = 'Copy',image = copy_icon,compound = tk.LEFT,accelerator = 'ctrl+C',command = lambda: text_editor.event_generate('<Control c>'))
edit.add_command(label = 'Paste',image = paste_icon,compound = tk.LEFT,accelerator = 'ctrl+V',command = lambda: text_editor.event_generate('<Control v>'))
edit.add_command(label = 'Cut',image = cut_icon,compound = tk.LEFT,accelerator = 'ctrl+X',command = lambda: text_editor.event_generate('<Control x>'))
edit.add_command(label = 'Clear All',image = clear_all_icon,compound = tk.LEFT,accelerator = 'ctrl+Alt+X',command = lambda : text_editor.delete(1.0,tk.END))
edit.add_command(label = 'Find',image = find_icon,compound = tk.LEFT,accelerator = 'ctrl+F',command = find_func)

#   VIEW COMMAND

show_statusbar = tk.BooleanVar()
show_statusbar.set(True)
show_toolbar = tk.BooleanVar()
show_toolbar.set(True)

def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        tool_bar.pack_forget()
        show_toolbar = False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP,fill= tk.X)
        text_editor.pack(fill=tk.BOTH,expand = True)
        status_bar.pack(side=tk.BOTTOM)
        show_toolbar = True
def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar = False
    else:
        status_bar.pack(side = tk.BOTTOM)
        show_statusbar = True        
 
view.add_checkbutton(label = 'Tool Bar',onvalue = True,offvalue = False,variable = show_toolbar,image = tool_bar_icon, compound = tk.LEFT,command = hide_toolbar)
view.add_checkbutton(label = 'Status_Bar',onvalue = True,offvalue = False,variable = show_statusbar,image = status_bar_icon,compound = tk.LEFT,command = hide_statusbar)

# THEME COMMAND

def change_theme():
    chosen_theme = theme_choice.get()
    colour_tuple = colour_dict.get(chosen_theme)
    fg_colour,bg_colour = colour_tuple[0],colour_tuple[1]
    text_editor.config(background = bg_colour,fg=fg_colour)
    

count = 0
for i in colour_dict:
    colour_theme.add_radiobutton(label = i,image = colour_icons[count],variable = theme_choice,compound = tk.LEFT,command = change_theme)
    count += 1


#☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺ MAIN MENU FUNCTIONALITY END ☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺

main_application.config(menu = main_menu)

# BIND SHORTCUT KRYS
main_application.bind('<Control-n>',new_file)
main_application.bind('<Control-o>',open_file)
main_application.bind('<Control-s>',save_file)
main_application.bind('<Control-Alt-s>',save_as)
main_application.bind('<Control-q>',exit_func)
main_application.bind('<Control-f>',find_func)

main_application.mainloop()
