from netmiko import ConnectHandler
from textfsm import TextFSM
import os

def connect(device_type,ip,username,password,port):

	device = {
		'device_type': device_type,
		'ip': ip,
		'username': username,
		'password':  password,
		'port': port
		}

	return ConnectHandler(**device)


def get_interfaces_list(device):
	output_interfaces = device.send_command('show interfaces')
	current_dir = os.getcwd()
	template_file = open(current_dir +"/controller/show_interface.template", "r")
	template = TextFSM(template_file)
	parsed_interfaces = template.ParseText(output_interfaces)

	interface_list = []
	for interface_data in parsed_interfaces:
		resultDict = {}
		resultDict["interface"] = interface_data[0]
		resultDict["mac address"] = interface_data[1]
		resultDict["ip address"] = interface_data[2]
		resultDict["MTU"] = interface_data[3]
		resultDict["bandwith"] = interface_data[4]

		interface_list.append(resultDict)

	return interface_list