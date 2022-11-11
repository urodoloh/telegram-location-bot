
export interface User {
    user_id: number
    user_name: string
}


export interface GameDataI {
    score: number
    latitude: number
    longitude: number
    message: string
}

export interface LeaderboardPlayerI {
    user_id: number
    user_name: string
    status: string
}


export interface SortedUsers {
    [user_name: string]: LeaderboardPlayerI[]
}

interface sortedGamesByScoreI {
    user: string
    games: LeaderboardPlayerI[]
}[]

export interface EndedGamesResponse{
    games: LeaderboardPlayerI[]
}

interface InputPropsI{
    type: string
    placeholder: string
    onChange: (e: string) => void
    value?: string | undefined
}

