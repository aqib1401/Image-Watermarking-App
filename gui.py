from tkinter import *
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import ImageTk, Image


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
                                    padx=5,
                                    pady=1,
                                    fg="white",
                                    font=("Arial", 12))
        self.img_button.place(x=250, y=250)

        self.watermark_img_button = tk.Button(self.root, text="Upload Watermark",
                                              command=self.upload_watermark_image,
                                              bg="Violet",
                                              padx=5,
                                              pady=1,
                                              fg="white",
                                              font=("Arial", 12))
        self.watermark_img_button.place(x=400, y=250)

        self.process_button = tk.Button(self.root, text="Add Watermark",
                                        bg="Tomato",
                                        padx=50,
                                        pady=5,
                                        fg="white",
                                        font=("Arial", 12))
        self.process_button.place(x=300, y=300)

        self.main_image_path = None
        self.watermark_path = None

        # Placeholder for the canvas where the image will be shown
        self.img_tk = None
        self.canvas = None
        self.img_label = None
        self.save_img_button = None

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
        self.watermark_path = image_path
        return self.watermark_path

    def show_image(self, img):
        # Clear previous canvas (if exists) to avoid overlaps
        if hasattr(self, 'canvas') and self.canvas:
            self.canvas.destroy()

        # Create a new canvas
        self.canvas = Canvas(self.root, width=300, height=300)
        self.canvas.place(x=250, y=100)

        # Load and display the image
        img = img.resize((300, 300))  # Resize the image to fit the canvas (optional)
        self.img_tk = ImageTk.PhotoImage(img)

        # Add the image to the canvas
        self.canvas.create_image(0, 0, anchor='nw', image=self.img_tk)

        # Update label text
        self.label.configure(text="Watermarked Image",
                             font=("Arial", 19),
                             fg="Gray",
                             anchor="center")
        self.label.place(x=290, y=50)

        # Save Image button
        self.save_img_button = tk.Button(self.root, text="Save Image",
                                         command=lambda: self.save_image(img),
                                         bg="MediumSeaGreen",
                                         padx=10,
                                         pady=2,
                                         fg="white",
                                         font=("Arial", 12))
        self.save_img_button.place(x=340, y=430)

    def save_image(self, img):
        save_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("All files", "*.*")]
        )
        if save_path:
            # Save the image to the user-specified path
            img.save(save_path)
            print(f"Image saved to {save_path}")

            messagebox.showinfo('Success', 'Image successfully saved!')

