from bunch import Bunch

class DictContainer(Bunch):
  def __init__(self, *args, **kwargs):
    Bunch.__init__(self, *args, **kwargs)

