from typing import Union, List

from pyrogram import filters

other_filters2 = filters.private & ~ filters.edited & ~ filters.via_bot & ~ filters.forwarded
