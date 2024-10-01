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
    # Get dimensions of the main image
    main_width, main_height = im1.size

    # Resize watermark to be 30% of the main image's size, keeping its original aspect ratio
    watermark_width, watermark_height = im2.size

    # Calculate the new dimensions for the watermark
    # We want the watermark to be 30% of the area of the main image
    scale_factor = 0.3  # This means we want the watermark to be 30% of the main image
    new_width = int(main_width * scale_factor)

    # Maintain aspect ratio
    aspect_ratio = watermark_width / watermark_height
    new_height = int(new_width / aspect_ratio)

    # Resize the watermark to the calculated dimensions
    im2 = im2.resize((new_width, new_height), Image.Resampling.LANCZOS)

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

