#!/usr/bin/python3
""" initialisation"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class wgich defines a Square"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for width."""

        return self.width

    @size.setter
    def size(self, value):
        """Setter for width."""

        self.width = self.validator("width", value)
        self.height = self.validator("width", value)

    def __str__(self):
        """Returns [Square] (<id>)
        <x>/<y> - <square>
        """

        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""

        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.size = args[1]
        if len(args) > 2:
            self.x = args[2]
        if len(args) > 3:
            self.y = args[3]
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""

        return {"id": self.id, "x": self.x, "size": self.size, "y": self.y}

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        obj_list = [obj.to_dictionary() for obj in list_objs]
        json_str = cls.to_json_string(obj_list)
        with open(filename, "w") as f:
            f.write(json_str)
