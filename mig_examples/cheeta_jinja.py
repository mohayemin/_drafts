from jinja2 import Environment, FileSystemLoader

def load_config():
  TMPL_PATH = "template/config.txt"
  values = {
    'VALUE': 5,
    'ROOT': '{{ ROOT }}'
  }
  path, file = os.path.split(TMPL_PATH)
  loader = FileSystemLoader(path)
  env = Environment(loader=loader)
  template = env.get_template(file)
  
  pxe_config = template.render(values)
  return pxe_config
