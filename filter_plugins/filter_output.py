# from deepdiff import DeepDiff
import re
def filter_sh_cdp_nei_check(input):
    print ('In CDP nei')
    pass

def filter_sh_ip_int_bri(input):
    reg = '(\w+)\s+(\d+.\d+.\d+.\d+)\s+(YES|NO)\s+(\w+)\s+(up|administratively down)\s+(up|down)'
    data = re.findall(reg, str(input))
    processed = []
    for x in data:
        da = list(x)
        res = {
            'interface': da[0],
            'ip':da[1],
            'status':da[4],
            'protocol': da[5],
        }
        processed.append(res)
    return processed

def filter_sh_boot(input):
    reg = 'BOOT variable = (\w.+.bin)'

def output_comparator(pre, post):
    if pre and post:
        dodiff = DeepDiff(pre, post)
        if dodiff:
            try:
                final = []
                data = dodiff['iterable_item_removed']
                for x, y in data.items():
                    final.append(y)
                return final
            except:
                pass
    else:
        return 'Either pre or post data is missing'

def filter_sh_ver(input):
    pass

def filter_sh_int_desc_bri(input):
    regex = '(\w+)\s+(up|admin down)\s+(up|down)'
    data = re.findall(regex, str(input))
    processed = []
    for x in data:
        da = list(x)
        # print (da)
        res = {
            'interface': da[0],
            'status':da[1],
            'protocol': da[2],
        }
        print (res)
        processed.append(res)
    return processed

def filter_nxos_sh_int_status(output):
    data = output['stdout_lines'][0]
    if type(data) == dict:
        output = data['TABLE_interface']['ROW_interface']
        if type(output) == list:
            return [{'inteface': x['interface'], 'state': x['state']} for x in output]
        else:
            return [{'interface': output['interface'], 'state': output['state']}]
    elif type(data) == list:
        return ''

def extractBin(data):
    all_boot = []
    loop = 1
    for x in data:
        if '.bin' in x:
            all_boot.append({loop:x.strip()})
            loop= loop+1
        else:
            pass
    print(all_boot)
    return all_boot[0][1]
            
def find_cisco_ios_sh_boot(input):

    try:
        for x in input:
            n = x.replace(';', ',').replace('=', ',')
            output = n.split(',')
            if output:
                return extractBin(output)
            else:
                return None
    except:
        return None

def find_uploaded_images(all_bin_files):  
    images =[] 
    for x in all_bin_files:
        try:
            out =  re.findall("\+\d+.\d+\s+(.*.bin)", str(x))
            images.append(out[0])
        except:
            return None
    print('in find_uploaded_images')
    print(images)
    return images


class FilterModule(object):
    def filters(self):
        return {
            'output_comparator':output_comparator,
            'filter_sh_cdp_nei_check': filter_sh_cdp_nei_check,
            'filter_sh_ip_int_bri':filter_sh_ip_int_bri,
            'filter_sh_boot':filter_sh_boot,
            'filter_sh_ver': filter_sh_ver,
            'filter_sh_int_desc_bri':filter_sh_int_desc_bri,
            'find_cisco_ios_sh_boot': find_cisco_ios_sh_boot,
            'find_uploaded_images':find_uploaded_images,

        }