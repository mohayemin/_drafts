from jinja2 import Environment, FileSystemLoader



def load_config():
  values = {
    'VALUE': 5,
    'ROOT': '{{ ROOT }}'
  }
  path, file = os.path.split("template/config.txt")
  loader = loader=FileSystemLoader(path)
  env = Environment(loader=loader)
  template = env.get_template(file)

  return template.render(values)

