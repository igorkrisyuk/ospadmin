"""The hello command."""


from json import dumps

from .base import Base


class Cluster(Base):
    """Wercker cluster admin command create/delete"""

    def run(self):
        print('Cluster comand')
        print('You supplied the following options:', dumps(self.options, indent=2, sort_keys=True))
        print('You supplied the following args:', dumps(self.args, indent=2, sort_keys=True))
        print('You supplied the following kwargs:', dumps(self.kwargs, indent=2, sort_keys=True))

    def create(self):
        print("Create cluster")

    def delete(self):
        print("Delete cluster")

    def update(self):
        print("Update cluster")