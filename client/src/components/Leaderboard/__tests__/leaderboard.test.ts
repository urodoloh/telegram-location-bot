import { renderHook, act, waitFor } from "@testing-library/react";

import { useLeaderBoard } from "../hooks";

jest.mock("../__mocks__/node-fetch");

test("Leaderboard testing", async () => {
  const { result } = renderHook(() => useLeaderBoard());

  await waitFor(() => {
    expect(result.current.sortedGamesByUsers.length).toBe(3);
  });

  expect(result.current.sortedGamesByUsers).toEqual([
    { user: "Boris", score: 3 },
    { user: "DOLYA", score: 2 },
    { user: "LOLYA", score: 1 },
  ]);

  act(() => {
    result.current.searchOnChangeHandler({
      target: { value: "Boris" },
    } as React.ChangeEvent<HTMLInputElement>);
  });

  await waitFor(() => {
    expect(result.current.sortedGamesByUsers.length).toBe(1);
  });

  expect(result.current.sortedGamesByUsers).toEqual([
    { user: "Boris", score: 3 },
  ]);
});
