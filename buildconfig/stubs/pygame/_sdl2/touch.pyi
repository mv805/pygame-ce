from typing import Union, Optional

def get_num_devices() -> int: ...
def get_device(index: int, /) -> int: ...
def get_num_fingers(device_id: int, /) -> int: ...
def get_finger(touchid: int, index: int) -> Optional[dict[str, Union[int, float]]]: ...
