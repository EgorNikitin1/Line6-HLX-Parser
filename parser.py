import json
import re
from pprint import pprint
import pandas as pd


def check_strings(target, _string):
    target_words = target.split()
    regex_pattern = ''.join(f'(?=.*{word})' for word in target_words)

    if re.search(regex_pattern, _string):
        return True
    else:
        return False


EQUIPMENT_LIST = ['Amp', 'Delay', 'Distortion', 'Dynamics', 'EQ', 'Filter', 'Modulation', 'Pitch-Synth', 'Reverb', 'Volume-Pan', 'Wah']
EQUIPMENT = {}
for model in EQUIPMENT_LIST:
    path = 'Equipment/' + model + '.csv'
    EQUIPMENT[model] = pd.read_csv(path, encoding='utf-8', sep=';')

path = "Presets/"
file_name = 'Discipline.hlx'  # choose file to parse
with open(path + file_name) as file:
    data = json.load(file)
    file.close()

regex_block = r'block\d'
blocks = {}
for key, value in data['data']['tone']['dsp0'].items():
    if re.search(regex_block, key):
        blocks[key] = value

pprint(blocks)

regex_snapshot = r'snapshot\d'
snapshots = {}
for key, value in data['data']['tone'].items():
    if re.search(regex_snapshot, key):
        snapshots[key] = value
        snapshots[key]['@blocks'] = value['blocks']['dsp0']
        del snapshots[key]['blocks']
        del snapshots[key]['@ledcolor']
        del snapshots[key]['@pedalstate']
        del snapshots[key]['@tempo']
        del snapshots[key]['@valid']

pprint(snapshots)
