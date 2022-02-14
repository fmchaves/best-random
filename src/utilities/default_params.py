from typing import Union


class DefaultParams:

    params = {}

    def create_param(self, param_name: str, param_type: type, param_value: Union[int, float, complex, bool, list, tuple, dict]):
        """This method will create key-value pairs in the class variable params.

        Args:
            param_name (str): parameter name
            param_type (type): parameter type
            param_value (Union[int, float, complex, bool, list, tuple, dict]): parameter value

        Returns:
            None
        """
        self.params[param_name] = {'type': param_type, 'value': param_value}

    def __getitem__(self, name: str) -> dict:
        return self.params.get(name)

    def get(self, name: str) -> dict:
        return self.__getitem__(name)

    def delete_param(self, param_name: str) -> dict:
        if deleted := self.params.get(param_name) != None:
            del self.params[param_name]
        return deleted

    def keys(self) -> list:
        return self.params.keys()

    def __str__(self) -> str:
        return str(self.params)
