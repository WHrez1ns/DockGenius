#!/usr/bin/python3
# _*_ coding: utf-8 _*_

from decouple import config
import requests

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def line():
    print(f"=======================================================")

def enter_for_continue():
    line()
    input("Press" + Colors.BOLD + " ENTER " + Colors.ENDC + "for continue...")

def list_containers():
    print("Listing containers:")
    line()
    response = requests.get(f"{API_ADDRESS}/v1.43/containers/json?all=true").json()
    for container in response:
        print(Colors.GREEN + "Container:" + Colors.ENDC, container)
    enter_for_continue()

def create_a_container():
    print("Creating a container:")
    line()
    response = requests.post(f"{API_ADDRESS}/v1.43/containers/create&Hostname=Renan&Image=httpd")
    print(Colors.GREEN + "Container created:" + Colors.ENDC, response.json(), response.status_code)
    enter_for_continue()

def list_processes_running_inside_a_container():
    print("Listing all processes running inside a container:")
    line()
    all_containers = requests.get(f"{API_ADDRESS}/v1.43/containers/json?all=true").json()
    for container in all_containers:
        container_id = container["Id"]
        response = requests.get(f"{API_ADDRESS}/v1.43/containers/{container_id}/top").json()
        print(Colors.GREEN + "Processes:" + Colors.ENDC, response)
    enter_for_continue()

def get_container_log():
    print("Geting containers log:")
    line()
    all_containers = requests.get(f"{API_ADDRESS}/v1.43/containers/json?all=true").json()
    for container in all_containers:
        container_id = container["Id"]
        response = requests.get(f"{API_ADDRESS}/v1.43/containers/{container_id}/logs?follow=true&stdout=true").json()
        print(Colors.GREEN + "Logs:" + Colors.ENDC, response)
    enter_for_continue()

def start_a_container():
    print("Starting a container:")
    line()
    container_id = input("ID or name of the container: ")
    response = requests.post(f"{API_ADDRESS}/v1.43/containers/{container_id}/start")
    print(Colors.GREEN + "Response:" + Colors.ENDC, response.status_code)
    enter_for_continue()

def stop_a_container():
    print("Stoping a container:")
    line()
    container_id = input("ID or name of the container: ")
    response = requests.post(f"{API_ADDRESS}/v1.43/containers/{container_id}/stop")
    print(Colors.GREEN + "Response:" + Colors.ENDC, response.status_code)
    enter_for_continue()

def restart_a_container():
    print("Restarting a container:")
    line()
    container_id = input("ID or name of the container: ")
    response = requests.post(f"{API_ADDRESS}/v1.43/containers/{container_id}/restart")
    print(Colors.GREEN + "Response:" + Colors.ENDC, response.status_code)
    enter_for_continue()

def kill_a_container():
    print("Killing a container:")
    line()
    container_id = input("ID or name of the container: ")
    response = requests.post(f"{API_ADDRESS}/v1.43/containers/{container_id}/kill")
    print(Colors.GREEN + "Response:" + Colors.ENDC, response.status_code)
    enter_for_continue()

def remove_a_container():
    print("Removing a container:")
    line()
    container_id = input("ID or name of the container: ")
    response = requests.delete(f"{API_ADDRESS}/v1.43/containers/{container_id}?v=true&force=true&link&true")
    if response.status_code != "204":
        print(Colors.GREEN + "Response:" + Colors.ENDC, response.status_code)
    else:
        print(Colors.GREEN + "Response:" + Colors.ENDC, response.status_code)
    enter_for_continue()

def list_images():
    print("Listing images: ")
    line()
    images = requests.get(f"{API_ADDRESS}/v1.43/images/json").json()
    for image in images:
        print(Colors.GREEN + "Image:" + Colors.ENDC, image)
    enter_for_continue()

