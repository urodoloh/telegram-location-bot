import {useState, useEffect} from 'react';
import { GetAPI } from '../API';
import { LeaderboardPlayerI } from '../types/getresponse.interface';

export const useGetEndedGames = () => {
    const [games, setGames] = useState<LeaderboardPlayerI[]>([]);
    const [isError, setIsError] = useState<boolean>(false)
    
	useEffect(() => {
        GetAPI.getEndedGames()
            .then((data) => {
                let ue = data.games
                setGames(ue)
            })
            .catch((err) => {
                setIsError(true);
                console.log("useGetEndedGamesList Error:", isError);
            });
    }, []);
    return games    
}