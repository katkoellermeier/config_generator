import jinja2

config_generator="""
as-path-set {{aspathset_name}}
  {{as_path_attribute}} '{{as_path_number}}'
end-set

elseif as-path in {{aspathset_name}} then
  set {{bgp_attribute}} {{attribute_number}}
  #{{ticket_number}}
  done """

aspathsetname = input("What is the as-path-set name?: ")
aspathattribute = input("""What is the as path attribute?
                        1. regex
                        2. length
                        3. neighbor-is
                        4. originates-from
                        5. passes-through
                        6. unique-length
                        > """)

aspathnumber = input("What is the as path number?: ")
bgpattribute = input("""Which bgp attribute is being manipulated?
                        1. local pref
                        2. med
                        > """)

attributenumber = input("What is the bgp attribute number?: ")
ticketnumber = input("What is the ticket number?: ")
config_generator= jinja2.Template(config_generator)
a = config_generator.render(aspathset_name=aspathsetname, as_path_attribute=aspathattribute, as_path_number=aspathnumber, bgp_attribute=bgpattribute, attribute_number=attributenumber, ticket_number=ticketnumber)

print(a)