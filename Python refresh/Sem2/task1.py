# Создайте несколько переменных разных типов.
# Проверьте к какому типу относятся созданные переменные.


a = [5, 1.479, "Goal", (1, 2), {5: "coal"}, {4, 5, 7}, frozenset((4, 6, 7)), True]

for i in a:
    print(type(i))
    print(type(i).__bases__)
    print(type(i).__mro__)
    print("---")

    # print(f"Is this int ? {isinstance(i, int)}")
    # print(f"Is this tuple ? {isinstance(i, tuple)}")
    # print(f"Is this bool ? {isinstance(i, bool)}")
    # print(f"Is this frozenset ? {isinstance(i, frozenset)}")
