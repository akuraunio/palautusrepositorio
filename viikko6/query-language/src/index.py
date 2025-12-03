from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, Not, HasFewerThan, All, Or, QueryBuilder


def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    # matcher = And(Not(HasAtLeast(2, "goals")), PlaysIn("NYR"))
    # matcher = And(HasFewerThan(2, "goals"), PlaysIn("NYR"))
    # matcher = Or(HasAtLeast(45, "goals"), HasAtLeast(70, "assists"))
    # matcher = And(
    #    HasAtLeast(70, "points"), Or(PlaysIn("COL"), PlaysIn("FLA"), PlaysIn("BOS"))
    # )

    # filtered_with_all = stats.matches(All())
    # print(len(filtered_with_all))

    query = QueryBuilder()
    # matcher = query.build()
    matcher = query.one_of(
        query.plays_in("PHI").has_at_least(10, "assists").has_fewer_than(10, "goals"),
        query.plays_in("EDM").has_at_least(50, "points"),
    ).build()
    # print(len(stats.matches(matcher)))

    for player in stats.matches(matcher):
        print(player)


if __name__ == "__main__":
    main()
