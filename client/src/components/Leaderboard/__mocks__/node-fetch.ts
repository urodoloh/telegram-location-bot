export default function fetch(
  url: RequestInfo,
  init?: RequestInit | undefined
) {
  return {
    json: () =>
      Promise.resolve([
        {
          status: "done",
          user_id: 413310716,
          user_name: "LOLYA",
          date: "2022-11-30 15:08:26.102946",
        },
        {
          status: "done",
          user_id: 413112716,
          user_name: "Boris",
          date: "2022-11-24 15:08:26.102946",
        },
        {
          status: "done",
          user_id: 413112716,
          user_name: "Boris",
          date: "2022-11-23 15:08:26.102946",
        },
        {
          status: "done",
          user_id: 413112716,
          user_name: "Boris",
          date: "2022-11-21 15:08:26.102946",
        },
        {
          status: "done",
          user_id: 432112716,
          user_name: "DOLYA",
          date: "2022-11-20 15:08:26.102946",
        },
        {
          status: "done",
          user_id: 432112716,
          user_name: "DOLYA",
          date: "2022-11-18 15:08:26.102946",
        },
      ]),
  };
}