def remove_a_image():
    print("Removing a image:")
    line()
    image_id = input("Image name or ID: ")
    response = requests.delete(f"{API_ADDRESS}/v1.43/images/{image_id}?force=true").json()
    print(Colors.GREEN + "Response:" + Colors.ENDC, response)
    enter_for_continue()

def get_system_information():
    print("Geting system infomation: ")
    line()
    response = requests.get(f"{API_ADDRESS}/v1.43/info").json()
    print(Colors.GREEN + "System information:" + Colors.ENDC, response)
    enter_for_continue()

def ping():
    print("Testing if the server is accessible: ")
    line()
    response = requests.get(f"{API_ADDRESS}/v1.43/_ping")
    print(Colors.GREEN + "Ping:" + Colors.ENDC, response.status_code)
    enter_for_continue()

def get_data_usage_information():
    print("Geting data usage information: ")
    line()
    response = requests.get(f"{API_ADDRESS}/v1.43/system/df").json()
    print(Colors.GREEN + "Data usage:" + Colors.ENDC, response)
    enter_for_continue()

def get_version():
    print("Geting version: ")
    line()
    response = requests.get(f"{API_ADDRESS}/v1.43/version").json()
    print(Colors.GREEN + "Version:" + Colors.ENDC, response['Version'])
    enter_for_continue()

API_ADDRESS = config('API_ADDRESS')

line()
print(Colors.HEADER + "DockGenius" + Colors.ENDC)

while True:
    try:
        line()
        print("Select a option from interact with the Docker: ")
        print(Colors.BLUE + "[1] " + Colors.ENDC + "List containers")
        print(Colors.BLUE + "[2] " + Colors.ENDC + "Create a containers")
        print(Colors.BLUE + "[3] " + Colors.ENDC + "List processes running inside a container")
        print(Colors.BLUE + "[4] " + Colors.ENDC + "Get containers log")
        print(Colors.BLUE + "[5] " + Colors.ENDC + "Start a container")
        print(Colors.BLUE + "[6] " + Colors.ENDC + "Stop a container")
        print(Colors.BLUE + "[7] " + Colors.ENDC + "Restart a container")
        print(Colors.BLUE + "[8] " + Colors.ENDC + "Kill a container")
        print(Colors.BLUE + "[9] " + Colors.ENDC + "Remove a container")
        print(Colors.BLUE + "[10] " + Colors.ENDC + "List Images")
        print(Colors.BLUE + "[11] " + Colors.ENDC + "Remove an image")
        print(Colors.BLUE + "[12] " + Colors.ENDC + "Get system information")
        print(Colors.BLUE + "[13] " + Colors.ENDC + "Ping")
        print(Colors.BLUE + "[14] " + Colors.ENDC + "Get data usage information")
        print(Colors.BLUE + "[15] " + Colors.ENDC + "Get version")
        print(Colors.FAIL + "[99] " + Colors.ENDC + "Exit")

        user_response = int(input(": "))
        line()

        if user_response==1:
            list_containers()
        elif user_response==2:
            create_a_container()
        elif user_response==3:
            list_processes_running_inside_a_container()
        elif user_response==4:
            get_container_log()
        elif user_response==5:
            start_a_container()
        elif user_response==6:
            stop_a_container()
        elif user_response==7:
            restart_a_container()
        elif user_response==8:
            kill_a_container()
        elif user_response==9:
            remove_a_container()
        elif user_response==10:
            list_images()
        elif user_response==11:
            remove_a_image()
        elif user_response==12:
            get_system_information()
        elif user_response==13:
            ping()
        elif user_response==14:
            get_data_usage_information()
        elif user_response==15:
            get_version()
        elif user_response==99:
            break
        else:
            print(Colors.FAIL + "Invalid option" + Colors.ENDC)
    except ValueError:
        line()
        print(Colors.FAIL + "Invalid option" + Colors.ENDC)
    except:
        line()
        print(Colors.FAIL + "Unexpected error" + Colors.ENDC)