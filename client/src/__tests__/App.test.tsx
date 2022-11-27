import React from "react";
import { render, screen, act, waitFor } from "@testing-library/react";
import App from "../App";

test("App rendered in 'root' div", () => {
  const { getByText } = render(<App />);

  expect(getByText("Leaderboard")).toBeInTheDocument();
});
