#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/18 14:06
# @Author  : Yuki
import _thread
import logging
from time import ctime, sleep

logging.basicConfig(level=logging.INFO)

loops = [2, 4]


def loop(nloop, nsec, lock):
    logging.info("strat loop" + str(nloop) + " at " + ctime())
    sleep(nsec)
    logging.info("end loop" + str(nloop) + " at " + ctime())
    lock.release()


# def loop0():
#     logging.info("strat loop0 at " + ctime())
#     sleep(4)
#     logging.info("end loop0 at " + ctime())
#
#
# def loop1():
#     logging.info("strat loop1 at " + ctime())
#     sleep(2)
#     logging.info("end loop1 at " + ctime())


def main():
    logging.info("strat all at " + ctime())
    locks = []
    nloops = range(len(loops))
    for i in nloops:
        lock = _thread.allocate_lock()
        lock.acquire()
        locks.append(lock)  # 将获取到的lock全部放入locks列表中
    for i in nloops:
        _thread.start_new_thread(loop, (i, loops[i], locks[i]))
    for i in nloops:
        while locks[i].locked():  pass
    # _thread.start_new_thread(loop0, ())
    # _thread.start_new_thread(loop1, ())
    # loop0()
    # loop1()
    # sleep(5)  # 主线程加这个强制等待且时间大于其他线程，原因是当主线程结束时，其他线程也会强制结束，_thread没有守护线程的功能，所以必须强制等待
    logging.info("end all at " + ctime())


if __name__ == '__main__':
    main()
