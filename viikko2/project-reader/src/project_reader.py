from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        parsed_toml = toml.loads(content)
        toml_stuff = parsed_toml["tool"]["poetry"]

        print(toml_stuff)
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(toml_stuff["name"], 
                       toml_stuff["description"],
                       toml_stuff["license"],
                       toml_stuff["authors"],
                       toml_stuff["dependencies"], 
                       toml_stuff["group"]["dev"]["dependencies"])
