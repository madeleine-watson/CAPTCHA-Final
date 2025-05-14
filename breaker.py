import easyocr

def break_captcha(name):
    """Use EasyOCR to read text from a CAPTCHA image."""
    reader = easyocr.Reader(['en'])
    results = reader.readtext(name, detail=0)  # detail=0 returns just the text
    
    return results

def batch_break_captcha(num_images=10):
    """Attempt to break multiple CAPTCHA images using OCR."""
    # Read the actual solutions from the file
    with open("solutions.txt", "r") as f:
        solutions = [line.strip() for line in f.readlines()]

    for i in range(num_images):
        name = f"captcha{i}.png"
        results = break_captcha(name)

        # Print and compare the results
        print(f"CAPTCHA {i}: OCR guessed {results}, actual: {solutions[i]}")
        if solutions[i] == results:
            print("✅ Broken successfully")
        else:
            print("❌ Unsuccessful")

if __name__ == "__main__":
    
    batch_break_captcha()