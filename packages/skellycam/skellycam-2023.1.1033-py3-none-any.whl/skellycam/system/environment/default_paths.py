import time
from datetime import datetime
from pathlib import Path

import skellycam
from skellycam.system.environment.home_dir import os_independent_home_dir

DEFAULT_SKELLYCAM_BASE_FOLDER_NAME = "skelly-cam-recordings"
SYNCHRONIZED_VIDEOS_FOLDER_NAME = "synchronized_videos"
TIMESTAMPS_FOLDER_NAME = "timestamps"

SESSION_START_TIME_FORMAT_STRING = "ISO6201 format timestamp with GMT offset in hours"

PATH_TO_SKELLY_CAM_LOGO_SVG = str(
    Path(skellycam.__file__).parent / "assets/logo/skelly-cam-logo.svg"
)


def get_default_skellycam_base_folder_path():
    return Path(os_independent_home_dir()) / DEFAULT_SKELLYCAM_BASE_FOLDER_NAME


def get_default_session_folder_path(create_folder: bool = True, string_tag: str = None):
    folder_path = get_default_skellycam_base_folder_path() / default_session_name(string_tag=string_tag)
    if create_folder:
        folder_path.mkdir(parents=True, exist_ok=True)
    return str(folder_path)


def get_gmt_offset_string():
    # from - https://stackoverflow.com/a/53860920/14662833
    gmt_offset_int = int(time.localtime().tm_gmtoff / 60 / 60)
    return f"{gmt_offset_int:+}"


def get_iso6201_time_string():
    iso6201_timestamp = datetime.now().isoformat(timespec="milliseconds")
    gmt_offset_string = f"_GMT{get_gmt_offset_string()}"
    iso6201_timestamp_w_gmt = iso6201_timestamp + gmt_offset_string
    return iso6201_timestamp_w_gmt


def default_session_name(string_tag: str = None):
    if string_tag is not None:
        string_tag = f"_{string_tag}"
    else:
        string_tag = ""

    return time.strftime("%Y-%m-%d_%H_%M_%S" + string_tag)
