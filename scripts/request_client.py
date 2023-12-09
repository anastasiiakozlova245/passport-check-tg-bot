import json
import logging
import os

URL = f"https://info.midpass.ru/api/request_ex/{os.getenv('EMBASSY_ID')}/{os.getenv('APPLICATION_ID')}"


def get(logger):
    # r = requests.get(URL)
    # logger.info(f"API request status code: {r.status_code}")
    os.system(f"curl {URL} > response.json")
    with open("response.json", "r") as f:
        r = f.read()
    if r:
        print(r[1:-1])
        return json.loads(r)


if __name__ == "__main__":
    logger = logging.getLogger()
    logger.setLevel(level="INFO")

    # URL = 'https://dummy.restapiexample.com/api/v1/employee/1'

    logging.info("Passport bot has been initialized")
    response = get(logger)[0]
    # logger.info(f"Test status: {response.get('message')}")
    logger.info(
        f"Готовность: {response.get('internalStatus').get('percent')}%, статус: {response.get('passportStatus').get('name')}, внутренний статус: {response.get('internalStatus').get('name')}"
    )
