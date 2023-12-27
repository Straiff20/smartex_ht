from dataclasses import dataclass


@dataclass
class ContentTypes:
    """
    Список доступных типов Content-Type
    """
    APPLICATION_JSON: str = "application/json"  # передает файл формата JSON
    APPLICATION_XML: str = "application/xml"  # передает файл формата XML
    IMAGE_GIF: str = "image/gif"  # передает файл формата GIF
    IMAGE_JPEG: str = "image/jpeg"  # передает файл формата JPEG
    IMAGE_PNG: str = "image/png"  # передает файл формата PNG
    MULTIPART_FORM_DATA: str = "multipart/form-data"  # передает файлы и данные формы в нескольких частях
    TEXT_PLAIN: str = "text/plain"  # передает простой текст
