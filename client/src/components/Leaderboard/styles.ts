import styled from "styled-components";

export const S = {
  Leaderboard: styled.div`
    display: flex;
    height: 100%;
    flex-direction: column;
    justify-content: space-between;
    text-transform: uppercase;
    text-align: center;
    font-family: Verdana, Geneva, Tahoma, sans-serif;
    font-weight: bold;
  `,
  Header: styled.div`
    display: flex;
    flex-direction: column;
    background: linear-gradient(#017777, #006d8a);
    color: white;
  `,
  Title: styled.h1`
    padding: 20px 150px;
    font-size: 230%;
  `,
  ColumnNames: styled.div`
    display: flex;
    flex-direction: row;
    padding: 10px 40px 10px 40px;
  `,
  UserTitle: styled.h3`
    padding: 20px 15px;
    border-top: 2px solid;
    &:hover {
      color: lightgreen;
    }
  `,
  ScoreTitle: styled.h3`
    padding: 20px 150px;
    border-top: 2px solid;
    border-left: 2px solid;
    &:hover {
      color: lightgreen;
    }
  `,
  Main: styled.div`
    min-height: 100%;
    display: flex;
    flex-direction: column;
    padding: 10px 40px;
  `,
  FilterBlock: styled.div`
    display: flex;
    flex-direction: row;
  `,
  Input: styled.input`
    font-weight: bold;
    border-radius: 10px;
    width: 100%;
    height: 22px;
  `,
  SearchIcon: styled.img`
    width: 22px;
    height: 22px;
  `,
  UsersListColumn: styled.div`
    display: flex;
    flex-direction: column;
  `,
  UserBlock: styled.div`
    display: flex;
    flex-direction: row;
    padding: 8px 0px;
  `,
  UsernameBlock: styled.div`
    padding-right: 20px;
  `,
  Username: styled.p`
    font-size: 90%;
    min-width: 150px;
    max-width: 150px;
    overflow: hidden;
    text-overflow: ellipsis;
    color: #36686f;
  `,
  ScoreBlock: styled.div`
    display: flex;
    flex-direction: row;
    width: 100%;
    border-radius: 10px;
    background-color: #b3b3b3;
    align-items: center;
  `,
  Progress: styled.div<{ width?: string }>`
    width: ${(props) => props.width};
    height: 20px;
    border-radius: 10px;
    background: linear-gradient(#037575, #047384);
  `,
  ScoreValue: styled.div`
    position: absolute;
    padding-left: 330px;
    font-size: 100%;
    color: white;
  `,
  Footer: styled.div`
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: center;
    padding: 10px 40px;
    font-size: 2ch;
    background: linear-gradient(#017777, #006d8a);
    color: white;
  `,
  Link: styled.a`
    color: white;
    &:hover {
      color: lightgreen;
    }
  `,
};
