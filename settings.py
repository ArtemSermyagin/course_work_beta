from pathlib import Path

ROOT_PATH = Path(__file__).parent
DATA_PATH_2 = Path.joinpath(ROOT_PATH, "data")
OPEN_XLS = Path.joinpath(DATA_PATH_2, "operations.xls")
OPEN_JSON = Path.joinpath(DATA_PATH_2, "user_settings.json")
