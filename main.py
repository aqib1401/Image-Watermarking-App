import os
from gui import GUI
from PIL import Image
import pil  # Refers to your file where `merge` and `reduce_opacity` are defined

# Initialize GUI
gui = GUI()


def process_image():
    # Now check if both images were uploaded
    try:
        if gui.main_image_path and gui.watermark_path:
            # Open main image and watermark
            main_image = Image.open(gui.main_image_path)
            watermark = Image.open(gui.watermark_path)

            # Merge the main image and the watermark using custom function
            outfile = pil.merge(main_image, watermark, opacity=0.3, position="center")

            # Display the watermarked image using the GUI
            gui.show_image(img=outfile)

        else:
            print("Both main image and watermark image must be selected.")
    except OSError as e:
        print(f"Error during watermarking: {e}")


gui.process_button.configure(command=process_image)

# Start the GUI loop first to allow image uploads
gui.root.mainloop()  # Run the GUI
