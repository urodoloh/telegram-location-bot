import fetch from "node-fetch";
import { Game } from "./types";

export async function getEndedGames(): Promise<Game[]> {
  const response = await fetch("http://localhost:5000/api/thegame", {
    method: "get",
  });
  return (await response.json()) as Promise<Game[]>;
}
