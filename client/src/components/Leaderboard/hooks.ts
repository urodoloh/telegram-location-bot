import { useCallback, useEffect, useMemo, useState } from "react";

import { getEndedGames } from "../../services/getUsersData";
import {
  Game,
  SortedGames,
  UserGames,
  SortByOption,
} from "../../services/getUsersData/types";

export function useLeaderBoard() {
  const [sortBy, setSortBy] = useState<SortByOption>({
    sort: "score",
    order: 1,
  });
  const [gamesData, setGamesData] = useState<Game[]>([]);
  const [usernameFilter, setUsernameFilter] = useState<string>("");

  useEffect(() => {
    getEndedGames().then((data) => {
      setGamesData(data);
    });
  }, []);

  const getLastGameDate = (games: Game[]) => {
    const sortedGames = [...games];

    if (games.length === 0) {
      return null;
    }

    sortedGames.sort((a, b) => {
      const aDate: Date = new Date(a.date);
      const bDate: Date = new Date(b.date);

      return bDate.getTime() - aDate.getTime();
    });

    return sortedGames[0].date;
  };

  const sortedGames = useMemo(() => {
    const groupedGames: SortedGames = {};

    gamesData.map((game) => {
      if (groupedGames[game.user_name]) {
        groupedGames[game.user_name] = {
          games: [...groupedGames[game.user_name].games, game],
        };
      } else {
        groupedGames[game.user_name] = { games: [game] };
      }
    });

    const gamesList: UserGames[] = Object.keys(groupedGames).map((user) => ({
      user: user,
      score: groupedGames[user].games.length,
      lastGameDate: getLastGameDate(groupedGames[user].games),
    }));

    const filteredGames: UserGames[] = usernameFilter
      ? gamesList.filter((game) => game.user.includes(usernameFilter))
      : [...gamesList];

    if (sortBy?.sort === "username") {
      filteredGames.sort((a, b) => {
        if (a.user < b.user) {
          return -1 * sortBy.order;
        }
        if (a.user > b.user) {
          return 1 * sortBy.order;
        }
        return 0;
      });
    }

    if (sortBy?.sort === "score") {
      filteredGames.sort((a, b) => (b.score - a.score) * sortBy.order);
    }

    return filteredGames;
  }, [gamesData, usernameFilter, sortBy]);

  const maxScore = useMemo(() => {
    return sortedGames.reduce(
      (max, currentGame) => Math.max(max, currentGame.score),
      0
    );
  }, [sortedGames]);

  const getGameScoreScale = useCallback(
    (game: UserGames) => {
      return 100 / (maxScore / game.score);
    },
    [maxScore]
  );

  const sortByHandler = useCallback(
    (sort: SortByOption["sort"]) => {
      setSortBy((prevSortBy) => {
        return {
          sort,
          order:
            prevSortBy !== undefined && prevSortBy.sort === sort
              ? prevSortBy.order * -1
              : 1,
        } as SortByOption;
      });
    },
    [setSortBy]
  );

  const sortByName = useCallback(() => {
    sortByHandler("username");
  }, [sortByHandler]);

  const sortByScore = useCallback(() => {
    sortByHandler("score");
  }, [sortByHandler]);

  const searchOnChangeHandler = useCallback(
    (e: React.ChangeEvent<HTMLInputElement>) => {
      setUsernameFilter(e.target.value);
    },
    [setUsernameFilter]
  );

  return {
    searchOnChangeHandler,
    sortedGames,
    sortByName,
    sortByScore,
    sortBy,
    maxScore,
    getGameScoreScale,
  };
}
