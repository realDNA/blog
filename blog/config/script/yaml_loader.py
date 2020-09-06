import os
import yaml


class YamlLoader():
    def __init__(self):
        self.BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/yaml_files/"

    def yaml_loader(self, file_name):
        with open(self.BASE_DIR + file_name, 'r') as stream:
            try:
                return (yaml.safe_load(stream))
            except yaml.YAMLError as exc:
                print(exc)

    def get_keys(self, dict):
        return list(dict.keys())


# if __name__=="__main__":
#     data = YamlLoader().yaml_loader("catagorization.yml")
#     keys = YamlLoader().get_keys(data)
#     print("keys = ", keys)