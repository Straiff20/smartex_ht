import uuid
from pydantic.main import BaseModel


class AssetValuesModel(BaseModel):
    title: str = "Pliev"
    description: str = "file description"


class AssetCreateModel(BaseModel):
    """
    - external_id должен быть уникальной строкой
    """
    content_type: str = "base"
    external_id: str = str(uuid.uuid4())
    values: AssetValuesModel = AssetValuesModel()


class AssetDeleteManyModel(BaseModel):
    id__in: list[int]
