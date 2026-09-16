from configparser import ConfigParser

class Config:
    def __init__(self, config_file='src/agentic_ai/langgraphagenticai/ui/uiconfigfile.ini'):
        self.config = ConfigParser()
        self.config.read(config_file)

    def _get_options(self, name):
        return [option.strip() for option in self.config["DEFAULT"].get(name).split(',')]

    def get_llm_options(self):
        return self._get_options("LLM_OPTIONS")

    def get_usecase_options(self):
        return self._get_options("USECASE_OPTIONS")

    def get_model_options(self):
        return self._get_options("MODEL_OPTIONS")

    def get_page_title(self):
        return self.config["DEFAULT"].get("PAGE_TITLE")