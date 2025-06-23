from Cheetah import Template

def load_config():
  TMPL_PATH = "template/config.txt"
  values = {
    'VALUE': 5,
    'ROOT': '${ROOT}',
  }
  tmpl_file = open(TMPL_PATH).read()
  tmpl = Template.Template(
    tmpl_file, 
    searchList=[values]
  )
  pxe_config = str(tmpl)
  return pxe_config
