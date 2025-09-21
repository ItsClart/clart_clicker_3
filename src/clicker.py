# import ctypes
import threading
import time


class Clicker:
    def __init__(self, master):
        self.master = master

        self.click_thread = None
        self.is_clicking = False
        self.delay_minutes = 0
        self.delay_seconds = 0
        self.delay_milliseconds = 100
        self.delay_minimum = 0.001
        self.delay = 0.1

    def start_clicker(self):
        if not self.is_clicking:
            # self.is_clicking = True
            self.master.start_button.configure(state="disable")
            self.master.stop_button.configure(state="normal")
            self.click_thread = threading.Thread(target=self._click_loop)
            self.click_thread.start()

    def stop_clicker(self):
        if self.is_clicking:
            self.is_clicking = False
            self.master.start_button.configure(state="normal")
            self.master.stop_button.configure(state="disable")
            self.click_thread.join()

    def set_delay(self):
        try:
            self.delay_minutes = float(self.master.minute_entry.get()) * 60
            self.delay_seconds = float(self.master.second_entry.get())
            self.delay_milliseconds = float(self.master.millisecond_entry.get()) / 1000
        except ValueError:
            pass

        delay = self.delay_minutes + self.delay_seconds + self.delay_milliseconds
        self.delay = max(delay, self.delay_minimum)

    def _click_loop(self):
        while self.is_clicking:
            """
            if self.master.click_options.get() == "Left Click":
                ctypes.windll.user32.mouse_event(0x0002, 0, 0, 0, 0)  # left down
                ctypes.windll.user32.mouse_event(0x0004, 0, 0, 0, 0)  # left up
            if self.maser.click_options.get() == "Right Click":
                ctypes.windll.user32.mouse_event(0x0008, 0, 0, 0, 0)  # right down
                ctypes.windll.user32.mouse_event(0x0010, 0, 0, 0, 0)  # right up
            """
            print("click")
            time.sleep(self.delay)
