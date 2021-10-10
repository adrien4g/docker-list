import docker
from .utils import *
from configparser import ConfigParser

class DockerList:
    data = []

    def __init__(self):
        self.dockerClient = docker.from_env()
        self.client = docker.APIClient(base_url='unix://var/run/docker.sock')
        self.config = ConfigParser()
        
        self.config.read('src/config.ini')

    def get_data(self):
        verify_directorys()
        print('Getting list of containers...')
        container_list = self.dockerClient.containers.list()
        progress_counter = 1
        for container in container_list:
            progress(progress_counter, len(container_list))
            selected_container = self.client.inspect_container(container.id)
            if self.check_for_docker_compose(selected_container):
                self.container_data = {
                    "id"          : selected_container["Id"],
                    "name"        : selected_container["Name"][1:],
                    "state"       : selected_container["State"]["Status"],
                    "image"       : selected_container['Config']["Image"],
                    "docker_compose" : selected_container['Config']['Labels']["com.docker.compose.project.working_dir"] + "/" + selected_container['Config']['Labels']["com.docker.compose.project.config_files"],
                    "volume"      : [],
                    "volume_size" : []
                }
                for vol in selected_container["Mounts"]:
                    self.container_data.volume.append([
                        vol["Source"],
                        vol["Destination"]
                    ])
                    self.container_data.volume_size.append(calculate_files_size(vol["Source"]))

                self.data.append(self.container_data)
            progress_counter += 1

        new_data = sorted(self.data, key=lambda x: x['docker_compose'])
        if len(new_data) != 0:
            create_csv(new_data)
    
    def check_for_docker_compose(self, container):
        try:
            path = container['Config']['Labels']["com.docker.compose.project.working_dir"]
        except:
            return False

        return True if self.config["Default"]["base_path"] in path else False