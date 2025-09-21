import customtkinter as ctk

from src.clicker import Clicker


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.clicker = Clicker(self)

        # --- GUI ---
        PAD_EDGE = 10
        PAD_FRAME = 5

        # Grid configuration
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure(2, weight=1)

        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(0, weight=0)

        # --- Frames ---
        # Top frame
        self.frame_top = ctk.CTkFrame(self)
        self.frame_top.grid(
            row=0, column=1, sticky="ew", padx=PAD_EDGE, pady=(PAD_EDGE, PAD_FRAME)
        )
        self.columnconfigure(1, weight=0)
        self.frame_top.grid_columnconfigure(0, weight=1)

        # Bottom frame (container)
        frame_bottom = ctk.CTkFrame(
            self, fg_color="transparent", corner_radius=0, border_width=0
        )
        frame_bottom.grid(
            row=1, column=1, sticky="ew", padx=PAD_EDGE, pady=(0, PAD_EDGE)
        )
        frame_bottom.grid_columnconfigure(0, weight=1, uniform="halves")
        frame_bottom.grid_columnconfigure(1, weight=1, uniform="halves")

        # Bottom left frame
        self.frame_bottom_left = ctk.CTkFrame(frame_bottom)
        self.frame_bottom_left.grid(
            row=0, column=0, sticky="ew", padx=(0, PAD_FRAME), pady=5
        )

        # Bottom right frame
        self.frame_bottom_right = ctk.CTkFrame(frame_bottom)
        self.frame_bottom_right.grid(
            row=0, column=1, sticky="ew", padx=(PAD_FRAME, 0), pady=5
        )

        # --- Widgets ---
        # Top frame widgets
        PAD_X = 10
        PAD_Y_TOP = 8
        PAD_Y_BOTTOM = 8

        self.frame_top.grid_columnconfigure(0, weight=1, uniform="time")
        self.frame_top.grid_columnconfigure(1, weight=1, uniform="time")
        self.frame_top.grid_columnconfigure(2, weight=1, uniform="time")

        self.minute_label = ctk.CTkLabel(self.frame_top, text="Minutes :")
        self.minute_label.grid(
            row=0, column=0, padx=PAD_X, pady=(PAD_Y_TOP, 0), sticky="w"
        )
        self.minute_entry = ctk.CTkEntry(self.frame_top)
        self.minute_entry.grid(
            row=1, column=0, padx=PAD_X, pady=(0, PAD_Y_BOTTOM), sticky="ew"
        )
        self.minute_entry.insert(0, "0")

        self.second_label = ctk.CTkLabel(self.frame_top, text="Seconds :")
        self.second_label.grid(
            row=0, column=1, padx=PAD_X, pady=(PAD_Y_TOP, 0), sticky="w"
        )
        self.second_entry = ctk.CTkEntry(self.frame_top)
        self.second_entry.grid(
            row=1, column=1, padx=PAD_X, pady=(0, PAD_Y_BOTTOM), sticky="ew"
        )
        self.second_entry.insert(0, "0")

        self.millisecond_label = ctk.CTkLabel(self.frame_top, text="Milliseconds :")
        self.millisecond_label.grid(
            row=0, column=2, padx=PAD_X, pady=(PAD_Y_TOP, 0), sticky="w"
        )
        self.millisecond_entry = ctk.CTkEntry(self.frame_top)
        self.millisecond_entry.grid(
            row=1, column=2, padx=PAD_X, pady=(0, PAD_Y_BOTTOM), sticky="ew"
        )
        self.millisecond_entry.insert(0, "100")

        # Bottom left widgets
        self.set_delay_button = ctk.CTkButton(
            self.frame_bottom_left, text="Set Delay", command=self.clicker.set_delay
        )
        self.set_delay_button.pack(pady=10)

        self.keybind_button = ctk.CTkButton(
            self.frame_bottom_left, text="Keybind Options"
        )
        self.keybind_button.pack(pady=10)

        self.theme_options = ctk.CTkOptionMenu(
            self.frame_bottom_left, values=["Dark Theme", "Light Theme"]
        )
        self.theme_options.pack(pady=10)

        # Bottom right widgets
        self.start_button = ctk.CTkButton(self.frame_bottom_right, text="Start")
        self.start_button.pack(pady=10)

        self.stop_button = ctk.CTkButton(self.frame_bottom_right, text="Stop")
        self.stop_button.pack(pady=10)
        self.stop_button.configure(state="disabled")

        self.click_options = ctk.CTkOptionMenu(
            self.frame_bottom_right, values=["Left Click", "Right Click"]
        )
        self.click_options.pack(pady=10)

        # Window Config
        self.update_idletasks()
        w = self.winfo_reqwidth()
        h = self.winfo_reqheight()
        self.title("Clart Clicker 3.0")
        self.resizable(False, False)
        self.geometry(f"{w}x{h}")
