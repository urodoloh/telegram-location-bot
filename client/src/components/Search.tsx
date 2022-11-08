import { SearchBarDiv } from '../styles/styledComponents';
import React, {useState, useEffect} from 'react'
import { useTheGames } from '../hooks/useTheGames';
import { useGetEndedGames } from '../hooks/useGetEndedGames';
import { LeaderboardPlayerI } from '../types/getresponse.interface';


const SearchBar = ({input}: any) => {
    const [searchInput, setSearchInput] = useState("");

    useEffect(()=>{
        if(searchInput !== ''){
            input(searchInput);
        }
    }, [searchInput])

    
    return (
      <div>
        <input 
            type='text' 
            placeholder="Search user by name. . ." 
            onChange={e => setSearchInput(e.target.value)}
            value={searchInput}
            />
      </div>
    );
};



export default SearchBar;