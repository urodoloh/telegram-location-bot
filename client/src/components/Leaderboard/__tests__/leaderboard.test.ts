import { ResultType } from "@remix-run/router/dist/utils";
import { renderHook, act, waitFor } from "@testing-library/react";

import { useLeaderBoard } from "../hooks";

jest.mock("../__mocks__/node-fetch");

describe("Leaderboard testing", () => {
  test("Search testing", async () => {
    const { result } = renderHook(() => useLeaderBoard());

    await waitFor(() => {
      expect(result.current.sortedGames.length).toBe(3);
    });

    expect(result.current.sortedGames).toEqual([
      { user: "Boris", score: 3, lastGameDate: "2022-11-24 15:08:26.102946" },
      { user: "DOLYA", score: 2, lastGameDate: "2022-11-20 15:08:26.102946" },
      { user: "LOLYA", score: 1, lastGameDate: "2022-11-30 15:08:26.102946" },
    ]);

    act(() => {
      result.current.searchOnChangeHandler({
        target: { value: "Boris" },
      } as React.ChangeEvent<HTMLInputElement>);
    });

    await waitFor(() => {
      expect(result.current.sortedGames.length).toBe(1);
    });

    expect(result.current.sortedGames).toEqual([
      { user: "Boris", score: 3, lastGameDate: "2022-11-24 15:08:26.102946" },
    ]);
  });

  test("Sort testing", async () => {
    const { result } = renderHook(() => useLeaderBoard());

    await waitFor(() => {
      expect(result.current.sortedGames.length).toBe(3);
    });

    act(() => {
      result.current.sortByScore();
    });

    expect(result.current.sortBy).toEqual({
      sort: "score",
      order: -1,
    });

    expect(result.current.sortedGames).toEqual([
      { user: "LOLYA", score: 1, lastGameDate: "2022-11-30 15:08:26.102946" },
      { user: "DOLYA", score: 2, lastGameDate: "2022-11-20 15:08:26.102946" },
      { user: "Boris", score: 3, lastGameDate: "2022-11-24 15:08:26.102946" },
    ]);

    act(() => {
      result.current.sortByName();
    });

    expect(result.current.sortBy).toEqual({
      sort: "username",
      order: 1,
    });

    expect(result.current.sortedGames).toEqual([
      { user: "Boris", score: 3, lastGameDate: "2022-11-24 15:08:26.102946" },
      { user: "DOLYA", score: 2, lastGameDate: "2022-11-20 15:08:26.102946" },
      { user: "LOLYA", score: 1, lastGameDate: "2022-11-30 15:08:26.102946" },
    ]);

    act(() => {
      result.current.sortByName();
    });

    expect(result.current.sortBy).toEqual({
      sort: "username",
      order: -1,
    });

    expect(result.current.sortedGames).toEqual([
      { user: "LOLYA", score: 1, lastGameDate: "2022-11-30 15:08:26.102946" },
      { user: "DOLYA", score: 2, lastGameDate: "2022-11-20 15:08:26.102946" },
      { user: "Boris", score: 3, lastGameDate: "2022-11-24 15:08:26.102946" },
    ]);
  });

  test("Scale bar testing", async () => {
    const { result } = renderHook(() => useLeaderBoard());

    await waitFor(() => {
      expect(result.current.sortedGames.length).toBe(3);
    });
    act(() => {
      result.current.maxScore;
    });

    expect(result.current.maxScore).toBe(3);

    expect(
      result.current.getGameScoreScale({
        user: "Boris",
        score: 3,
        lastGameDate: "2022-11-24 15:08:26.102946",
      })
    ).toBeCloseTo(100, 1);

    expect(
      result.current.getGameScoreScale({
        user: "DOLYA",
        score: 2,
        lastGameDate: "2022-11-20 15:08:26.102946",
      })
    ).toBeCloseTo(66.66, 1);

    expect(
      result.current.getGameScoreScale({
        user: "LOLYA",
        score: 1,
        lastGameDate: "2022-11-30 15:08:26.102946",
      })
    ).toBeCloseTo(33.33, 1);
  });
});
