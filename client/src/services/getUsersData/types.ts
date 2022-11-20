export interface User {
  user_id: number;
  user_name: string;
}

export interface Game {
  user_id: number;
  user_name: string;
  status: string;
  date: string;
}

export interface SortedUsers {
  [user_name: string]: { games: Game[]; date: string };
}

export interface EndedGamesResponse {
  games: Game[];
}

export interface UserGames {
  user: string;
  score: number;
  date: string;
}
