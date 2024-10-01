# Main.py
import os
from gui import GUI
from PIL import Image
import pil

gui = GUI()
gui.root.mainloop()

try:
    if gui.main_image_path and gui.watermark_path:
        f, e = os.path.splitext(gui.main_image_path)
        main_image = Image.open(gui.main_image_path)
        watermark_image = Image.open(gui.watermark_path)

        # Merge the main image and the watermark
        outfile = pil.merge(main_image, watermark_image, opacity=0.3, position="center")

        # Save the new image as PNG or in the original format
        output_path = f + "_watermarked.png"  # Saves as PNG
        outfile.save(output_path)
        print(f"Watermarked image saved to {output_path}")
    else:
        print("Both main image and watermark image must be selected.")
except OSError:
    print("Cannot watermark image:", gui.main_image_path)

#  Pil.py
import os
from PIL import Image, ImageEnhance, ImageTk


# Function to reduce the opacity of the watermark
def reduce_opacity(im, opacity):
    assert 0 <= opacity <= 1, "Opacity must be between 0 and 1"
    if im.mode != 'RGBA':
        im = im.convert('RGBA')
    else:
        im = im.copy()

    alpha = im.split()[3]  # Get alpha channel
    alpha = ImageEnhance.Brightness(alpha).enhance(opacity)  # Adjust transparency
    im.putalpha(alpha)  # Set the new alpha channel with modified opacity
    return im


# Function to overlay watermark onto the main image
def merge(im1, im2, opacity=0.3, position="center"):
    # Resize watermark to fit the main image (30% of the main image's size)
    im2 = im2.resize((int(im2.size[0] * 0.3), int(im2.size[1] * 0.3)))

    # Adjust opacity of the watermark
    im2 = reduce_opacity(im2, opacity=opacity)

    # Convert the main image to RGBA mode (to support transparency)
    im1 = im1.convert("RGBA")

    # Determine the position of the watermark
    if position == "center":
        position = ((im1.size[0] - im2.size[0]) // 2, (im1.size[1] - im2.size[1]) // 2)
    elif position == "bottom-right":
        position = (im1.size[0] - im2.size[0], im1.size[1] - im2.size[1])

    # Paste the watermark on the main image using the watermark's alpha channel as a mask
    im1.paste(im2, position, im2)

    return im1


# GUI.py
from tkinter import *
import tkinter as tk
from tkinter import filedialog


class GUI:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("800x500")
        self.root.title("Image watermarking")

        self.label = tk.Label(self.root, text="Please Select Image to add watermark",
                              font=("Arial", 19),
                              fg="blue",
                              anchor="center")
        self.label.place(x=180, y=200)
        self.img_button = tk.Button(self.root, text="Upload Image",
                                    command=self.upload_main_image,
                                    bg="SlateBlue",
                                    padx=10,
                                    pady=2,
                                    fg="white",
                                    font=("Arial", 12))
        self.img_button.place(x=250, y=250)

        self.watermark_img_button = tk.Button(self.root, text="Upload Watermark",
                                              command=self.upload_watermark_image,
                                              bg="Violet",
                                              padx=10,
                                              pady=2,
                                              fg="white",
                                              font=("Arial", 12))
        self.watermark_img_button.place(x=400, y=250)
        self.main_image_path = None
        self.watermark_image_path = None

    def upload_main_image(self):
        # Open file dialog and allow only image files to be selected
        image_path = filedialog.askopenfilename(
            title="Select Image",
            filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.webp;*.bmp")]
        )
        # print("Selected Main Image Path:", self.main_image_path)
        self.main_image_path = image_path
        return self.main_image_path

    def upload_watermark_image(self):
        # Open file dialog and allow only image files to be selected
        image_path = filedialog.askopenfilename(
            title="Select Image",
            filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.webp;*.bmp")]
        )
        # print("Selected Watermark Image Path:", self.watermark_image_path)
        self.watermark_image_path = image_path
        return self.watermark_image_path
