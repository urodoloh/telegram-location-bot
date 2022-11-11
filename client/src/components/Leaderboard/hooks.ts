import { useCallback, useEffect, useMemo, useState } from "react";
import { GetAPI } from '../../API';
import { User, LeaderboardPlayerI, SortedUsers } from "../../types/getresponse.interface";




export function useLeaderBoard() {
    const [usersData, setUsersData] = useState<LeaderboardPlayerI[]>([]);
    const [usernameFilter, setUsernameFilter] = useState('');

    useEffect(() => {
            GetAPI.getEndedGames().then((data) => {
                setUsersData(data.games);
            });
    }, []);

    const sortedGamesByUsers = useMemo(()=>{
        const groupedGames:SortedUsers = {};

        usersData.map((game)=>{
            if(groupedGames[game.user_name]){
                groupedGames[game.user_name] = [...groupedGames[game.user_name], game];
            } else {
                groupedGames[game.user_name] = [game]
            }
        });

        const gamesList =  Object.keys(groupedGames).map((user, userIndex) => ({user: user, games: groupedGames[user].length, key: userIndex}));
        const sortedGames = gamesList.sort((a, b) => (b.games - a.games));
        
        
        return sortedGames

    }, [usersData])


    const searchOnChangeHanler = useCallback((e: React.ChangeEvent<HTMLInputElement>) => {
      setUsernameFilter(e.target.value);
     }, [setUsernameFilter])
     
    
    const users = useMemo(() => {
        const usersFilterResult = sortedGamesByUsers.filter((user) => user.user.includes(usernameFilter));
        
        
        return usersFilterResult
    }, [usersData, usernameFilter])
   

    return {searchOnChangeHanler, users}
   }

