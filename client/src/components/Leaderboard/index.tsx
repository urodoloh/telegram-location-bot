import { useState } from "react";
import ReactTooltip from "react-tooltip";
import styled from "styled-components";

import { useLeaderBoard } from "./hooks";
import { S } from "./styles";

export function LeaderBoard() {
  const {
    searchOnChangeHandler,
    sortedGames,
    sortByScore,
    sortByName,
    getGameScoreScale,
  } = useLeaderBoard();

  return (
    <S.Leaderboard>
      <S.Header>
        <S.Title>Leaderboard</S.Title>
        <S.ColumnNames>
          <S.UserTitle onClick={sortByName}>username</S.UserTitle>

          <S.ScoreTitle onClick={sortByScore}>score</S.ScoreTitle>
        </S.ColumnNames>
      </S.Header>

      <S.Main>
        <S.FilterBlock>
          <S.SearchIcon src={require("./icons/loupe.JPG")} />
          <S.Input
            onChange={searchOnChangeHandler}
            placeholder="Enter username"
          />
        </S.FilterBlock>

        <S.UsersListColumn>
          {sortedGames.map((userGames, userGamesIndex) => (
            <S.UserBlock key={userGamesIndex}>
              <S.UsernameBlock>
                <S.Username data-for={`user-games-${userGamesIndex}`} data-tip>
                  {userGames.user}
                </S.Username>
                <ReactTooltip id={`user-games-${userGamesIndex}`}>
                  <span>
                    {userGames.user} <br /> {userGames.lastGameDate}
                  </span>
                </ReactTooltip>
              </S.UsernameBlock>

              <S.ScoreBlock>
                <S.ScoreValue>{userGames.score}</S.ScoreValue>

                <S.Progress
                  width={`${getGameScoreScale(userGames)}%`}
                ></S.Progress>
              </S.ScoreBlock>
            </S.UserBlock>
          ))}
        </S.UsersListColumn>
      </S.Main>

      <S.Footer>
        <h4>BY URODOLOH</h4>
        <h5> my links:</h5>
        <S.Link href="https://github.com/urodoloh/telegram-location-bot">
          GitHub Page
        </S.Link>
      </S.Footer>
    </S.Leaderboard>
  );
}
