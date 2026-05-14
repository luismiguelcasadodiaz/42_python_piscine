import os
import time

# 100%|███████████████████████| 333/333 [00:01<00:00, 194.45it/s]
# 12345-----------------------67---8---90123456789012345678901234
# ......................................1.........2.........3....
# -----------------------------/nnn/nnn/-------------------------


def ft_tqdm(lst: range) -> None:
    """
    Display a progress bar in the terminal, mimicking tqdm behavior.

    Iterates over the given range, yielding each element while printing
    a dynamic progress bar to stdout. The bar adapts to the terminal
    width and shows completion percentage, item count, elapsed time,
    estimated remaining time, and iteration speed.

    Args:
        lst: A range object to iterate over.

    Yields:
        Each element of lst, one at a time.

    Example:
        >>> for item in ft_tqdm(range(1000)):
        ...     pass
         45%|████████████████             | 450/1000 [00:03<00:04, 112.50it/s]
    """
    all = len(lst)
    columns = os.get_terminal_size().columns
    fixchar = 34
    varchar = len(str(all))  # nnn
    barchar = columns - fixchar - (varchar * 2)
    prev_per = 0
    t0 = time.time()
    for current, e in enumerate(lst):
        yield e
        per = (current + 1) * 100 // all
        if per != prev_per:
            elapsed_seconds = time.time() - t0
            lasting_seconds = all * elapsed_seconds / (current + 1)
            remain_seconds = lasting_seconds - elapsed_seconds
            elapsed_time = time.strftime("%M:%S", time.gmtime(elapsed_seconds))
            remain_time = time.strftime("%M:%S", time.gmtime(remain_seconds))
            ite_second = (current + 1) / elapsed_seconds
            per = (current + 1) * 100 // all
            barfull = per * barchar // 100
            barempt = barchar - barfull
            bar = "█" * barfull + " " * barempt
            chunk1 = f"{per:3}%|{bar}| {current + 1:{varchar}d}/{all} "
            chunk3 = f"[{elapsed_time}<{remain_time}, {ite_second:.2f}it/s]"
            print("\r" + chunk1 + chunk3, end="", flush=True)
            prev_per = per
