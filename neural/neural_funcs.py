import easyocr
import os
import cv2


def is_valid_file_path(file_path):
    if not os.path.isfile(file_path):
        raise ValueError(f"Invalid file path: {file_path}")


def is_supported_file_format(file_path):
    if not (file_path.endswith('.jpg') or file_path.endswith('.png')):
        raise ValueError(f"Unsupported file format: {file_path}")


async def pic_to_text(file_path):
    try:
        is_valid_file_path(file_path)
        is_supported_file_format(file_path)
        reader = easyocr.Reader(['uk', 'en'])
        result = reader.readtext(file_path, detail=0, paragraph=True)
    except Exception as e:
        raise Exception(f"Text recognition failed: {e}")
    return result