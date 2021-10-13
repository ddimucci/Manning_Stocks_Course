import yahoo_fin.stock_info as yf
import pandas as pd

def get_keys(methods):
    """
    Retrieves a list of all key fields that can be pulled for a stock symbol

    input: methodlist

    output: list of keys

    """
    titles = []
    while len(methods) > 0:
        j = methods.pop()
        result = eval(j)
        titles.append(result.keys())
    return titles


def generate_methods(yf,symbol):
    """
    Generates commands that can be called on the provided symbol

    input: module name, stock symbol

    output: list of commands 
    """
    methods = dir(yf)
    keep = []
    for i in methods:
        if 'get_' in i and '_get' not in i:
            keep.append( 'yf.'+i+"('"+symbol + "')")
    return keep

assert isinstance(get_keys(["yf.get_analysts_info('pacb')", "yf.get_balance_sheet('pacb')"]),list)
