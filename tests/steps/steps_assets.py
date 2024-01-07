import allure

from time import sleep
from api.assets import AssetsRequests


class StepsAssets:

    @allure.step("Найти созданный asset в preview и в thumbnail")
    def step_find_asset(self, token: str, pk_id: int, range_time: int = 3):
        for i in range(range_time):
            _, response = AssetsRequests().find_asset_perform(token=token)
            result = response['results']
            data_list = [item for item in result if item['id'] == pk_id]
            if not data_list:
                sleep(range_time)
            else:
                break

        data = data_list[0]
        preview = data["preview"]
        thumbnail = data["thumbnail"]

        return preview, thumbnail
