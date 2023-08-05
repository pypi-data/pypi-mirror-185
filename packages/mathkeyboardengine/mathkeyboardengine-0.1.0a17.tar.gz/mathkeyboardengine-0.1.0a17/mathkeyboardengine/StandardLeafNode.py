from typing import Callable, Union
from mathkeyboardengine.KeyboardMemory import KeyboardMemory
from mathkeyboardengine.LatexConfiguration import LatexConfiguration
from mathkeyboardengine.LeafNode import LeafNode

class StandardLeafNode(LeafNode):
  def __init__(self, latex: Union[str, Callable[[], str]]) -> None:
    self.latex : Callable[[], str] = (lambda : latex) if isinstance(latex, str) else latex
  
  def get_latex_part(self, k: KeyboardMemory, latexconfiguration: LatexConfiguration) -> str:
    return self.latex()
