# tel_wp_sync/scheduler.py

import asyncio
import state
import wordpress
from datetime import datetime

async def periodic_check(app):
    while True:
        timer_str = state.get_timer()
        if timer_str:
            try:
                target = datetime.strptime(timer_str, "%Y-%m-%d %H:%M")
                now = datetime.now()
                if target > now:
                    delta = (target - now).total_seconds()
                    await asyncio.sleep(delta)
                    state.set_state("red")
                    wordpress.update_wp()
                    state.clear_timer()
            except:
                pass
        await asyncio.sleep(30)

async def post_init(app):
    app.create_task(periodic_check(app))