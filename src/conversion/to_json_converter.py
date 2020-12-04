import csv
import json
import xmltodict
import os


def xml_file_to_json(xml_file_path):
    """
        Takes an xml file path, reads file and converts to json format
    """
    with open(xml_file_path, 'r') as xml_file:
        xml_json = xmltodict.parse(xml_file.read())

    return json.dumps(xml_json)


def csv_file_to_json(csv_file_path):
    """
        Takes a csv file path, reads file and converts to json format
    """
    pass
