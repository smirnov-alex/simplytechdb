def format_rru(rru):
    rru_split = rru.split('-')
    sector_num = int(rru_split[1]) % 3
    if sector_num == 0:
        sector_num = 3
        return sector_num
    else:
        return sector_num


def create_RET_dict(uniqueid_list, bs):
    RET_common_list = []
    i = 1
    for uniqueid in uniqueid_list:
        RET = {}
        RET_rru_unique = uniqueid.split(' : ')
        RET['number'] = i
        RET['ret_label'] = bs.upper()
        RET['sector'] = format_rru(RET_rru_unique[0])
        RET['rru'] = RET_rru_unique[0]
        RET['unique_id'] = RET_rru_unique[1].strip()
        # RET['tech'] = None
        # RET['cur_el_tilt'] = None
        # RET['new_el_tilt'] = None
        RET_one_line = list(RET.values())
        RET_common_list.append(RET_one_line)
        i += 1
    return RET_common_list
