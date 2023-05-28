def device_model(net_model):
    IOS_MODELS = ['csr1000v']    
    NEXUS_MODELS = ['n5k-c5596up', 'n9k-c93180lc-ex']

    if net_model in IOS_MODELS:
        device_model = 'ios'
    elif net_model in NEXUS_MODELS:
        device_model = 'nexus'
    return device_model

class FilterModule(object):
    def filters(self):
        return {
            'device_model': device_model,
        }