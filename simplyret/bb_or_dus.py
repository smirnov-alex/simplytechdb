import re


def bb_or_dus(bs):
    network_element = bs.upper()
    bb6620_regex = re.compile('\w{2}\d{4}-BL$')
    bb6620G_regex = re.compile('\w{2}\d{4}-BG$')
    bb6630_regex = re.compile('\w{2}\d{4}-B$')
    dus_regex = re.compile('\w{2}\d{4}-L$')
    mo_bb6620 = bb6620_regex.search(network_element)
    mo_bb6620G = bb6620G_regex.search(network_element)
    mo_bb6630 = bb6630_regex.search(network_element)
    mo_dus = dus_regex.search(network_element)
    if mo_bb6630 is not None:
        digital_unit = 'Baseband'
    elif mo_bb6620G is not None:
        digital_unit = 'Baseband'
    elif mo_bb6620 is not None:
        digital_unit = 'Baseband'
    elif mo_dus is not None:
        digital_unit = 'DUS'
    else:
        digital_unit = 'Unknown'
    return digital_unit


def get_enodeb(bs):
    bs_region = bs[:2]
    enodeb_dict = {
        'AA': 'AAA',
        'BB': 'BBB',
        'CC': 'CCC',
        'DD': 'DDD',
        'EE': 'EEE',
        'FF': 'FFF',
        'GG': 'GGG',
        'HH': 'HHH',
        'JJ': 'JJJ',
        'KK': 'KKK',
        'LL': 'LLL',
        'MM': 'MMM',
    }
    return enodeb_dict[bs_region.upper()]
