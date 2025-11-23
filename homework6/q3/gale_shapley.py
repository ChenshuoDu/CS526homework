def parse_input_file(path):
    """
    Parse the marriage input file.

    Format we assume:
    - First non-empty line: an integer n (number of men and women)
    - Next n lines: each line = man_name followed by all women in preference order
    - Next n lines: each line = woman_name followed by all men in preference order
    """
    lines = []
    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                lines.append(line)

    if not lines:
        raise ValueError("Input file is empty")

    n = int(lines[0])
    if len(lines) < 2 * n + 1:
        raise ValueError("Not enough lines for {} men and women".format(n))

    men_prefs = {}
    women_prefs = {}
    men_order = []
    women_order = []

    idx = 1
    for _ in range(n):
        parts = lines[idx].split()
        idx += 1
        man = parts[0]
        prefs = parts[1:]
        men_prefs[man] = prefs
        men_order.append(man)

    for _ in range(n):
        parts = lines[idx].split()
        idx += 1
        woman = parts[0]
        prefs = parts[1:]
        women_prefs[woman] = prefs
        women_order.append(woman)

    return n, men_order, women_order, men_prefs, women_prefs


def gale_shapley(men_prefs, women_prefs):
    """
    Gale–Shapley stable matching algorithm (men propose).
    men_prefs:  dict man -> list of women in preference order
    women_prefs: dict woman -> list of men in preference order
    Returns a dict man -> woman.
    """
    women_rank = {}
    for w, pref_list in women_prefs.items():
        rank = {man: i for i, man in enumerate(pref_list)}
        women_rank[w] = rank

    next_proposal_index = {m: 0 for m in men_prefs.keys()}

    engaged = {}

    free_men = list(men_prefs.keys())

    while free_men:
        m = free_men.pop(0)
        prefs = men_prefs[m]
        i = next_proposal_index[m]

        if i >= len(prefs):
            continue

        w = prefs[i]
        next_proposal_index[m] += 1

        if w not in engaged:
            engaged[w] = m
        else:
            current = engaged[w]
            if women_rank[w][m] < women_rank[w][current]:
                engaged[w] = m
                free_men.append(current)
            else:
                free_men.append(m)

    matches = {m: None for m in men_prefs.keys()}
    for w, m in engaged.items():
        matches[m] = w
    return matches
