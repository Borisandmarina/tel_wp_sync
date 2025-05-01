import asyncio
import state
import wordpress

async def check_and_trigger():
    if state.check_timer_due():
        state.set_state("red")
        wordpress.update_wp()
        print("⏱ Таймер сработал: переключено на красный")

async def periodic_check(app):
    while True:
        await check_and_trigger()
        await asyncio.sleep(60)  # Проверка каждую минуту

def start_timer_check(app):
    app.create_task(periodic_check(app))