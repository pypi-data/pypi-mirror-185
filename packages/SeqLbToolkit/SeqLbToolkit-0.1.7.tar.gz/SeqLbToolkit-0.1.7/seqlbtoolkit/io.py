from lib2to3.pgen2.token import OP
from optparse import Option
import os
import re
import tqdm
import json
import shutil
import logging
from pathlib import Path
from typing import Optional

logger = logging.getLogger(__name__)


class TqdmLoggingHandler(logging.Handler):
    """
    Don't let logger print interfere with tqdm progress bar
    """
    def __init__(self, level=logging.NOTSET):
        super().__init__(level)

    def emit(self, record):
        try:
            msg = self.format(record)
            tqdm.tqdm.write(msg)
            self.flush()
        except Exception:
            self.handleError(record)


# noinspection PyArgumentList
def set_logging(log_dir: Optional[str] = None):
    """
    setup logging
    Last modified: 07/20/21

    Parameters
    ----------
    log_dir: where to save logging file. Leave None to save no log files

    Returns
    -------

    """
    if log_dir and log_dir != 'null':
        log_dir = os.path.abspath(log_dir)
        if not os.path.isdir(os.path.split(log_dir)[0]):
            os.makedirs(os.path.abspath(os.path.normpath(os.path.split(log_dir)[0])))
        if os.path.isfile(log_dir):
            os.remove(log_dir)
        logging.basicConfig(
            format="%(asctime)s - %(levelname)s - %(name)s -   %(message)s",
            datefmt="%m/%d/%Y %H:%M:%S",
            level=logging.INFO,
            handlers=[
                # logging.StreamHandler(sys.stdout),
                logging.FileHandler(log_dir),
                TqdmLoggingHandler(),
            ],
        )
    else:
        logging.basicConfig(
            format="%(asctime)s - %(levelname)s - %(name)s -   %(message)s",
            datefmt="%m/%d/%Y %H:%M:%S",
            level=logging.INFO,
            handlers=[
                # logging.StreamHandler(sys.stdout),
                TqdmLoggingHandler()
            ],
        )


def logging_args(args):
    """
    Logging model arguments into logs
    Last modified: 08/19/21

    Parameters
    ----------
    args: arguments

    Returns
    -------
    None
    """
    arg_elements = {attr: getattr(args, attr) for attr in dir(args) if not callable(getattr(args, attr))
                    and not attr.startswith("__") and not attr.startswith("_")}
    logger.info(f"Parameters: ({type(args)})")
    for arg_element, value in arg_elements.items():
        logger.info(f"  {arg_element}: {value}")


def prettify_json(text, indent=2, collapse_level=4):
    pattern = r"[\r\n]+ {%d,}" % (indent * collapse_level)
    text = re.sub(pattern, ' ', text)
    text = re.sub(r'([\[({])+ +', r'\g<1>', text)
    text = re.sub(r'[\r\n]+ {%d}([])}])' % (indent * (collapse_level-1)), r'\g<1>', text)
    text = re.sub(r'(\S) +([])}])', r'\g<1>\g<2>', text)
    return text


def remove_dir(directory: str):
    """
    Remove a directory and its subtree folders/files
    """
    dirpath = Path(directory)
    if dirpath.exists() and dirpath.is_dir():
        shutil.rmtree(dirpath)
    return None


def init_dir(directory: str):
    """
    Create the target directory. If the directory exists, remove all subtree folders/files in it.
    """

    remove_dir(directory)
    os.makedirs(os.path.normpath(directory))
    return None


def save_json(obj, path: str, collapse_level: Optional[int] = None):
    """
    Save objective to a json file.
    Create this function so that we don't need to worry about creating parent folders every time

    Parameters
    ----------
    obj: the objective to save
    path: the path to save
    collapse_level: set to any collapse value to prettify output json accordingly

    Returns
    -------
    None
    """
    file_dir = os.path.split(path)[0]
    os.makedirs(file_dir, exist_ok=True)

    json_obj = json.dumps(obj, indent=2, ensure_ascii=False)
    if collapse_level:
        json_obj = prettify_json(json_obj, collapse_level=collapse_level)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(json_obj)

    return None


def prettify_json(text, indent=2, collapse_level=4):
    """
    Make json file more readable by collapsing indent levels higher than `collapse_level`.

    Parameters
    ----------
    text: input json text obj
    indent: the indent value of your json text. Notice that this value needs to be larger than 0
    collapse_level: the level from which the program stops adding new lines

    Usage
    -----
    ```
    my_instance = list()  # user-defined serializable data structure
    json_obj = json.dumps(my_instance, indent=2, ensure_ascii=False)
    json_obj = prettify_json(json_text, indent=2, collapse_level=4)
    with open(path_to_file, 'w', encoding='utf=8') as f:
        f.write(json_text)
    ```
    """
    pattern = r"[\r\n]+ {%d,}" % (indent * collapse_level)
    text = re.sub(pattern, ' ', text)
    text = re.sub(r'([\[({])+ +', r'\g<1>', text)
    text = re.sub(r'[\r\n]+ {%d}([])}])' % (indent * (collapse_level-1)), r'\g<1>', text)
    text = re.sub(r'(\S) +([])}])', r'\g<1>\g<2>', text)
    return text
