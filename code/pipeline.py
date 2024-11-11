from typing import Callable


from base import DataLoader, Preprocess, Postprocess, Model, DataLoader



class Pipeline:

    def __init__(
            self, 
            data_config: dict, 
            preprocess_fxn: Callable[[list], list], 
            postprocess_fxn: Callable[[list], list], 
            model_config: dict
        ):
        self.data_loader = DataLoader(data_config)
        self.preprocess = Preprocess(preprocess_fxn=preprocess_fxn)
        self.postprocess = Postprocess(postprocess_fxn=postprocess_fxn)
        self.model = Model(model_config=model_config)

    def run(self):
        self.load_data()
        self.preprocess()
        self.model.train()
        predictions = self.model.predict()
        self.postprocess()


