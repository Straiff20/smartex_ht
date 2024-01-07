from collections import namedtuple
from dataclasses import dataclass
from utils.constatnts import ARTIFACTS_DIR

FilesForUpload = namedtuple("FilesForUpload", ["name", "path"])


@dataclass
class ContentTypes:
    """
    Список используемых Content-Type
    """
    application_json: str = "application/json"
    application_pdf: str = 'application/pdf'
    image_gif: str = "image/gif"
    image_jpeg: str = "image/jpeg"
    image_png: str = "image/png"
    multipart_form_data: str = "multipart/form-data"
    text_plain: str = "text/plain"
    audio_mp3: str = 'audio/mpeg'


files_for_upload = {
    "small_png": FilesForUpload(name="small_png", path=rf"{ARTIFACTS_DIR}/extra_large_png.png"),
    "small_jpg": FilesForUpload(name="small_jpg", path=rf"{ARTIFACTS_DIR}/small_jpg.jpg"),
    "small_pdf": FilesForUpload(name="small_pdf", path=rf"{ARTIFACTS_DIR}/small_pdf.pdf"),
    "small_mp3": FilesForUpload(name="small_mp3", path=rf"{ARTIFACTS_DIR}/small_mp3.mp3"),

    "middle_png": FilesForUpload(name="middle_png", path=rf"{ARTIFACTS_DIR}/middle_png.png"),
    "middle_jpg": FilesForUpload(name="middle_jpg", path=rf"{ARTIFACTS_DIR}/middle_jpg.jpg"),
    "middle_mp3": FilesForUpload(name="middle_mp3", path=rf"{ARTIFACTS_DIR}/middle_mp3.mp3"),

    "large_png": FilesForUpload(name="large_png", path=rf"{ARTIFACTS_DIR}/large_png.png"),
    "large_jpg": FilesForUpload(name="large_jpg", path=rf"{ARTIFACTS_DIR}/large_jpg.jpg"),
    "large_mp3": FilesForUpload(name="large_mp3", path=rf"{ARTIFACTS_DIR}/large_mp3.mp3"),

    "extra_large_png": FilesForUpload(name="extra_large_png", path=rf"{ARTIFACTS_DIR}/extra_large_png.png"),
    "extra_large_jpg": FilesForUpload(name="extra_large_jpg", path=rf"{ARTIFACTS_DIR}/extra_large_jpg.jpg"),
    "extra_large_mp3": FilesForUpload(name="extra_large_mp3", path=rf"{ARTIFACTS_DIR}/extra_large_mp3.mp3")
}
