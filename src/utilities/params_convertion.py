from .default_params import DefaultParams


def convert_request_params(request: dict, default: DefaultParams):

    output = {}

    for param_name, param_value in request.items():
        converted_value = default[param_name]['type'](param_value)
        output[param_name] = converted_value

    return output
