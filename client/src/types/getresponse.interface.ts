
interface UserI {
    user_id: number
    user_name: string
}

interface UserlistI{
    userlist: UserI[]
}

interface GameDataI {
    score: number
    latitude: number
    longitude: number
    message: string
}

interface LeaderboardPlayerI {
    user_id: number
    user_name: string
    status: string
}


interface SortedUsers {
    [user_name: string]: LeaderboardPlayerI[]
}

interface sortedGamesByScoreI {
    user: string
    games: LeaderboardPlayerI[]
}[]

interface EndedGamesResponse{
    games: LeaderboardPlayerI[]
}

interface InputPropsI{
    type: string
    placeholder: string
    onChange: (e: string) => void
    value?: string | undefined
}

export type {UserI, sortedGamesByScoreI,  SortedUsers, GameDataI, EndedGamesResponse, LeaderboardPlayerI, UserlistI}