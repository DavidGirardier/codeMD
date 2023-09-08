from PIL import Image, ImageDraw

# Define the dimensions of the image
width = 300
height = 300
border_size = 20  # Size of the degraded border

# Create a new image with a white background
image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(image)

# Define the colors for the gradient
upper_left_color = (255, 0, 0)       # Red
upper_right_color = (0, 255, 0)      # Green
bottom_color = (0, 0, 255)           # Blue

# Draw the gradient on the image
for y in range(height):
    r_left = int(upper_left_color[0] + (bottom_color[0] - upper_left_color[0]) * y / height)
    g_left = int(upper_left_color[1] + (bottom_color[1] - upper_left_color[1]) * y / height)
    b_left = int(upper_left_color[2] + (bottom_color[2] - upper_left_color[2]) * y / height)

    r_right = int(upper_right_color[0] + (bottom_color[0] - upper_right_color[0]) * y / height)
    g_right = int(upper_right_color[1] + (bottom_color[1] - upper_right_color[1]) * y / height)
    b_right = int(upper_right_color[2] + (bottom_color[2] - upper_right_color[2]) * y / height)

    for x in range(width):
        r = int(r_left + (r_right - r_left) * x / width)
        g = int(g_left + (g_right - g_left) * x / width)
        b = int(b_left + (b_right - b_left) * x / width)
        draw.point((x, y), (r, g, b))

# Draw the degraded borders
for i in range(border_size):
    r = int(upper_left_color[0] + (bottom_color[0] - upper_left_color[0]) * i / border_size)
    g = int(upper_left_color[1] + (bottom_color[1] - upper_left_color[1]) * i / border_size)
    b = int(upper_left_color[2] + (bottom_color[2] - upper_left_color[2]) * i / border_size)

    draw.rectangle([(i, i), (width - i - 1, i)], fill=(r, g, b))  # Top border
    draw.rectangle([(i, i), (i, height - i - 1)], fill=(r, g, b))  # Left border
    draw.rectangle([(i, height - i - 1), (width - i - 1, height - i - 1)], fill=(r, g, b))  # Bottom border
    draw.rectangle([(width - i - 1, i), (width - i - 1, height - i - 1)], fill=(r, g, b))  # Right border

# Save the image
image.save("color_gradient_square_degraded_border.png")
