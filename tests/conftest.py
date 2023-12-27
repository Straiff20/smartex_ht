import glob
import json
import sys

from utils.constatnts import ROOT_DIR

schemas_path = f'{ROOT_DIR}/api/schemas/'


def parse_schemas_path(folder: str):
    """
    Parse path of schemas into dict with name and json schema
    Example: {get_accounts: schemas_with_get_account}
    """
    paths = glob.glob(schemas_path + folder + "/*.json")
    names = [i.split('\\' if sys.platform == 'win32' else '/')[-1].split('.json')[0] for i in paths]
    schemas = {k: json.load(open(v, encoding='utf-8')) for k, v in zip(names, paths)}
    return schemas
