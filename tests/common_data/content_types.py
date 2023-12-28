from dataclasses import dataclass


@dataclass
class ContentTypes:
    """
    Список доступных типов Content-Type
    """
    application_json: str = "application/json"
    application_xml: str = "application/xml"
    application_pdf: str = 'application/pdf'
    image_gif: str = "image/gif"
    image_jpeg: str = "image/jpeg"
    image_png: str = "image/png"
    multipart_form_data: str = "multipart/form-data"
    text_plain: str = "text/plain"
    audio_mp3: str = 'audio/mpeg'
