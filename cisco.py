from netmiko import ConnectHandler
import textfsm 

class router(object):

	def __init__(self,device_type,ip,username,password,port):
		self.device_type = device_type
		self.ip = ip
		self.username = username
		self.password = password
		self.port = port

	def connect(self):

		cisco_vios = {
    		'device_type':self.device_type,
    		'ip': self.ip,
    		'username':self.username,
    		'password': self.password,
			'port': self.port
			}

		net_connect = ConnectHandler(**cisco_vios)
		string_interface = net_connect.send_command('show interfaces')
		template_file = open("showinterface.template")
		template = textfsm.TextFSM(template_file)
		result_template = template.ParseText(string_interface)

		interface_list = []
		for list in result_template:
			resultDict = {}
			resultDict["interface"] = list[0]
			resultDict["mac address"] = list[1]
			resultDict["ip address"] = list[2]
			resultDict["MTU"] = list[3]
			resultDict["bandwith"] = list[4]

			interface_list.append(resultDict)
		return interface_list

