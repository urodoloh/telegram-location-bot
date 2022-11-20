import ReactTooltip from "react-tooltip";

import { useLeaderBoard } from "./hooks";
import { S } from "./styles";

export function LeaderBoard() {
  const { searchOnChangeHandler, sortedGamesByUsers } = useLeaderBoard();

  return (
    <S.LeaderboardS>
      <S.HeaderS>
        <S.TitleS>Telegram Get-Point Game</S.TitleS>
        <S.TitleS>Leaderboard Page</S.TitleS>
        <S.HeaderSectionOneS>
          <S.Subtitle>Username</S.Subtitle>
          <S.Subtitle>Score</S.Subtitle>
        </S.HeaderSectionOneS>
      </S.HeaderS>

      <S.FilterS>
        <input onChange={searchOnChangeHandler} placeholder="Enter username" />
      </S.FilterS>

      {sortedGamesByUsers.map((userGames, userGamesIndex) => (
        <S.UserBlockS>
          <div key={`user-games-${userGamesIndex}`}>
            <p data-for={`user-games-${userGamesIndex}`} data-tip>
              {userGames.user} {userGames.score}
            </p>
            <ReactTooltip id={`user-games-${userGamesIndex}`}>
              <span>
                {userGames.user} <br /> {userGames.date}
              </span>
            </ReactTooltip>
          </div>
        </S.UserBlockS>
      ))}

      <S.FooterS>BY URODOLOH</S.FooterS>
    </S.LeaderboardS>
  );
}
