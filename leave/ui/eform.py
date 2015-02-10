__author__ = 'sky_wu'
__version__= '0.1'

import base64
import uuid

# get a UUID - URL safe, Base64
def get_a_uuid():
    return str(uuid.uuid4())
    #r_uuid = base64.urlsafe_b64encode(uuid.uuid4().bytes)
    #return r_uuid.replace('=', '')

class eForm:
    """ eform definition
        * eform has status definition
        * eform has attributes definition
    """
    def __init__(self, fid, attr):
        self.form_id = fid
        self.attribute_definition = attr

def get_instance_id(form_id):
    """
    :param form_id:
    :return: instance id according to the form id
    """
    return (uuid.UUID())

class eFormInstance:
    """ instance of eForm
        * default status
        *
    """
    def __init__(self, form_id):
        self.form_instance_id = get_instance_id(form_id)



