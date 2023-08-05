from typing import Union
from mathkeyboardengine.Placeholder import Placeholder
from mathkeyboardengine.StandardBranchingNode import StandardBranchingNode

class AscendingBranchingNode(StandardBranchingNode):
  def get_move_down_suggestion(self, fromPlaceholder: Placeholder) -> Union[Placeholder, None]:
    currentPlaceholderIndex = self.placeholders.index(fromPlaceholder)
    if currentPlaceholderIndex > 0:
      return self.placeholders[currentPlaceholderIndex - 1]
    else:
      return None  

  def get_move_up_suggestion(self, fromPlaceholder: Placeholder) -> Union[Placeholder, None]:
    currentPlaceholderIndex = self.placeholders.index(fromPlaceholder)
    if currentPlaceholderIndex < len(self.placeholders) - 1:
      return self.placeholders[currentPlaceholderIndex + 1]
    else:
      return None
