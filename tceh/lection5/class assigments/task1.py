class Trash(object):
    def __init__(self, volume=15):
        self.volume = volume
        self.items = []

    def put_obj(self, obj):
        if self.volume >= obj.volume:
            self.items.append(obj)
            self.volume -= obj.volume
            print("Item succesfully added.")
        else:
            print("There are lack of place for this item.")

    def extract_obj(self, obj):
        if obj in self.items:
            self.volume += obj.volume
            self.items.remove(obj)
            print("Item succesfully extracted.")
        else:
            print("There is no such object.")


class Package(Trash):
    def __init__(self, volume=5):
        super().__init__(volume)


class Box(object):
    def __init__(self, volume):
        self.volume = volume


a = Box(2)
b = Box(9)
c = Box(11)
d = Box(3)

package = Package()
trash = Trash()

package.put_obj(c)
package.put_obj(b)
package.extract_obj(c)

trash.put_obj(a)
trash.put_obj(b)
trash.put_obj(c)
trash.extract_obj(a)
