export default function fetch(
  url: RequestInfo,
  init?: RequestInit | undefined
) {
  return {
    json: () =>
      Promise.resolve([
        { status: "done", user_id: 413310716, user_name: "LOLYA" },
        { status: "done", user_id: 413112716, user_name: "Boris" },
        { status: "done", user_id: 413112716, user_name: "Boris" },
        { status: "done", user_id: 413112716, user_name: "Boris" },
        { status: "done", user_id: 432112716, user_name: "DOLYA" },
        { status: "done", user_id: 432112716, user_name: "DOLYA" },
      ]),
  };
}
