from flask import Blueprint, request
from ..utilities.default_params import DefaultParams
from ..utilities.params_validation import check_parameters
from ..utilities.params_convertion import convert_request_params
from random import randint


end_point = Blueprint('uniform_random_custom', __name__)

# Response model
output_model = {
    'numbers': [],
    'distribution': 'uniform',
    'custom_list': [],
    'sample_size': None,
    'status': None,
    'error_msg': [],
    'request_url': ''
}


# Route for uniform random custom
@end_point.route('/uniform_random_custom', methods=['POST'])
def uniform_random_number():

    # Create the default input parameters
    default_params = DefaultParams()
    default_params.create_param('custom_list', list, list(range(1, 11)))
    default_params.create_param('sample_size', int, 5)

    # Create a copy of the output response model
    output = output_model.copy()

    # Check if there are any request arguments
    if request.get_json():
        # Check if the parameters are correct
        validate_params = check_parameters(request.get_json(), default_params)
        if validate_params['status'] != None:
            output.update(validate_params)
            return output

    # Convert params value to the correct form
    converted_params = convert_request_params(
        request.get_json(), default_params)
    output.update(converted_params)
    output['status'] = 200
    output['request_url'] = request.url
    indexes = [randint(0, len(output['custom_list']) - 1)
               for _ in range(output['sample_size'])]
    output['numbers'] = [output['custom_list'][index] for index in indexes]

    return output
