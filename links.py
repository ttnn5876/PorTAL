import json

class link:
    def __init__(self, name: str, path: str, hotkey: str):
        self.name = name
        self.path = path
        self.hotkey = hotkey

    def get_name(self):
        return self.name
    
    def get_path(self):
        return self.path

    def get_hotkey(self):
        return self.hotkey


class LinkException(Exception):
    pass

class links:
    def __init__(self):
        self.hotkeys = list()
        self.links = list()

        with open("c:\portal\links.json") as links_fd:
            data = json.load(links_fd)
        
        for link in data["links"]:
            self._create_link(link["name"], link["path"], link["hotkey"])

    def _create_link(self, name: str, path: str, hotkey: str):
        if hotkey in self.hotkeys:
            raise LinkException("Hotkey {0} Already exists".format(hotkey))
        
        self.links.append(link(name, path, hotkey))

    def get_links(self):
        for link in self.links:
            yield link

    def get_links_count(self):
        return len(self.links)
