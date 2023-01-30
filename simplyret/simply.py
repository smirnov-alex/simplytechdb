import paramiko
import time
import re
import os
from os.path import exists
from .rets_perem import create_RET_dict
from .calibration_formatted import calibration_formatted
from .bb_or_dus import bb_or_dus, get_enodeb

SERVERS = {
    'ENM6': '10.12.72.28',
    'ENM7': '10.12.110.28',
    'ENM8': '10.12.112.28',
    'ENM9': '10.12.114.28',
    'ENM10': '10.12.116.28',
    'ENM11': '10.12.118.28',
    'ENM12': '10.12.120.28',
    'ENM14': '10.12.240.28',
    'ENM15': '10.12.246.28',
}

SERVERS_NAMES = [key for key in SERVERS.keys()]
CWD = os.getcwd()


# Сделать выгрузку RET
def upload_unique_id_BS(bs, login, password, server):
    bs = bs
    login = login
    password = password
    server = server
    ip_server = SERVERS.get(server, 'Empty')
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname=ip_server, username=login, password=password, port=22, look_for_keys=False,
                       allow_agent=False)
        sftp = client.open_sftp()
        list_of_folders_main = sftp.listdir(f'/home/shared/{login}/')
        if 'RET' not in list_of_folders_main:
            sftp.mkdir(f'/home/shared/{login}/RET')
            sftp.close()
        else:
            sftp.close()
    except paramiko.AuthenticationException:
        return 'No_auth'
    dig_unit = bb_or_dus(bs)
    if dig_unit == 'DUS':
        enodeb = get_enodeb(bs)
        filename_full = f'SubNetwork=ONRM_ROOT_MO,SubNetwork=eNodeB_{enodeb},MeContext={bs.upper()}' \
                        f',ManagedElement=1,NodeManagementFunction=1,EquipmentDiscovery=1_DeviceScanResult.xml'
    else:
        filename_full = f'ManagedElement={bs.upper()},NodeSupport=1,EquipmentDiscovery=1_DeviceScanResult.xml'
    command = f'amos -v username=rbs,password=RBSEricsson12# {bs.upper()} \n'
    long_pathname = f'/home/shared/{login}/RET'
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname=ip_server, username=login, password=password, port=22, look_for_keys=False,
                       allow_agent=False)
        sftp = client.open_sftp()
        list_of_files = sftp.listdir(long_pathname)
        if filename_full in list_of_files:
            sftp.remove(f'{long_pathname}/{filename_full}')
        with client.invoke_shell() as ssh:
            time.sleep(5)
            ssh.send(command)
            time.sleep(10)
            connection = ssh.recv(5000).decode('utf-8')
            if 'Checking ip contact...Not OK' in connection:
                return 'No_connection'
            else:
                ssh.send('lt all\n')
                time.sleep(20)
                ssh.send('confbl+\n')
                time.sleep(1)
                ssh.send('set EquipmentDiscovery=1 portConfiguration 0\n')
                time.sleep(1)
                ssh.send('set EquipmentDiscovery=1 portVoltage 1\n')
                time.sleep(1)
                ssh.send(f'set EquipmentDiscovery=1 sftpServerIpAddress {ip_server} \n')
                time.sleep(1)
                ssh.send(f'set EquipmentDiscovery=1 sftpServerPath {long_pathname} \n')
                time.sleep(1)
                ssh.send(f'set EquipmentDiscovery=1 sftpUsername {login} \n')
                time.sleep(1)
                ssh.send(f'set EquipmentDiscovery=1 sftpPassword {password} \n')
                time.sleep(1)
                ssh.send('confbl-\n')
                time.sleep(1)
                ssh.send('acc EquipmentDiscovery=1 performFullAntennaDeviceScan\n')
                time.sleep(3)
                ssh.send('y\n')
                time.sleep(1)
                flag_scaner = True
                while flag_scaner:
                    ssh.send('get EquipmentDiscovery=1\n')
                    check_state = ssh.recv(5000).decode('utf-8')
                    if '2 (SCAN_FINISHED)' in check_state:
                        flag_scaner = False
                    elif '(SCAN_FAILED)' in check_state:
                        flag_scaner = False
                    time.sleep(20)
                ssh.send('q\n')
                time.sleep(3)
            sftp = client.open_sftp()
            list_of_files = sftp.listdir(long_pathname)
            if filename_full in list_of_files:
                sftp.get(f'{long_pathname}/{filename_full}', f'{CWD}//{filename_full}')
            sftp.close()
        RET_list = check_uniqueid(bs.upper())
        if len(RET_list) == 0:
            return 'Empty_file'
        return RET_list
    except paramiko.AuthenticationException:
        return 'No_auth'


