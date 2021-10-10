import os
import csv
import sys
from os import path
from configparser import ConfigParser

def calculate_files_size(path):
    size = 0
    for path, _, files in os.walk(path):
        for f in files:
            fp = os.path.join(path, f)
            size += os.path.getsize(fp)

    #MiB
    return "{:.2f}".format(size / (1024 ^2))

def create_csv(container_data):
    config = ConfigParser()
    config.read('src/config.ini')
    output_path = config['Default']['output_path']

    if not path.exists(output_path):
        raise SystemExit('\nOutput directory does not exist.')

    # Create header
    header = [i for i in container_data[0]]

    with open(output_path + "/docker_list.csv", "w") as list_file:
        docker_file = csv.writer(list_file)
        docker_file.writerow(header)
        for container in container_data:
            docker_file.writerow(list(container.values()))

def progress(actual, max):
    progress_bar = int((actual / max) * 100)
    sys.stdout.write(('\r[ {}% ] {}>{}'.format(progress_bar, '=' * progress_bar, '' * (max - actual))))
    sys.stdout.flush()