import win32com.shell.shell as shell
import tkinter
import customtkinter
import keyboard

import links


APP_WIDTH = 0 # Updates at runtime
APP_HEIGHT = 220
APP_PADX = 20
APP_COLOR = "#202020"

BUTTON_DIM = 100
BUTTON_PADY = (20, 10)
BUTTON_COLOR = "#2b2b2b"
BUTTON_HOVER_COLOR = "#323231"
BUTTON_CORNER = 10
BUTTON_FONT = ("Segoe UI Semibold", 10)

LABEL_FONT = ("Segoe UI Bold", 20)

active_links = {}
app = None

def start_link(path: str):
    shell.ShellExecuteEx(fMask=0x140, lpFile=path, nShow=1)

class link_button():
    """ Represent a running link on the portal. """
    def __init__(self, app: customtkinter.CTk, path: str, name: str, hotkey: str, index: int):
        self.path = path

        # Create a button and a label with the button hotkey
        self.button = customtkinter.CTkButton(master = app,
                                                 text = name,
                                                 command =self.execute,
                                                 width = BUTTON_DIM,
                                                 height = BUTTON_DIM,
                                                 text_font = BUTTON_FONT,
                                                 fg_color = BUTTON_COLOR,
                                                 hover_color = BUTTON_HOVER_COLOR,
                                                 corner_radius = BUTTON_CORNER)
        self.button.grid(column=index, row=0)
        self.label = customtkinter.CTkLabel(master=app, justify=tkinter.CENTER, text=hotkey, text_font=LABEL_FONT)
        self.label.grid(column=index, row=1, pady = BUTTON_PADY)


    def execute(self):
        shell.ShellExecuteEx(fMask=0x140, lpFile=self.path, nShow=1)

def key_handler(event: keyboard.KeyboardEvent):

    if event.name == "esc":
        app.destroy()
        exit()
        

    # Find the key that was triggered
    for link in active_links:
        if event.name.lower() == link.lower():

            # Launch the link associated with the link and exit
            active_links[link].execute()
            app.destroy()
            exit()
        
    return

if __name__ == "__main__":
    
    # Create window
    customtkinter.set_appearance_mode("System")
    app = customtkinter.CTk(fg_color=APP_COLOR)




    # Remove top bar
    app.overrideredirect(1)
    
    # Get links properties
    links_obj = links.links()

    # Calculate window size
    APP_WIDTH = (BUTTON_DIM + 40) * links_obj.get_links_count() + 20

    # Open window on top, in center
    app.attributes('-topmost', True)
    x = int((app.winfo_screenwidth() / 2) - (APP_WIDTH / 2))
    y = int((app.winfo_screenheight() / 2) - (APP_HEIGHT / 2))

    app.geometry("{0}x{1}+{2}+{3}".format(APP_WIDTH, APP_HEIGHT, x, y))

    app.grid_anchor(tkinter.CENTER)

    # Create buttons
    current_index = 0
    for ln in links_obj.get_links():

        lb = link_button(app, ln.get_path(), ln.get_name(), ln.get_hotkey(), current_index)
        active_links[ln.get_hotkey()] = lb
        current_index += 1
    
    # Hook hotkeys
    keyboard.hook(key_handler)

    # Display portal window
    app.mainloop()