def check_uniqueid(bs):
    eq_discovery_bb = exists(f'ManagedElement={bs.upper()},NodeSupport=1,EquipmentDiscovery=1_DeviceScanResult.xml')
    enodeb = get_enodeb(bs)
    eq_discovery_dus = exists(f'SubNetwork=ONRM_ROOT_MO,SubNetwork=eNodeB_{enodeb},MeContext={bs.upper()},'
                              f'ManagedElement=1,NodeManagementFunction=1,EquipmentDiscovery=1_DeviceScanResult.xml')
    uniqueID_list = []
    if eq_discovery_bb:
        filename_bb = f'ManagedElement={bs.upper()},NodeSupport=1,EquipmentDiscovery=1_DeviceScanResult.xml'
        if os.stat(filename_bb).st_size == 0:
            return 'Empty_file'
        f = open(filename_bb)
        for line in f:
            rru_regex = re.compile('RRU-(\d+)-\d')
            unique_regex = re.compile('(unique_id=)"(\S+)"')
            mo_rru = rru_regex.search(line)
            mo_unique = unique_regex.search(line)
            if mo_rru is not None:
                x1 = mo_rru.group() + ' : '
            elif mo_unique is not None:
                x2 = mo_unique.group(2)
                uniqueID_list.append(x1 + x2)
            else:
                pass
        f.close()
    elif eq_discovery_dus:
        filename_dus = f'SubNetwork=ONRM_ROOT_MO,SubNetwork=eNodeB_{enodeb},MeContext={bs.upper()},' \
                       f'ManagedElement=1,NodeManagementFunction=1,EquipmentDiscovery=1_DeviceScanResult.xml'
        if os.stat(filename_dus).st_size == 0:
            return 'Empty_file'
        f = open(filename_dus)
        for line in f:
            rru_regex = re.compile('RRU-(\d+)-\d')
            unique_regex = re.compile('(unique_id=)"(\S+)"')
            mo_rru = rru_regex.search(line)
            mo_unique = unique_regex.search(line)
            if mo_rru is not None:
                x1 = mo_rru.group() + ' : '
            elif mo_unique is not None:
                x2 = mo_unique.group(2) + '\n'
                uniqueID_list.append(x1 + x2)
            else:
                pass
        f.close()
    else:
        return 'Nothing'
    RET_inserted_list = create_RET_dict(uniqueID_list, bs)
    return RET_inserted_list


# проверить калибровку RET
def check_calibration_BS(bs, login, password, server):
    bs = bs
    login = login
    password = password
    server = server
    ip_server = SERVERS.get(server, 'Empty')
    AntNearUnit, RetNearUnit = connection_for_checking(bs, login, password, ip_server)
    if AntNearUnit == 'No_connection' and RetNearUnit == 'No_connection':
        return 'No_connection'
    elif AntNearUnit == 'No_auth' and RetNearUnit == 'No_auth':
        return 'No_auth'
    RET_inserted_list = calibration_formatted(AntNearUnit.strip().split('\n'), RetNearUnit.strip().split('\n'))
    if not RET_inserted_list:
        return 'No_rets'
    return RET_inserted_list


def connection_for_checking(bs, login, password, ip_server):
    command0 = f'amos -v username=rbs,password=RBSEricsson12# {bs.upper()}' + '\n'
    command1 = 'hget AntennaNearUnit antennaNearUnitId|operationalState|^uniqueId|rfPortRef' + '\n'
    command2 = 'hget RetSubUnit= electricalAntennaTilt|operationalState|userLabel' + '\n'
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname=ip_server, username=login, password=password,
                       port=22, look_for_keys=False, allow_agent=False)
        with client.invoke_shell() as ssh:
            time.sleep(5)
            ssh.send(command0)
            time.sleep(10)
            connection = ssh.recv(5000).decode('utf-8')
            if 'Checking ip contact...Not OK' in connection:
                return 'No_connection', 'No_connection'
            else:
                ssh.send('lt all\n')
                time.sleep(20)
                ssh.recv(5000)
                ssh.send(command1)
                time.sleep(10)
                AntNearUnit = ssh.recv(10000).decode('utf-8')
                ssh.send(command2)
                time.sleep(10)
                RetNearUnit = ssh.recv(10000).decode('utf-8')
                ssh.send('q\n')
                time.sleep(3)
                return AntNearUnit, RetNearUnit
    except paramiko.AuthenticationException:
        return 'No_auth', 'No_auth'


# прописать RET на БС
def set_ret_on_BS(bs, login, password, server):
    bs = bs
    login = login
    password = password
    server = server
    add_ret_mos = exists(f'{bs.upper()}_Add_RET.mos')
    if not add_ret_mos:
        result = f'Скрипт для {bs.upper()} не найден!'
        return result
    else:
        ip_server = SERVERS.get(server, 'Empty')
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            client.connect(hostname=ip_server, username=login, password=password, port=22,
                           look_for_keys=False, allow_agent=False)
            sftp = client.open_sftp()
            sftp.put(f'{bs.upper()}_Add_RET.mos',
                     f'/home/shared/{login}/RET/{bs.upper()}_Add_RET.mos')
            sftp.close()
            command = f'amos -v username=rbs,password=RBSEricsson12# {bs.upper()}\n'
            run_command = f'run /home/shared/{login}/RET/{bs.upper()}_Add_RET.mos\n'
            client2 = paramiko.SSHClient()
            client2.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client2.connect(hostname=ip_server, username=login, password=password, port=22,
                            look_for_keys=False, allow_agent=False)
            with client2.invoke_shell() as ssh:
                ssh.send(command)
                time.sleep(5)
                connection = ssh.recv(5000).decode('utf-8')
                if 'Checking ip contact...Not OK' in connection:
                    return f'Сетевой элемент {bs.upper()} недоступен или не существует!'
                ssh.send(run_command)
                time.sleep(120)
                ssh.send('q\n')
                time.sleep(3)
            return f'Прописка RET на {bs.upper()} завершена!'
        except paramiko.AuthenticationException:
            return 'Нет подключения! Проверьте имя/пароль пользователя ENM!'
