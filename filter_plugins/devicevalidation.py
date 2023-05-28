import re

def check_nexus_series(input):
    if 'n9k' in input:
        return 'n9k'
    elif 'n7k' in input:
        return 'n7k'
    elif 'n5k' in input:
        return 'n5k'

def ios_check_free_space(input):
    return input['bootflash:']['spacefree_kb']

def find_current_boot(input):
    reg = 'bootflash:(.*.bin)'
    try:
        for x in input:
            out = re.findall(reg, str(x))
            if out:
                return out
    except:
        return 'No boot found'

def delete_images(current_image, upgrade_image, dir_images):    
    match_all = re.findall("\+\d+.\d+\s+(.*.bin)", str(dir_images))
    try:
        match_all.remove(upgrade_image)
    except:
        print ('Unable to remove the upgrade image')
    try:
        match_all.remove(str(current_image).split(":")[1])
    except:
        print ('Unable to remove the current image')    
    return (match_all)

def find_all_images(ios_file, input):
    regez = '(\d+)' # write regex
    data = show_images['stdout_lines'][0]
    for x in data:
        out = re.findall(regez, x)
        data = list(out[0])
        if ios_file in data[7]:
            return 'Image Found'

def check_nexus_md5(md5_supplied, md5_device):
    if md5_supplied == md5_device['sdtout'][0]:
        return 'Passed'
    else:
        return 'Failed'

def check_nxos_current(current_ver, ios_file):
    if current_ver == 'bootflash:///'+ios_file:
        return 'Same'
    else:
        return 'Different'

def check_nexus_install(output, nexus_series):
    if nexus_series == 'n9k':
        data = output['stdout'][0]
        reg = '\s+(\d+)\s+(nxos|bios)\s+(\w.+)\s+(yes|no)'
        out = re.findall(reg, data)
        converted = []
        for x in out:
            con = list(x)
            data = {con[1]:con[3]}
            converted.append(data)
        return converted

class FilterModule(object):
    def filters(self):
        return {
            'check_nexus_series': check_nexus_series,
            'ios_check_free_space':ios_check_free_space,
            'find_current_boot':find_current_boot,
            'delete_images':delete_images,
            'find_all_images':find_all_images,
            'check_nexus_md5':check_nexus_md5,
            'check_nxos_current':check_nxos_current,
            'check_nexus_install':check_nexus_install,
        }
