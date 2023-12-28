from dataclasses import dataclass


@dataclass
class ErrorTexts:
    not_exist_asset = {"detail": "Asset matching query does not exist."}
