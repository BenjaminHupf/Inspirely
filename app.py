# Copyright (C) 2025 - Benjamin Hupf
#
# Inspirely (https://github.com/BenjaminHupf/Inspirely)
# - Made with ♥ by Benjamin Hupf (https://github.com/BenjaminHupf)
# Last update: 13.01.2025
#
# This work is made available under the GNU Affero General Public License v3.0.
# More informations about the license can be found at:
# https://www.gnu.org/licenses/agpl-3.0

from flask import Flask, render_template
import random
import json
from PIL import Image, ImageDraw, ImageFont

app = Flask(__name__)

with open("quotes.json", "r") as file:
    quotes = json.load(file)

@app.route("/")
def generate_quote():
    quote = random.choice(quotes)

    image_path = f"static/images/{random.randint(1, 5)}.jpg"

    output_path = f"static/images/output.jpg"
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

if __name__ == "__main__":
    app.run(debug=True)