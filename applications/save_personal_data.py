#!/usr/bin/python
# Copyright (c) 2018 Warren Usui, MIT License
"""
Save personal data
"""
import os
import sys
import codecs
from json import dumps
from llama_slobber import get_season
from llama_slobber import act_on_all_rundles
from llama_slobber import get_rundle_personal

def personal_by_rundle(season, rundle, payload):
    """
    Create json file of personal information for this rundle.

    Input:
        season -- season number
        rundle -- rundle name
        payload -- dictionary where 'output_directory' entry contains the
                   name of the directory where data will be stored
    """
    outstr = dumps(get_rundle_personal(season, rundle), indent=4)
    outdir = payload['output_directory']
    fname = "%s%s%s.json" % (outdir, os.sep, rundle)
    with open(fname, "w") as ofile:
        ofile.write(outstr)


def personal_dict(season, rundle, payload):
    """
    Add to large payload dictionary.

    Input:
        season -- season number
        rundle -- rundle name
        payload -- dictionary where results will be stored
    """
    data = get_rundle_personal(season, rundle)
    payload.update(data)


def save_personal_data(out_dir):
    """
    Save personal data

    Input:
        out_dir -- directory where results will be stored.

    First store all the personal data into json files named by the rundle.
    Then store all the personal data into one big json file.
    """
    sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
    season = get_season()
    act_on_all_rundles(season, personal_by_rundle,
                       {'output_directory': out_dir})
    payload = {}
    act_on_all_rundles(season, personal_dict, payload)
    outstr = dumps(payload, indent=4)
    fname = '%s%severybody.json' % (out_dir, os.sep)
    with open(fname, "w") as ofile:
        ofile.write(outstr)


if __name__ == "__main__":
    save_personal_data("personal")
