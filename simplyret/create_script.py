from .bb_or_dus import bb_or_dus


def return_6x(bs):
    with open('BS_6x.txt', 'r') as f:
        for line in f:
            if line.startswith(bs.upper()):
                x = line.split()
                bs_name_6x = x[1]
                return bs_name_6x
            else:
                pass
    

def create_script_mos(bs, RET_list):
    dig_unit = bb_or_dus(bs)
    bs_name = bs[:6]
    bs_region = bs[:2]
    num_bs_name = int(bs[2:6])    
    technology_dict = {'GSM900': '', 'GSM1800': '', 'UMTS2100': '_', 'UMTS2100(6x)': '_', 'LTE800': '_08',
                       'LTE1800': '_01', 'LTE1800(2)': '_01', 'LTE2600': '_02', 'LTE2300': '_03', 'LTE2300(2)': '_03',
                       'LTE2100': '_05', 'LTE2100(6x)': '_15', 'LTE2600(2)': '_02', 'UMTS2100 (RR4xxx)': '_',
                       'UMTS2100 (RR5xxx)': '_', }
    # проверка наличия пустых строк
    counter = 0
    for item in RET_list:        
        if item[6] == 'Not Used' or item[5] == "Not Used":
            pass
        else:
            counter += 1        
    if counter == 0:
        return 'FAIL'        
    out_file = open(bs.upper() + '_Add_RET.mos', 'w')
    out_file.write('lt all\ngs+\nconfbl+\n')
    for line in RET_list:
        if line[6] == 'Not Used' or line[5] == 'Not Used':
            pass
        else:
            if line[5] == 'GSM1800':
                bs_name_file = bs[:6].upper()
                sector_name = int(line[2]) + 3              
                tech_sector_name = technology_dict.get(line[5])
                AntennaNearUnit = 'RET_' + bs_name_file + tech_sector_name + str(sector_name)   
            elif line[5] == 'UMTS2100':
                sector_name = line[2]
                bs_name_file = bs_region + str(num_bs_name + 3000)
                tech_sector_name = technology_dict.get(line[5])
                AntennaNearUnit = 'RET_' + bs_name_file + tech_sector_name + str(sector_name)
            elif line[5] == 'UMTS2100 (RR4xxx)':
                sector_name = line[2]
                bs_name_file = bs_region + str(num_bs_name + 4000)
                tech_sector_name = technology_dict.get(line[5])
                AntennaNearUnit = 'RET_' + bs_name_file + tech_sector_name + str(sector_name)
            elif line[5] == 'UMTS2100 (RR5xxx)':
                sector_name = line[2]
                bs_name_file = bs_region + str(num_bs_name + 5000)
                tech_sector_name = technology_dict.get(line[5])
                AntennaNearUnit = 'RET_' + bs_name_file + tech_sector_name + str(sector_name)
            elif line[5] == 'LTE1800(2)' or line[5] == 'LTE2600(2)' or line[5] == 'LTE2300(2)':
                sector_name = line[2]   
                bs_name_file = bs[:6].upper()           
                tech_sector_name = technology_dict.get(line[5])
                AntennaNearUnit = 'RET_' + bs_name_file + tech_sector_name + str(sector_name) + '_2'
            elif line[5] == 'UMTS2100(6x)':
                sector_name = line[2]   
                bs_name_file = return_6x(bs_name)          
                tech_sector_name = technology_dict.get(line[5])
                AntennaNearUnit = 'RET_' + str(bs_name_file) + tech_sector_name + str(sector_name) 
            else:
                bs_name_file = bs[:6].upper()
                tech_sector_name = technology_dict.get(line[5])
                sector_name = line[2]
                AntennaNearUnit = 'RET_' + bs_name_file + tech_sector_name + str(sector_name)
            number, base_station, sector, rru, unique_id, technology, el_tilt = line
            user_label = AntennaNearUnit[4:]
            if dig_unit == 'Baseband':
                output1 = '''
#{0}
CRE Equipment=1,AntennaUnitGroup={5},AntennaNearUnit={0}
SET Equipment=1,AntennaUnitGroup={5},AntennaNearUnit={0} administrativeState UNLOCKED

CRE Equipment=1,AntennaUnitGroup={5},AntennaNearUnit={0},RetSubUnit=1

CRE Equipment=1,AntennaUnitGroup={5},AntennaUnit=1,AntennaSubunit={0}
SET Equipment=1,AntennaUnitGroup={5},AntennaUnit=1,AntennaSubunit={0} azimuthHalfPowerBeamwidth 65

SET Equipment=1,AntennaUnitGroup={5},AntennaNearUnit={0} uniqueId {1}

SET Equipment=1,AntennaUnitGroup={5},AntennaNearUnit={0} rfPortRef Equipment=1,FieldReplaceableUnit={2},RfPort=R

SET Equipment=1,AntennaUnitGroup={5},AntennaNearUnit={0},RetSubUnit=1 userLabel {4}

SET Equipment=1,AntennaUnitGroup={5},AntennaUnit=1,AntennaSubunit={0} retSubunitRef Equipment=1,AntennaUnitGroup={5},
AntennaNearUnit={0},RetSubUnit=1
SET Equipment=1,AntennaUnitGroup={5},AntennaNearUnit={0},RetSubUnit=1 electricalAntennaTilt {3}
\n
'''
            elif dig_unit == 'DUS':
                output1 = '''
#{0}
CRE Equipment=1,AntennaUnitGroup={5},AntennaNearUnit={0}
SET Equipment=1,AntennaUnitGroup={5},AntennaNearUnit={0} administrativeState UNLOCKED

CRE Equipment=1,AntennaUnitGroup={5},AntennaNearUnit={0},RetSubUnit=1

CRE Equipment=1,AntennaUnitGroup={5},AntennaUnit=1,AntennaSubunit={0}
SET Equipment=1,AntennaUnitGroup={5},AntennaUnit=1,AntennaSubunit={0} azimuthHalfPowerBeamwidth 65

SET Equipment=1,AntennaUnitGroup={5},AntennaNearUnit={0} uniqueId {1}

SET Equipment=1,AntennaUnitGroup={5},AntennaNearUnit={0} rfPortRef Equipment=1,AuxPlugInUnit={2},DeviceGroup=ru,RfPort=R

SET Equipment=1,AntennaUnitGroup={5},AntennaNearUnit={0},RetSubUnit=1 userLabel {4}

SET Equipment=1,AntennaUnitGroup={5},AntennaUnit=1,AntennaSubunit={0} retSubunitRef Equipment=1,AntennaUnitGroup={5},
AntennaNearUnit={0},RetSubUnit=1
SET Equipment=1,AntennaUnitGroup={5},AntennaNearUnit={0},RetSubUnit=1 electricalAntennaTilt {3}
\n
'''
            else:
                output1 = 'ERROR'
            out_file.write(output1.format(AntennaNearUnit, unique_id, rru, el_tilt, user_label, sector))
    out_file.write('cvms Add_RET\ngs-\nconfbl-\n')
    out_file.close()
    return 'SUCCESS'
