#!/usr/bin/env python3
import os
import sys
import sqlite3 as db

#Each website to crawl is a separate project
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating project ' + directory)
        os.makedirs(directory)

#Create queue and crawled files
def create_data_files(project_name, base_url):
    try:
        connection = db.connect(project_name + '/' + project_name + '.db')
        cursor = connection.cursor()
        #create tables
        #insert base_url into queue table
    except db.Error as e:
        print('Error: ' + e.args[0])
        sys.exit(1)
    finally:
        if connection:
            connection.close()
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    if not os.path.exists(queue):
        write_file(queue, base_url)
    if not os.path.exists(crawled):
        write_file(crawled, '')

# Remove queue and crawled files (if exist)
def remove_data_files(project_name):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    db = project_name + '/' + project_name + '.db'
    if os.path.isfile(queue):
        os.remove(queue)
    if os.path.isfile(crawled):
        os.remove(crawled)
    if os.path.isfile(db):
        os.remove(db)

#Creates a new file
def write_file(path, data):
    with open(path, 'w') as f:
        f.write(data)

#Add data to an existing file
def append_to_file(path, data):
    with open(path, 'a') as f:
        f.write(data + '\n')

#Delete the contents of a file
def delete_file_contents(path):
    with open(path, 'w'):
        pass

#Convert file to set
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results

#Convert set to a file
def set_to_file(links, file):
    delete_file_contents(file)
    for link in sorted(links):
        append_to_file(file, link)

