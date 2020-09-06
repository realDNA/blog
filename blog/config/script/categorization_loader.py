from .yaml_loader import YamlLoader


def load_category_data(file_name="catagorization.yml"):
    data = YamlLoader().yaml_loader(file_name)
    return data


def get_keys(dict_data):
    keys = YamlLoader().get_keys(dict_data)
    return keys


def get_alias(dict_data):
    alias = []
    for data in dict_data:
        alias.append(list(dict_data.get(data)[0].values())[0])
    return alias

# if __name__=="__main__":
#     data = load_category_data("catagorization.yml")
#     keys = get_keys(data)
#     print("data = ", data)
#     print("keys = ", keys)