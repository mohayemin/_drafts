from Cheetah import Template


def load_config():
    pxe_config = str(Template.Template(
            open("template/config.txt").read(),
            searchList=[{
                'VALUE': 5,
                'ROOT': '${ROOT}',
            }]))
    return pxe_config