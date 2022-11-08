import { LeaderboardPlayerI } from "../types/getresponse.interface";
import { SortedUsers } from "../types/getresponse.interface";

export function useTheGames(games: LeaderboardPlayerI[]):SortedUsers {
  const sortedGames:SortedUsers = {}; //init empty object
  
  for (const game of games) {
   if (sortedGames[game.user_name]) {
     sortedGames[game.user_name] = [...sortedGames[game.user_name], game];
    } else {
     sortedGames[game.user_name] = [game];
    }
  }
  return sortedGames;
  
}
