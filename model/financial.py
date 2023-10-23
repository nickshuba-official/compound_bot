import numpy as np


def compound(rate: [float, int], current_comp: str, target_comp: str, bullet_term_mnth: int = 0) -> float:
    if current_comp.lower() in ["d", "daily", "dly"]:
        interim_rate = np.log(1 + (rate / 100) / 365) * 365
    elif current_comp.lower() in ["w", "weekly", "wkly"]:
        interim_rate = np.log(1 + (rate / 100) / 52) * 52
    elif current_comp.lower() in ["m", "monthly", "mnthly", "mly"]:
        interim_rate = np.log(1 + (rate / 100) / 12) * 12
    elif current_comp.lower() in ["q", "quarterly", "qly"]:
        interim_rate = np.log(1 + (rate / 100) / 4) * 4
    elif current_comp.lower() in ["s", "s/a", "sa", "semiannual", "semi-annual"]:
        interim_rate = np.log(1 + (rate / 100) / 2) * 2
    elif current_comp.lower() in ["a", "y", "annual", "yearly"]:
        interim_rate = np.log(1 + (rate / 100))
    elif current_comp.lower() in ["b", "bullet", "iam"]:
        interim_rate = np.log(1 + (rate / 100) * bullet_term_mnth / 12) * 12 / bullet_term_mnth
    elif current_comp.lower() in ["c", "cc", "continuous"]:
        interim_rate = rate / 100
    else:
        pass

    if target_comp.lower() in ["d", "daily", "dly"]:
        target_comp_rate = (np.exp(interim_rate / 365) - 1) * 365 * 100
    elif target_comp.lower() in ["w", "weekly", "wkly"]:
        target_comp_rate = (np.exp(interim_rate / 52) - 1) * 52 * 100
    elif target_comp.lower() in ["m", "monthly", "mnthly", "mly"]:
        target_comp_rate = (np.exp(interim_rate / 12) - 1) * 12 * 100
    elif target_comp.lower() in ["q", "quarterly", "qly"]:
        target_comp_rate = (np.exp(interim_rate / 4) - 1) * 4 * 100
    elif target_comp.lower() in ["s", "s/a", "sa", "semiannual", "semi-annual"]:
        target_comp_rate = (np.exp(interim_rate / 2) - 1) * 2 * 100
    elif target_comp.lower() in ["a", "y", "annual", "yearly"]:
        target_comp_rate = (np.exp(interim_rate) - 1) * 100
    elif target_comp.lower() in ["b", "bullet", "iam"]:
        target_comp_rate = (np.exp(interim_rate / 12 * bullet_term_mnth) - 1) * 12 * 100 / bullet_term_mnth
    elif target_comp.lower() in ["c", "cc", "continuous"]:
        target_comp_rate = target_comp
    else:
        pass

    return target_comp_rate
