import io
import json

from frames.utils import *


frames = io.open('data/frames.json', 'r').read()
frames = json.loads(frames)


def display_conversation(conversation):
    for turn in conversation['turns']:
        labels = turn['labels']
        for i in Act2JSONStr().transform(labels['acts']):
            print(f'{i} ({labels["active_frame"]})')
        print('\n')


def display_text(conv_id, turn):
    return frames[conv_id]['turns'][turn]['text']
