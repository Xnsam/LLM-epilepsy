from typing import Callable, Union


class DataLoader:
    def __init__(self, data_config: dict):
        """
        A function to load the data from the given config

        :param data_config: configuaration containing the information on the data
        :type data_config: dict

        :return: none
        """
        self.data_config = data_config


class Model:
    def __init__(self, model_config: dict): 
        """
        A function to initialize the model

        :param model_config: a dictionary of details related to models
        :type model_config: dict

        :return: None
        """
        self.model_config = model_config

    def _predict(self):
        """
        A function to model predict

        :return: 
        :rtype: 
        """
        pass

    def _download(self):
        """
        A function to model function

        :return:
        :rtype:
        """
        pass



class Preprocess:
    def __init__(self, preprocess_fxn: Callable[[list], list]):
        """
        An initialization function

        :param preprocess_fxn: function to be used for preprocessing in the pipeline
        :type preprocess_fxn: Callable[[list], list]

        :return: None
        """
        self.preprocess  = preprocess_fxn
    
    def __call__(self, data: list) -> list:
        """
        A function to run the preprocess functions

        :param data: list of data
        :type data: list

        :return: modified data
        :rtype: list
        """
        return self.preprocess(data)


class Postprocess:
    def __init__(self, postprocess_fxn: Callable[[list], list]):
        """
        An initialization function

        :param preprocess_fxn: function to be used for preprocessing in the pipeline
        :type preprocess_fxn: Callable[[list], list]

        :return: None
        """
        self.postprocess  = postprocess_fxn
    
    def __call__(self, data: list) -> list:
        """
        A function to run the postprocess functions

        :param data: list of data
        :type data: list

        :return: modified data
        :rtype: list
        """
        return self.postprocess(data)



class Validation:
    def __init__(self, validation_fxn: Callable[[list], list]): 
        """
        An initialization function for validation class


        :param validation_fxn: function to be used for preprocessing in the pipeline
        :type validation_fxn: Callable[[list], list]

        :return: None
        """
        self.validation = validation_fxn
    
    def __call__(self, prediction: list, ground_truth: list) -> Union[int, float, list]:
        """
        A function to run the validation functions

        :param prediction: list of predicted values
        :type prediction: list
        :param ground_truth: list of ground truth values
        :type ground_truth: list

        :return: calculated validation score
        :rtype: Union[int, float, list]
        """
        return self.validation(prediction, ground_truth)
