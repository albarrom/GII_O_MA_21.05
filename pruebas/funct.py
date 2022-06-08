

from charset_normalizer import CharsetNormalizerMatches as CnM
import pandas as pd
import os
from re import search

from pandas.errors import EmptyDataError




def existe(directorio):
    """
    funcion que comprueba si directorio existe
    :param directorio: directorio del archivo que se quiere comprobar
    :return: True si existe, False si no.
    """
    try:
        if os.path.isfile(directorio): return True
        else: return False
    except BaseException:
        return False


def vacio (directorio):
    """
    Funcion que comprueba si directorio esta vacio.
    :param directorio: directorio del archivo que se quiere comprobar
    :return: True si existe, False si no.
    """
    try:
        if os.stat(directorio).st_size==0: return True
        else: return False
    except BaseException:
        return False


def encoding_csv(directorio):
    """
    Funcion que devuelve el tipo de encoding de directorio
    :param directorio: directorio del archivo que se quiere comprobar
    :return:
    """
    try:
        return CnM.from_path(directorio).best().first().encoding
    except BaseException as e:
        return str(e)

def extension(directorio):
    """
    Funcion que devuelve los ultimos 4 caracteres de directorio
    :param directorio: directorio del archivo que se quiere comprobar
    :return: ultimos 4 caracteres del archivo
    """
    return directorio[-4:]


def funcion_pandas(directorio):
    """
    Funcion que devuelve las columnas de directorio
    :param directorio: directorio del archivo que se quiere comprobar
    :return: columnas del dataframe o un mensaje de error
    """
    try:
        posible_fichero_ok= pd.read_csv(directorio)
        return posible_fichero_ok.columns
    except BaseException as error:
        return str(error)


def columnas_no_nulas(directorio, pred):

    try:
        f = pd.read_csv(directorio)
        # si pred es subset de las columnas y ninguna de esas columnas es nula
        if set(pred).issubset(f.columns) and f[pred].notna().any().all():
            return True
        else:
            return False
    except BaseException as error:
        return False













