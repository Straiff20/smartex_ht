import uuid
from pydantic.main import BaseModel


class AssetValuesModel(BaseModel):
    title: str = "Pliev"
    description: str = "file description"


class AssetCreateModel(BaseModel):
    """
    Общие сведения об asset для создания

    - external_id должен быть уникальной строкой
    """
    content_type: str = "base"
    external_id: str = str(uuid.uuid4())
    values: AssetValuesModel = AssetValuesModel()
