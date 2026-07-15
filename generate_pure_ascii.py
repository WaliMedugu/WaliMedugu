import os
import sys
try:
    from PIL import Image
except ImportError:
    import subprocess
    print("Installing Pillow...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])
    from PIL import Image

def generate_raw_ascii(image_path, output_path, new_width=150):
    try:
        img = Image.open(image_path)
    except Exception as e:
        print(f"Error opening image: {e}")
        return

    # Convert to grayscale
    img = img.convert('L')
    
    # Calculate height with monospace aspect ratio adjustment (usually around 0.5 to 0.55)
    width, height = img.size
    aspect_ratio = height / float(width)
    new_height = int(new_width * aspect_ratio * 0.5)
    
    img = img.resize((new_width, new_height))
    
    # ASCII chars from dark to light
    chars = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", ".", " "]
    
    pixels = img.getdata()
    ascii_str = ""
    for pixel in pixels:
        index = int((pixel / 255.0) * (len(chars) - 1))
        index = max(0, min(len(chars) - 1, index))
        inverted_index = (len(chars) - 1) - index
        ascii_str += chars[inverted_index]
    
    # Split into lines
    ascii_lines = [ascii_str[i:(i + new_width)] for i in range(0, len(ascii_str), new_width)]
    ascii_content = "\n".join(ascii_lines)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(ascii_content)
        
    print(f"Successfully generated high-res ascii text at {output_path} (width: {new_width}, height: {new_height})")

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    generate_raw_ascii(
        r"C:\Users\Wali\Downloads\QuickShare\20260617_125532_1(1).jpg",
        os.path.join(script_dir, "ascii_avatar.txt"),
        new_width=150
    )
