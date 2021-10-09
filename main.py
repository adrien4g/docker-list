from sys import path
path.insert(0, 'src/')
from docker_conf import DockerList

if __name__ == "__main__":
    d = DockerList()
    d.get_data()