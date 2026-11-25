from service import check

N1 = 5
N2 = 29
N = N1 + N2
K = 8 + N % 5

def report(case, expected, actual):
    status = "PASS" if actual == expected else "FAIL"
    print(case, expected, actual, status, sep=" | ")

cases = [
    ([0, 60], "OK"),
    ([30] * K, "OK"),
    (None, "TYPE"),
    ([], "EMPTY"),
    ([30, True], "BAD_ITEM"),
    ([61], "BAD_ITEM"),
    ([-1], "BAD_ITEM"),
    ([None] * (K + 1), "OVERLOAD"),
]

for i, (values, expected) in enumerate(cases, 1):
    report(f"Б-{i:02}", expected, check(values, K))

actual_stress = (check([30] * (1000 * K), K), check([30], K))
report("Б-09", ("OVERLOAD", "OK"), actual_stress)

# Испытание 2 (раздел 7): Восстановление (ровно K допустимых после перегрузки)
actual_recovery = (check([30] * (1000 * K), K), check([30] * K, K))
report("Б-10", ("OVERLOAD", "OK"), actual_recovery)
