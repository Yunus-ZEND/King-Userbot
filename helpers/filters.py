from typing import Union, List

other_filters2 = filters.private & ~ filters.edited & ~ filters.via_bot & ~ filters.forwarded

def command(commands: Union[str, List[str]]):
    return filters.command(commands)
