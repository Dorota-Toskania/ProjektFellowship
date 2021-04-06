
def wog(zob_ogol: float, aktywa_ogol: float) -> float:

    """
      Wskaźnik ogólnego zadłużenia (ang. debt ratio)

      Parameters
      ----------
      zob_ogol:float
          Zobowiązania ogółem (ang. Total debt)
      aktywa_ogol:float
          Aktywa ogółem (ang. Total assets)

      Returns
      -------
      result: float
          wog
      """
    return zob_ogol/aktywa_ogol


def wzkw(zob_ogol: float, kapital_wlasny: float) -> float:

    """
      Wskaźnik zadłużenia kapitału własnego  (ang. Debt to equity ratio)

      Parameters
      ----------
      zob_ogol:float
          Zobowiązania ogółem (ang. Total debt)
      kapital_wlasny:float
          Kapitał własny (ang. Total amount of equity)

      Returns
      -------
      result: float
          wzkw
      """
#     if kapital_wlasny is None or kapital_wlasny == 0 or zob_ogol is None:
#         return None
    #     else:
    return zob_ogol / kapital_wlasny


def wdzo(zob_dlug: float, aktywa_ogol: float) -> float:

    """
      Wskaźnik długoterminowego zadłużenia ogółem  (ang. Long term debt ratio)

      Parameters
      ----------
      zob_dlug:float
          Zobowiązania długoterminowe (ang. Long term debt)
      aktywa_ogol:float
          Aktywa ogółem (ang. Total assets)

      Returns
      -------
      result: float
          wdzo
      """
#     if aktywa_ogol is None or aktywa_ogol == 0 or zob_dlug is None:
#         return None
#     else:
    return zob_dlug / aktywa_ogol


def wdzkw(zob_dlug: float, kapital_wlasny: float) -> float:

    """
      Wskaźnik długoterminowego zadłużenia kapitału własnego  (ang. Long term debt to equity ratio)

      Parameters
      ----------
      zob_dlug:float
          Zobowiązania długoterminowe (ang. Long term debt)
      kapital_wlasny:float
          Kapitał własny (ang. Total amount of equity)

      Returns
      -------
      result: float
          wdzo
      """
#     if kapital_wlasny is None or kapital_wlasny == 0 or zob_dlug is None:
#         return None
#     else:
    return zob_dlug / kapital_wlasny


def wuzd(zob_dlug: float, zob_ogol: float) -> float:

    """
      Wskaźnik udziału zobowiązań długoterminowych  (ang. Long term debt to total debt ratio)

      Parameters
      ----------
      zob_dlug:float
          Zobowiązania długoterminowe (ang. Long term debt)
      zob_ogol:float
          Zobowiązania ogółem (ang. Total debt)

      Returns
      -------
      result: float
          wuzd
      """
#     if zob_ogol is None or zob_ogol == 0 or zob_dlug is None:
#         return None
#     else:

    return zob_dlug / zob_ogol



def wpdr(rsmt: float, zob_dlug: float) -> float:

    """
      Wskaźnik pokrycia zobowiązań długoterminowymi rzeczowymi składnikami majątku  (ang. The ratio of coverage of liabilities with long-term tangible assets)

      Parameters
      ----------
      rsmt:float
          Rzeczowe składniki majątku trwałego (ang. Tangible fixed assets)
      zob_dlug:float
          Zobowiązania długoterminowe (ang. Long term debt)

      Returns
      -------
      result: float
          wpdr
      """
#     if zob_dlug is None or zob_dlug == 0 or rsmt is None:
#         return None
#     else:
    return rsmt / zob_dlug


def wsk(wzkw: float) -> float:

    """
    Wskaźnik struktury kapitału  (ang. Capital structure ratio)
    Wskaźnik struktury kapitału jest odwrotnością wskaźnika zadłużenia kapitału własnego
    Parameters
    ----------
    kapital_wlasny:float
    Kapitał własny (ang. Total amount of equity)
    zob_ogol:float
    Zobowiązania ogółem (ang. Total debt)

    Returns
    -------
    result: float
    wsk
    """
#     if wzkw is None or wzkw == 0:
#         return None
#     else:
    return (wzkw**-1)


def tsk(kapital_staly: float, aktywa_ogol: float) -> float:

    """
      Trwałość struktury finansowania  (ang. Capital to assets ratio)

      Parameters
      ----------
      kapital_staly:float
          Kapitał stały (ang. Constant capital)
      aktywa_ogol:float
          Aktywa ogółem (ang. Total assets)

      Returns
      -------
      result: float
          tsk
      """
#     if aktywa_ogol is None or aktywa_ogol == 0 or kapital_staly is None:
#         return None
#     else:
    return kapital_staly / aktywa_ogol



