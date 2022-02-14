from .default_params import DefaultParams


def check_url_params(request_params: list[str], default_params: list[str]) -> list:
    """This function will check if the request valiables name are correct.

    Args:
        request_params (list[str]): list containing the request variables name
        default_params (list[str]): list containing the default variables name

    Returns:
        list: list containing the errors
    """

    output = []
    for param_name in request_params:
      # Check if the request param name is in default parameters
      # if not success, append an error to the output
        if param_name not in default_params:
            output.append(f'Incorrect parameter: {param_name}')
    return output


def check_type_params(request_params: dict, default_params: dict) -> list:
    """This function will check if the type of the request variables are correct.

    Args:
        request_params (dict): dictionary containing the request parameters
        default_params (dict): dictionary containing the default parameters

    Returns:
        list: list containing the errors
    """

    output = []
    for param_name in request_params.keys():
        # This block try to convert the request variable into default type
        # if not success, append an error to the output
        try:
            variable_type = default_params.get(param_name)['type']
            variable_converted = variable_type(request_params[param_name])
            default_params.get(param_name)['value'] = variable_converted
        except:
            output.append(
                f'Incorrect value type of {param_name} parameter - expected ({default_params.get(param_name)["type"]})')
    return output


def check_parameters(request_params: dict, default_params: DefaultParams) -> dict:
    """This function will check if the name and value of request is in the correct form

    Args:
        request_params (dict): dictionary containing the request
        default_params (DefaultParams): object of DefaultParams class

    Returns:
        dict: dictionary containing the status code and the errors
    """

    output = {'status': None, 'error_msg': []}

    # Check request parameters name
    param_name_errors = check_url_params(
        request_params.keys(), default_params.keys())

    # If any errors with parameters name, return the output
    if param_name_errors:
        output['status'] = 400
        output['error_msg'] = param_name_errors
        return output

    # Check parameters type
    param_type_errors = check_type_params(request_params, default_params)

    # If any errors with parameters type, return the output
    if param_type_errors:
        output['status'] = 400
        output['error_msg'] = param_type_errors
        return output

    return output
