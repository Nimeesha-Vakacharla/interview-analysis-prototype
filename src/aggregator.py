import numpy as np

def aggregate_emotions(emotions_list):
    if not emotions_list:
        return {}

    totals = {}

    for emo in emotions_list:
        for k, v in emo.items():
            totals[k] = totals.get(k, 0) + v

    avg = {k: float(v / len(emotions_list)) for k, v in totals.items()}

    return avg