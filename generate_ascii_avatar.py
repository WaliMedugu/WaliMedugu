import os
import sys
import math
import io
import urllib.request

try:
    from PIL import Image
except ImportError:
    import subprocess
    print("Installing Pillow...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])
    from PIL import Image

def generate_ascii_svg(image_path, output_path, new_width=120):
    try:
        img = Image.open(image_path)
    except Exception as e:
        print(f"Error opening image: {e}")
        return

    # Convert to grayscale
    img = img.convert('L')
    
    # Calculate new height, accounting for typical monospace font aspect ratio (~0.5)
    width, height = img.size
    aspect_ratio = height / float(width)
    new_height = int(new_width * aspect_ratio * 0.5)
    
    img = img.resize((new_width, new_height))
    
    # Define ASCII chars from dark to light
    chars = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", ".", " "]
    
    pixels = img.getdata()
    ascii_str = ""
    for pixel in pixels:
        index = int((pixel / 255.0) * (len(chars) - 1))
        index = max(0, min(len(chars) - 1, index))
        inverted_index = (len(chars) - 1) - index
        ascii_str += chars[inverted_index]
    
    # Split the string into lines
    ascii_lines = [ascii_str[i:(i + new_width)] for i in range(0, len(ascii_str), new_width)]
    
    font_size = 12
    char_width = font_size * 0.6
    line_height = font_size * 1.2
    
    svg_width = int(new_width * char_width) + 20
    svg_height = int(new_height * line_height) + 20
    
    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {svg_width} {svg_height}" width="100%" height="100%">
  <defs>
    <filter id="glow">
      <feGaussianBlur stdDeviation="1.5" result="coloredBlur"/>
      <feMerge>
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <linearGradient id="bgGradient" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0a0a0a" />
      <stop offset="100%" stop-color="#111827" />
    </linearGradient>
  </defs>
  <rect width="100%" height="100%" fill="url(#bgGradient)" rx="15" />
  <rect width="100%" height="100%" fill="none" stroke="rgba(255,255,255,0.1)" stroke-width="2" rx="15" />
  
  <g font-family="monospace" font-size="{font_size}px" fill="#00ff41" font-weight="bold" filter="url(#glow)">
"""
    
    y = line_height
    for line in ascii_lines:
        escaped_line = line.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        svg_content += f'    <text x="10" y="{y}" xml:space="preserve">{escaped_line}</text>\n'
        y += line_height
        
    svg_content += """  </g>
</svg>"""

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(svg_content)
        
    print(f"Successfully generated {output_path}")

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = r"C:\Users\Wali\Downloads\QuickShare\20260617_125532_1(1).jpg"
    output_path = os.path.join(script_dir, "ascii_avatar.svg")
    generate_ascii_svg(image_path, output_path, new_width=120)
