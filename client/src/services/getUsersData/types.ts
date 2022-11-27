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

export interface SortedGames {
  [user_name: string]: { games: Game[] };
}

export interface EndedGamesResponse {
  games: Game[];
}

export interface UserGames {
  user: string;
  score: number;
  lastGameDate: string | null;
}

export interface SortByOption {
  sort: "username" | "score";
  order: 1 | -1;
}
