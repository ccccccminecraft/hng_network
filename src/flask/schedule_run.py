import schedule
from time import sleep
from MinecraftServerChecker import MinecraftServerChecker


def task():
    print("check")
    mc_checker = MinecraftServerChecker()
    mc_checker.run()


schedule.every(60).seconds.do(task)
while True:
    schedule.run_pending()
    sleep(1)
