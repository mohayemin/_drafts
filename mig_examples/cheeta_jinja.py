import jinja2


def load_config():
  values = {
    'VALUE': 5,
    'ROOT': '{{ ROOT }}'
  }
  tmpl_path, tmpl_file = os.path.split("template/config.txt")
  loader = loader=jinja2.FileSystemLoader(tmpl_path)
  env = jinja2.Environment(loader=loader)
  template = env.get_template(tmpl_file)

  return template.render(values)

