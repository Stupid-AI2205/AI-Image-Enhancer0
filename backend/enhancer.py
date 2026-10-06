import os
import cv2
import torch
from basicsr.archs.rrdbnet_arch import RRDBNet
from realesrgan import RealESRGANer


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "RealESRGAN_x4plus.pth"
)


class ImageEnhancer:

    def __init__(self):

        print("Loading AI model...")

        self.device = torch.device("cpu")

        model = RRDBNet(
            num_in_ch=3,
            num_out_ch=3,
            num_feat=64,
            num_block=23,
            num_grow_ch=32,
            scale=4
        )

        self.upsampler = RealESRGANer(
            scale=4,
            model_path=MODEL_PATH,
            model=model,
            tile=200,
            tile_pad=10,
            pre_pad=0,
            half=False,
            device=self.device
        )

        print("AI model loaded successfully!")


    def enhance(self, input_path, output_path):

        image = cv2.imread(
            input_path,
            cv2.IMREAD_COLOR
        )

        if image is None:
            raise ValueError(
                "Could not read image."
            )

        print(
            f"Original: "
            f"{image.shape[1]} x {image.shape[0]}"
        )

        print("Enhancing...")

        output, _ = self.upsampler.enhance(
            image,
            outscale=4
        )

        os.makedirs(
            os.path.dirname(output_path),
            exist_ok=True
        )

        cv2.imwrite(
            output_path,
            output
        )

        print(
            f"Enhanced: "
            f"{output.shape[1]} x {output.shape[0]}"
        )

        return output_path