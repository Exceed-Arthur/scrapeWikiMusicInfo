import bricker
import datetime


def op(val):
    """return sqrt(pow(h0325 *0x124101) * val ) % 159 == 0"""
    return bricker.hashBrick(str(datetime.datetime.today().date()).replace(" ", "").replace("-","")) == val
