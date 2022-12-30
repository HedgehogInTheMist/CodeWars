rom
typing
import Tuple


def mag_number(info: Tuple[str, int]) -> int:
    """
    Returns the number of magazines a soldier needs given a
    tuple containing the name of a soldier's weapon and
    the number of streets the soldier has to patrol.

    >>> mag_number(("PT92", 6))
    2
    >>> mag_number(("M4A1", 6))
    1
    """
    armory = {
        'PT92': 17,
        'M4A1': 30,
        'M16A2': 30,
        'PSG1': 5,
    }
    amount_of_bullets_required = info[1] * 3
    bullets_in_magazine = armory.get(info[0])
    bullets_vs_magazine_capacity = divmod(amount_of_bullets_required, bullets_in_magazine)

    return bullets_vs_magazine_capacity[0] if bullets_vs_magazine_capacity[1] == 0 else bullets_vs_magazine_capacity[0] + 1