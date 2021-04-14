import requests
import os
import json


class ApiConnector:
    """[This class is for defining endpoints and API keys.]"""

    def __init__(self):
        self.servers_endpoint = "https://api.hetzner.cloud/v1/servers"
        self.locations_endpoint = "https://api.hetzner.cloud/v1/locations"
        self.images_endpoint = "https://api.hetzner.cloud/v1/images"
        self.key = "APIHETZNER"
        self.token = os.getenv(self.key)
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
        }


class GetVmList(ApiConnector):
    """[This class is getting list of VMs.]"""

    def get_vms_list(self):
        request = requests.get(self.servers_endpoint, headers=self.headers).json()
        # print (request)
        #print (request["servers"])
        existing_servers = [
            (x["name"], x["id"], x["status"]) for x in request["servers"]
        ]
        return existing_servers


class CreateVm(ApiConnector):
    """[This class is validate data and create VMs]"""

    def create_vm(self, location="hel1", name="MyServer", image="ubuntu-20.04"):
        request = requests.get(self.images_endpoint, headers=self.headers).json()
        existing_images = [x["name"] for x in request["images"]]
        if image not in existing_images:
            raise ValueError(
                f'Wrong image name. Valid values are: { ", ".join(existing_images) }'
            )

        request = requests.get(self.locations_endpoint, headers=self.headers).json()
        existing_locations = [x["name"] for x in request["locations"]]
        if location not in existing_locations:
            raise ValueError(
                f'Wrong datacenter. Valid values are: { ", ".join(existing_locations) }'
            )

        data = {
            "name": name,
            "location": location,
            "server_type": "cx11",
            "image": image,
        }
        result = requests.post(
            self.servers_endpoint, data=json.dumps(data), headers=self.headers
        ).json()
        print (result)

        return json.dumps(result, indent=2, default=str)

if __name__ == "__main__":
    my_vm = CreateVm().create_vm(name="MyServer1", location="hel1", image="ubuntu-20.04")
    print(my_vm)
    vm_list = GetVmList().get_vms_list()
    print(vm_list)

# vm_list = GetVmList().get_vms_list()
# print(vm_list)