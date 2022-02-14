from flask import Blueprint, request, abort
from ..utilities.default_params import DefaultParams
from ..utilities.params_validation import check_parameters
from ..utilities.params_convertion import convert_request_params
from random import randint


end_point = Blueprint('uniform_random_integer', __name__)

# Response model
output_model = {
    'numbers': [],
    'distribution': 'uniform',
    'range_width': None,
    'sample_size': None,
    'status': None,
    'error_msg': [],
    'request_url': ''
}

# Route for uniform random integers number


@end_point.route('/uniform_random_integer')
def uniform_random_integer():

    # Create the default input parameters
    default_params = DefaultParams()
    default_params.create_param('range_width', int, 10)
    default_params.create_param('sample_size', int, 1)

    # Create a copy of the output response model
    output = output_model.copy()

    # Check if there are any request arguments
    if request.args:
        # Check if the parameters are correct
        validate_params = check_parameters(request.args, default_params)
        if validate_params['status'] != None:
            output.update(validate_params)
            return output

    # Convert params value to the correct form
    converted_params = convert_request_params(request.args, default_params)
    if converted_params:
        output.update(converted_params)
    else:
        output['range_width'] = default_params['range_width']['value']
        output['sample_size'] = default_params['sample_size']['value']

    print(output)
    
    output['status'] = 200
    output['request_url'] = request.url
    output['numbers'] = [
        randint(0, output['range_width']) for _ in range(output['sample_size'])]

    return output
