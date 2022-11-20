import styled from "styled-components";

export const S = {
  LeaderboardS: styled.div`
    flex-direction: row;
    justify-content: center; //Y
    align-items: center; //
    height: 600px;
    background: lightblue;
  `,
  HeaderS: styled.header`
    justify-content: center; //Y
    align-items: center; //X
    height: 120px;
    background: #1c87c9;
    color: #fff;
  `,
  HeaderSectionOneS: styled.section`
    display: flex;
    gap: 10px 20px; /* row-gap column gap */
    column-gap: 20px;
    justify-content: space-evenly; //Y
  `,
  TitleS: styled.section`
    order: 2;
    font-size: 3ch;
    text-align: center;
  `,
  Subtitle: styled.section`
    order: 1;
    font-size: 2ch;
    text-align: center;
  `,
  FilterS: styled.div`
    text-align: center;

    justify-content: center; //Y
    align-items: center; //X
  `,
  UserBlockS: styled.div`
    text-align: center;
    height: 40px;
  `,
  FooterS: styled.footer`
    display: flex;
    justify-content: start; //Y
    align-items: center; //X
    height: 120px;
    font-size: 2ch;
    background: #1c87c9;
    color: #fff;
  `,
};
