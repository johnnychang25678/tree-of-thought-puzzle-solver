

class Config:

    # TODO: load from a config file
    def __init__(self, openai_model:str, openai_api_key: str, user_azure: bool) -> None:
        self.openai_model = openai_model
        self.openai_api_key = openai_api_key
        self.use_azure = user_azure
