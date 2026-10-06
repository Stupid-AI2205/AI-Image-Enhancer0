import os
from enhancer import enhance_image


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

input_image = os.path.join(
    BASE_DIR,
    "uploads",
    "test.jpg"
)

output_image = os.path.join(
    BASE_DIR,
    "outputs",
    "enhanced_test.jpg"
)


print("Input:", input_image)
print("Output:", output_image)

result = enhance_image(
    input_image,
    output_image
)

print()
print("================================")
print("Enhancement completed!")
print("Saved to:", result)
print("================================")