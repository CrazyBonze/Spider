#!/usr/bin/python
import os

#Each website to crawl is a separate project
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating project ' + directory)
        os.makedirs(directory)


