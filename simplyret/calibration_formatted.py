def calibration_formatted(ant, ret):
    RET_common_list = []
    i = 1
    for line in ant:
        if line.startswith('AntennaUnitGroup'):
            RET_rru_unique = line.split()
            RET = {}
            field_replaceable_unit = RET_rru_unique[4].split(',')[0]
            sector_num = RET_rru_unique[0].split(',')[0]
            RET['number'] = i
            RET['ret_label'] = RET_rru_unique[1]
            if int(sector_num.split('=')[1]) % 3 == 0:
                RET['sector'] = 3
            else:
                RET['sector'] = int(sector_num.split('=')[1]) % 3
            RET['rru'] = field_replaceable_unit.split('=')[1]
            RET['unique_id'] = RET_rru_unique[5].strip()
            RET['tech'] = None
            RET['cur_el_tilt'] = None
            RET['operational_state'] = None
            RET_one_line = list(RET.values())
            RET_common_list.append(RET_one_line)
            i += 1
        else:
            pass
    k = 1
    for line in ret:
        if line.startswith('AntennaUnitGroup'):
            RET_rru = line.split()
            RET = []
            RET.append('RET_' + RET_rru[4])
            RET.append(RET_rru[1])
            RET.append(RET_rru[3])
            for m in range(0, len(RET_common_list)):
                if RET_common_list[m][1] == RET[0]:
                    RET_common_list[m][6] = RET[1]
                    RET_common_list[m][7] = RET[2].strip()
            k += 1   
        else:
            pass
    return RET_common_list
