from typing import List
from shapes import Shape

class VectorEditor:
    """Core logic for managing a collection of shapes."""
    
    def __init__(self):
        self.shapes: List[Shape] = []

    def add_shape(self, shape: Shape):
        """Adds a shape to the editor."""
        self.shapes.append(shape)
        return len(self.shapes) - 1  # Return the index/ID of the added shape

    def remove_shape(self, index: int) -> bool:
        """Removes a shape by its index. Returns True if successful, False otherwise."""
        if 0 <= index < len(self.shapes):
            del self.shapes[index]
            return True
        return False

    def list_shapes(self) -> List[Shape]:
        """Returns the list of all shapes."""
        return self.shapes
