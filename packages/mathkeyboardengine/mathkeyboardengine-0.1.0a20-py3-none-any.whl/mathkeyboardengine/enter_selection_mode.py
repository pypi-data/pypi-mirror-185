from mathkeyboardengine.KeyboardMemory import KeyboardMemory
from mathkeyboardengine._helpers._helpers.set_selection_diff import set_selection_diff

def enter_selection_mode(k: KeyboardMemory) -> None:
  set_selection_diff(k, 0)
