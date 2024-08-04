

import customtkinter as ctk
from PIL import Image, ImageFont



def run_app(interface:str, **kwargs):
    app = App()
    app.build(interface=interface, **kwargs)


def load_custom_font(font_dir):
    pil_font = ImageFont.truetype(font_dir)
    font_name = pil_font.getname()[0]
    return font_name


class App(ctk.CTk):

    inter_font_regular = (load_custom_font("desktopapp/fonts/Inter/Inter.ttf"), 18)

    def __init__(self):
        super().__init__()
        self.resizable(width=False, height=False)
        self.wm_attributes('-alpha', 0.5)
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")


    def networkerror_interface(self):

        width, height = (350, 250)
        geometry = f"{width}x{height}"

        self.title("PointerPad - Network Error")
        self.geometry(geometry)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        error_text = "Holà ! Une erreur est survenue\n"
        error_text += "Assurez-vous que votre ordinateur \
est connecté au réseau local puis relancer PointerPad."

        error_label = ctk.CTkLabel(self, text=error_text, wraplength=(3/4 * width), font=self.inter_font_regular)
        error_label.grid(row=0, column=0, sticky='nwse')


    def serverlaunched_interface(self, qrimage_dir:str):
        
        width, height = (350, 500)
        geometry = f"{width}x{height}"

        self.title("PointerPad")
        self.geometry(geometry)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        
        qrimage = ctk.CTkImage(light_image=Image.open(qrimage_dir), dark_image=Image.open(qrimage_dir), size=(3/4 * width, 3/4 * width))
        qrimage_label = ctk.CTkLabel(self, image=qrimage, text="")
        qrimage_label.grid(row=0, column=0)

        info_text = "Scanner ce Code QR sur votre smartphone pour controller votre présentation !"
        info_label = ctk.CTkLabel(self, text=info_text, wraplength=(3/4 * width), font=self.inter_font_regular)
        info_label.grid(row=1, column=0, sticky='nwse', pady=(15, 15))

        exit_button = ctk.CTkButton(self, text="Quitter PointerPad", width=(3/4 * width),font=self.inter_font_regular)
        exit_button.grid(row=2, column=0, pady=(0, 30), ipady=7.5)


    def build(self, interface:str, **kwargs):
        
        match interface:
            case "server_launched":
                self.serverlaunched_interface(kwargs.get("qrimage_dir"))
            case "network_error":
                self.networkerror_interface()

        self.mainloop()