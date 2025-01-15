# Copyright (C) 2025 - Benjamin Hupf
#
# Inspirely (https://github.com/BenjaminHupf/Inspirely)
# - Made with ♥ by Benjamin Hupf (https://github.com/BenjaminHupf)
# Last update: 14.01.2025
#
# This work is made available under the GNU Affero General Public License v3.0.
# More informations about the license can be found at:
# https://www.gnu.org/licenses/agpl-3.0

from flask import Flask, render_template
import random
import json
from PIL import Image, ImageDraw, ImageFont
import os

app = Flask(__name__)

with open("quotes.json", "r") as file:
    quotes = json.load(file)

@app.route("/")
def generate_quote():
    quote = random.choice(quotes)

    image_folder = "static/images"

    image_path = os.path.join(image_folder, random.choice(get_image_files(image_folder)))

    output_path = os.path.join(image_folder, "output.jpg")
    render_quote_on_image(quote, image_path, output_path)

    return render_template("index.html", image_url=output_path)

def render_quote_on_image(quote, image_path, output_path):
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", 30)

    width, height = image.size

    bbox = draw.textbbox((0, 0), quote, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    position = ((width - text_width) // 2, (height - text_height) // 2)

    draw.text(position, quote, (255, 255, 255), font=font)
    image.save(output_path)

def get_image_files(folder_path):
    ignored_files = {"image_credits.json", "output.jpg"}
    allowed_extensions = {".jpg", ".jpeg", ".png"}

    all_files = os.listdir(folder_path)

    image_files = [
        file for file in all_files
        if file not in ignored_files and os.path.splitext(file)[1].lower() in allowed_extensions
    ]

    return image_files

if __name__ == "__main__":
    app.run(debug=True)