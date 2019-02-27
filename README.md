# data-interfaces-flask

![screenshot_2019-02-20_10-50-57](https://user-images.githubusercontent.com/19608381/53065397-13cc3b80-34fe-11e9-957a-41444ba38507.png)


Display Cisco IOS router and switch interfaces information using Flask. Simple usage, just set up ssh on your router and sign in with this website.

### Requirements

- Flask
- Netmiko
- TextFSM

### How to Use

```
git clone https://github.com/hasri20/data-interfaces-flask/
cd data-interfaces-flask
python3 app.py
```

Open [http://0.0.0.0:8080](http://0.0.0.0:8080) in your browser.

### Test using DevNet Sandbox

Don't have a router or switch? No problem, you can use this [DevNet Always-On Sandbox](https://devnetsandbox.cisco.com/RM/Diagram/Index/27d9747a-db48-4565-8d44-df318fce37ad?diagramType=Topology). 

The required information from the sandbox environment is provided here for convenience, but we recommend you access the [sandbox](https://devnetsandbox.cisco.com/RM/Diagram/Index/27d9747a-db48-4565-8d44-df318fce37ad?diagramType=Topology) to make sure this information is still current. 

- Hostname: ios-xe-mgmt.cisco.com
- SSH Port: 8181
- Username: root
- Password: D_Vay!_10&

