from collections import namedtuple
from dataclasses import dataclass

from utils.constatnts import ARTIFACTS_DIR

FilesForUpload = namedtuple("FilesForUpload", ["name", "path"])


@dataclass
class ContentTypes:
    """
    Список доступных типов Content-Type
    """
    application_json: str = "application/json"
    application_pdf: str = 'application/pdf'
    image_gif: str = "image/gif"
    image_jpeg: str = "image/jpeg"
    image_png: str = "image/png"
    multipart_form_data: str = "multipart/form-data"


files_for_upload = {
    "small_png": FilesForUpload(name="small_png", path=f"{ARTIFACTS_DIR}/small_png.png"),
    "small_jpg": FilesForUpload(name="small_jpg", path=f"{ARTIFACTS_DIR}/small_jpg.jpg"),
    "small_pdf": FilesForUpload(name="small_pdf", path=f"{ARTIFACTS_DIR}/small_pdf.pdf"),

    "middle_png": FilesForUpload(name="middle_png", path=f"{ARTIFACTS_DIR}/middle_png.png"),
    "middle_jpg": FilesForUpload(name="middle_jpg", path=f"{ARTIFACTS_DIR}/middle_jpg.jpg"),

    "large_png": FilesForUpload(name="large_png", path=f"{ARTIFACTS_DIR}/large_png.png"),
    "large_jpg": FilesForUpload(name="large_jpg", path=f"{ARTIFACTS_DIR}/large_jpg.jpg"),

    "extra_large_png": FilesForUpload(name="extra_large_png", path=f"{ARTIFACTS_DIR}/extra_large_png.png"),
    "extra_large_jpg": FilesForUpload(name="extra_large_jpg", path=f"{ARTIFACTS_DIR}/extra_large_jpg.jpg")
}
