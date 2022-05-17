from sourses.SerializerJson import SerializerJson as js
from sourses.SerializerToml import SerializerToml as ts
from sourses.SerializerYaml import SerializerYaml as ys

class SerializerFactory:
    def __init__(self, path: str):
        self.path = path

    def create_serializer(self, extension="json"):
        if extension.lower() == "json":
            return js.SerializerJson(self.path)
        #elif extension.lower() == "pickle":
            #return ps.PickleSerializer(self.path)
        elif extension.lower() == "toml":
            return ts.SerializeToml(self.path)
        elif extension.lower() == "yaml":
            return ys.SerializeYaml(self.path)