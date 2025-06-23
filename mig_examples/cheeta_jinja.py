from Cheetah import Template


def load_config():
  values = {
    'VALUE': 5,
    'ROOT': '${ROOT}',
  }
  tmpl_file = open("template/config.txt").read()
  tmpl = Template.Template(tmpl_file, searchList=[values])
  pxe_config = str(tmpl)
  return pxe_config
