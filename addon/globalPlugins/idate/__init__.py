# -*- coding: UTF-8 -*-
import os
import sys
from datetime import datetime
import ui
import globalPluginHandler
import scriptHandler

sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__))))

import hijridate

sys.path.remove(sys.path[-1])

MONTHS = (
    "Muharram",
    "Safar",
    "Rabi al-Awwal",
    "Rabi al-Thani",
    "Jumada al-Awwal",
    "Jumada al-Thani",
    "Rajab",
    "Sha'ban",
    "Ramadan",
    "Shawwal",
    "Dhu al-Qi'dah",
    "Dhu al-Hijjah",
)


class GlobalPlugin(globalPluginHandler.GlobalPlugin):
    def __init__(self):
        super().__init__()

    @scriptHandler.script(
        gesture="kb:nvda+shift+h", description="Get Islamic Date", category="idate"
    )
    def script_date(self, gesture):
        """Get Islamic date"""
        current_date = datetime.now()
        gregorian_date = hijridate.Gregorian(
            current_date.year, current_date.month, current_date.day
        )
        date = gregorian_date.to_hijri()
        month_name = MONTHS[date.month - 1]
        date_str = f"{date.day} {month_name} {date.year}"
        ui.message(date_str)
