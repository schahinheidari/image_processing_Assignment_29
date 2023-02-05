from tkinter import *
import cv2 as cv

def update_r(value):
    r_pct = "{:.1f}%".format(int(value) / 31 * 100)
    label_r_output.config(text=r_pct)
    update_final_output()


def update_g(value):
    g_pct = "{:.1f}%".format(int(value) / 63 * 100)
    label_g_output.config(text=g_pct)
    update_final_output()


def update_b(value):
    b_pct = "{:.1f}%".format(int(value) / 31 * 100)
    label_b_output.config(text=b_pct)
    update_final_output()


def update_final_output():
    rgb = slider_rgb()
    label_color_output.config(bg=rgb)



def slider_to_565():
    r = scale_r.get()
    g = scale_g.get()
    b = scale_b.get()
    return "#{:04X}".format(r << 11 | g << 5 | b)


def slider_rgb():
    r_8bit = "{:02X}".format(round(scale_r.get() / 3 * 255))
    g_8bit = "{:02X}".format(round(scale_g.get() / 3 * 255))
    b_8bit = "{:02X}".format(round(scale_b.get() / 3 * 255))
    return f"#{r_8bit}{g_8bit}{b_8bit}"

text_font = cv.FONT_ITALIC
fontSize_percent = cv.FONT_HERSHEY_SIMPLEX
slider_length = 120
fontSize = 15


root = Tk()

root.title("RGB Color Picker")

label_r = Label(root, text="Red", font=(text_font, fontSize, "bold"), fg="red")
label_r.grid(row=10, column=0, pady=(15, 0), padx=(20, 10))

label_g = Label(root, text="Green", font=(text_font, fontSize, "bold"), fg="green")
label_g.grid(row=10, column=1, pady=(15, 0), padx=(10, 10))

label_b = Label(root, text="Blue", font=(text_font, fontSize, "bold"), fg="blue")
label_b.grid(row=10, column=2, pady=(15, 0), padx=(10, 20))

scale_r = Scale(root, from_=0, to=31, resolution=1, length=slider_length, orient=HORIZONTAL, font=(text_font, 12), command=update_r)
scale_r.set(0)
scale_r.grid(row=15, column=0, padx=(20, 10))

scale_g = Scale(root, from_=0, to=63, resolution=1, length=slider_length, orient=HORIZONTAL, font=(text_font, 12), command=update_g)
scale_g.set(0)
scale_g.grid(row=15, column=1, padx=(10, 10))

scale_b = Scale(root, from_=0, to=31, resolution=1, length=slider_length, orient=HORIZONTAL, font=(text_font, 12), command=update_b)
scale_b.set(255)
scale_b.grid(row=15, column=2, padx=(10, 20))

label_r_output = Label(root, text=None, font=(text_font, fontSize_percent), fg="black", bg=None)
label_r_output.grid(row=20, column=0, pady=(10, 10), padx=(20, 10))

label_g_output = Label(root, text=None, font=(text_font, fontSize_percent), fg="black", bg=None)
label_g_output.grid(row=20, column=1, pady=(10, 10), padx=(10, 10))

label_b_output = Label(root, text=None, font=(text_font, fontSize_percent), fg="black", bg=None)
label_b_output.grid(row=20, column=2, pady=(10, 10), padx=(10, 20))

label_color_output = Label(root, text=None, fg="black", width=12, height=3)
label_color_output.grid(row=25, column=1, pady=(20, 0), padx=(5, 5))

root.mainloop()