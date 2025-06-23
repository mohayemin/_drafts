from Cheetah import Template


def load_config():
    pxe_config = str(Template.Template(
            open("template.txt").read(),
            searchList=[{
                'VALUE': 5,
                'ROOT': '${ROOT}',
            }]))
    return pxe_config