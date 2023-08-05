from typing import List, Union
from mathkeyboardengine.Placeholder import Placeholder

def get_first_non_empty_on_left_of(list: List[Placeholder], element: Placeholder) -> Union[Placeholder, None]:
  isOnTheLeft = False
  for i in range(len(list) - 1, -1, -1):
    placeholder: Placeholder = list[i]
    if not isOnTheLeft:
      if placeholder == element:
        isOnTheLeft = True
      continue

    if len(placeholder.nodes) > 0:
      return placeholder
  return None
