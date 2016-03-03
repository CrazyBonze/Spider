#!/usr/bin/env python3
import threading
import argparse
from queue import Queue
from spider import Spider
from domain import *
from general import *

parser = argparse.ArgumentParser(description="Multi-rhreaded website crawler written in Python")

parser.add_argument("--flush", help="empty project folder prior to crawling", action="store_true")

args = parser.parse_args()

PROJECT_NAME = 'wiki'
HOMEPAGE = 'https://en.wikipedia.org/wiki/'
DOMAIN_NAME = get_domain_name(HOMEPAGE)

QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 8
queue = Queue()

attrs = {
    'project_name': PROJECT_NAME,
    'base_url': HOMEPAGE,
    'domain_name': DOMAIN_NAME,
    'flush': args.flush
}

Spider(attrs)


# Create worker threads (will die when main exits)
def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()


# Do the next job in the queue
def work():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()


# Each queued link is a new job
def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()


# Check if there are items in the queue, if so crawl them
def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    if queued_links:
        number_of_links = len(queued_links)
        print('{} links in the queue'.format(number_of_links))
        create_jobs()

create_workers()
crawl()
