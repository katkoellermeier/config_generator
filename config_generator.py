from string import Template
import jinja2 

# Jinja2 template for Cisco switch interface VLAN assignment configuration
interface_template = """
interface {{ interface_name }}
 switchport access {{ vlan_id }}
end
"""

# Get user input
interface_name = input("Interface name (e.g., GigabitEthernet1/0/1)? ")
vlan_id = input("VLAN ID? ")

# Render the template
interfacetemplate = jinja2.Template(interface_template)
a = interfacetemplate.render(interface_name=interface_name, vlan_id=vlan_id)

print(a)