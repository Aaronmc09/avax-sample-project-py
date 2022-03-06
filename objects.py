from typing import List, Dict


ATTRIBUTE_KEY_TRANSLATIONS: Dict[str, str] = {
    '01-Background': 'background',
    '02-Xbgitem': 'x_bg_item',
    '03-Head': 'head',
    '04-Shirts': 'shirts',
    '05-Jacket': 'jacket',
    '06-Hair': 'hair',
    '07-Facial': 'facial',
    '08-Glasses': 'glasses',
    '09-Extensions': 'extensions',
    '10-Frame': 'frame'
}


class Attribute(object):
    # List of expected keys from metadata attributes
    background: str = 'None'
    x_bg_item: str = 'None'
    head: str = 'None'
    shirts: str = 'None'
    jacket: str = 'None'
    hair: str = 'None'
    facial: str = 'None'
    glasses: str = 'None'
    extensions: str = 'None'
    frame: str = 'None'

    def __init__(self, attributes: List[Dict[str, str]], parent: object = None):
        expected_keys = ATTRIBUTE_KEY_TRANSLATIONS.keys()

        for attribute in attributes:
            # Check if incoming key is within the list of expected keys
            if attribute['trait_type'] in expected_keys:
                translated_key = ATTRIBUTE_KEY_TRANSLATIONS[attribute['trait_type']]
                self.__setattr__(translated_key, attribute['value'])

            else:
                # Raise error if an unexpected key is present from attribute
                raise AttributeError(f'{self} object does not have {attribute["trait_type"]} attribute.')

    def __iter__(self):
        # To be used by python dict() method
        # Will return dictionary with translated keys instead of object keys
        """
        instead of: {'background': 'Common-waves-1', 'x_bg_item: Epic-avax', ...}
        return:     {'01-Background': 'Common-waves-1', '02-Xbgitem: Epic-avax', ...}
        """

        for key in ATTRIBUTE_KEY_TRANSLATIONS.keys():
            translated_key = ATTRIBUTE_KEY_TRANSLATIONS[key]
            yield key, self.__getattribute__(translated_key)

    def __str__(self):
        return 'Attribute'


class AvaxEl33t(object):
    # List of expected keys from metadata
    name: str = ''
    description: str = ''
    fee_recipient: str = ''
    seller_fee_basis_points: str = ''
    image: str = ''
    external_url: str = ''
    attributes: List[dict] = []
    hash: str = ''

    def __init__(self, **kwargs):

        for key in kwargs.keys():
            # Check if incoming key is within the list of expected keys
            if hasattr(self, key):
                self.__setattr__(key, kwargs.get(key))

            else:
                # Raise error if an unexpected key is present from metadata
                raise AttributeError(f'{self} object does not have {key} attribute.')

    def __str__(self):
        return f'Name: {self.name} Hash: {self.hash}.'

    def clean_attributes(self):
        nft_attr = Attribute(self.attributes)

        return dict(nft_attr)
