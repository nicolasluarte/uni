from configparser import ConfigParser

config = ConfigParser()

config['preprocess'] = {
        # work donde in filtering d=5 for real time
        'filter_size': '3',
        # should be the same
        # < 10 not much effect
        # > 150 strong effect image look "cartoonish"
        'sigma_color': '150',
        'sigma_space': '150'
        }

config['postprocess'] = {
        'kernelx': '5',
        'kernely': '5',
        }

with open('config.conf', 'w') as f:
    config.write(f)
