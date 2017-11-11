from typing import List

from exceptions import CalculateChangeError


def calculate_change(target: int, available: List[int]) -> List[int]:
    """A function to calculates the coins and notes to return given a certain amount.

    Args:
        - target: (int) total amount of change to return
        - available: (List[int]) of coins and notes that are available

    Returns:
        - (List[int]) of coins and notes that match the target
    """

    total_amount_available = sum(available)

    if target <= 0:
        raise CalculateChangeError('To calculate change requires the target amount to be positive.')

    if total_amount_available < target:
        raise CalculateChangeError("Amount available '{}' is not enough to give change for amount '{}'")

    if target in available:
        return [target]

    ordered_available = sorted(available, key=int, reverse=True)

    result = []
    rolling_target = target
    rolling_available = ordered_available

    for a in ordered_available:
        if rolling_target in rolling_available:
            result.append(rolling_target)
            rolling_available.remove(rolling_target)
            rolling_target -= rolling_target

        elif rolling_target > a:
            result.append(a)
            rolling_available.remove(a)
            rolling_target -= a
        else:
            raise CalculateChangeError('There is not enough change to match this amount')

        if rolling_target == 0:
            return sorted(result, key=int, reverse=True)
