import { useCallback, useEffect, useMemo, useState } from "react";

import { getEndedGames } from "../../services/getUsersData";
import {
  Game,
  SortedUsers,
  UserGames,
} from "../../services/getUsersData/types";

export function useLeaderBoard() {
  const [gamesData, setGamesData] = useState<Game[]>([]);
  const [usernameFilter, setUsernameFilter] = useState<string>("");

  useEffect(() => {
    getEndedGames().then((data) => {
      setGamesData(data);
    });
  }, []);

  const sortedGamesByUsers = useMemo(() => {
    const groupedGames: SortedUsers = {};

    gamesData.map((game) => {
      if (groupedGames[game.user_name]) {
        let lastDate = game.date;
        if (lastDate < groupedGames[game.user_name].date) {
          lastDate = groupedGames[game.user_name].date;
        }
        groupedGames[game.user_name] = {
          games: [...groupedGames[game.user_name].games, game],
          date: lastDate,
        };
      } else {
        const lastDate = game.date;
        groupedGames[game.user_name] = { games: [game], date: lastDate };
      }
    });

    const gamesList: UserGames[] = Object.keys(groupedGames).map((user) => ({
      user: user,
      score: groupedGames[user].games.length,
      date: groupedGames[user].date,
    }));

    const filteredGames: UserGames[] = usernameFilter
      ? gamesList.filter((game) => game.user.includes(usernameFilter))
      : [...gamesList];

    const sortedGames = filteredGames.sort((a, b) => b.score - a.score);

    return sortedGames;
  }, [gamesData, usernameFilter]);

  const searchOnChangeHandler = useCallback(
    (e: React.ChangeEvent<HTMLInputElement>) => {
      setUsernameFilter(e.target.value);
    },
    [setUsernameFilter]
  );

  return { searchOnChangeHandler, sortedGamesByUsers };
}
