import random
import string
from PIL import Image, ImageDraw, ImageFont, ImageFilter


def generate_random_text(length=6):
   """Generate a random string of uppercase letters and digits."""
   chars = string.ascii_uppercase + string.digits
   return ''.join(random.choices(chars, k=length))


def generate_captcha(text=None, width=200, height=80, font_path="arial.ttf", name="captcha"):
   """Generate a CAPTCHA image with random text and noise."""
   if text is None:
       text = generate_random_text()


   # Create blank image with white background
   image = Image.new('RGB', (width, height), 'white')
   draw = ImageDraw.Draw(image)


   # Load a font (default to a system font if custom font fails)
   try:
       font = ImageFont.truetype(font_path, 40)
   except:
       font = ImageFont.load_default()


   # Calculate text size using textbbox
   text_bbox = draw.textbbox((0, 0), text, font=font)
   text_width = text_bbox[2] - text_bbox[0]
   text_height = text_bbox[3] - text_bbox[1]


   # Draw the text centered
   text_start = ((width - text_width) // 2, (height - text_height) // 2)
   draw.text(text_start, text, font=font, fill=(0, 0, 0))


   # Draw random lines as noise
   for _ in range(5):
       start = (random.randint(0, width), random.randint(0, height))
       end = (random.randint(0, width), random.randint(0, height))
       draw.line([start, end], fill=(0, 0, 0), width=2)


   # Add noise dots
   for _ in range(100):
       x = random.randint(0, width)
       y = random.randint(0, height)
       draw.point((x, y), fill="black")


   # Apply a filter to make it harder to OCR
   image = image.filter(ImageFilter.EDGE_ENHANCE_MORE)


   # Save the image
   image.save(name+'.png')
   print(f"CAPTCHA saved as "+ name + ".png with text: {text}")
   return text

def generate_plain_text(text=None, width=200, height=80, font_path="arial.ttf", name="captcha"):
   """Generate a CAPTCHA image with random text and noise."""
   if text is None:
       text = generate_random_text()


   # Create blank image with white background
   image = Image.new('RGB', (width, height), 'white')
   draw = ImageDraw.Draw(image)


   # Load a font (default to a system font if custom font fails)
   try:
       font = ImageFont.truetype(font_path, 40)
   except:
       font = ImageFont.load_default()


   # Calculate text size using textbbox
   text_bbox = draw.textbbox((0, 0), text, font=font)
   text_width = text_bbox[2] - text_bbox[0]
   text_height = text_bbox[3] - text_bbox[1]


   # Draw the text centered
   text_start = ((width - text_width) // 2, (height - text_height) // 2)
   draw.text(text_start, text, font=font, fill=(0, 0, 0))


   # Save the image
   image.save(name+'.png')
   print(f"CAPTCHA saved as "+ name + ".png with text: {text}")
   return text


def batch_generate_captcha(num_images=10):
    """Generate multiple CAPTCHA images and save their solutions to a file."""
    batch_solution = []

    for i in range(num_images):
        name = "captcha" + str(i)
        text = generate_captcha(name=name)
        batch_solution.append(text)
        print(f"Generated CAPTCHA {i + 1} with text: {text}")

    # Write the solutions to a text file
    with open("solutions.txt", "w") as f:
        for sol in batch_solution:
            f.write(sol + "\n")

    return batch_solution



# Example usage:
if __name__ == "__main__":
   batch_generate_captcha()






