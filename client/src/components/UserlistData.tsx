import { useState } from 'react';
import styled from 'styled-components';
import { useGetEndedGames } from '../hooks/useGetEndedGames';
import { useTheGames } from '../hooks/useTheGames';
import { UserlistDataDiv } from '../styles/styledComponents';
import { SortedUsers } from "../types/getresponse.interface";
import SearchBar from './Search';
import UserRow from './UserRow';


export default function UserlistData() {
  const Sgames = useGetEndedGames();
  const sortedGamesByUsers = useTheGames(Sgames);    
  const sortedGamesByUsersDestruction = Object.keys(sortedGamesByUsers).map((user, userIndex) => ({user: user, games: sortedGamesByUsers[user]}));
  const sortedGamesByScore = sortedGamesByUsersDestruction.sort((a, b) => (b.games.length - a.games.length));

  // SORTED USERLIST
  const sortedUserlist = sortedGamesByScore.map((element, elementIndex) => (
    <p key={`user-${elementIndex}`}>{element.user} | SCORE: {element.games.length}</p>
  ))
  
  

  const [searchResult, setSearchResult] = useState([{}]);
  const [notFound, setNotFound] = useState(true)
  
  const searchText = (text:string) => {
    const result = sortedGamesByScore.filter(user => user.user === text);
    console.log(result.length);
    console.log(notFound);
    
    if (result.length >= 1){
      setSearchResult(result)
      setNotFound(false)
    } 
    if (result.length <= 0) {
      setSearchResult(result)
      setNotFound(true)
    }
  }


  function renderedResults(){
    if (notFound === false){
      searchResult.map((element, elementIndex)=>{
        return <UserRow element={element} key={elementIndex}/>
      })
    } 
    if (notFound === true){
      return sortedUserlist
    }
  }
  

  
  return (<UserlistDataDiv>
      <SearchBar input={(text:string) => searchText(text)}/>
      {/* <div>{sortedUserlist}</div> */}
      <div>{renderedResults()}</div>
    </UserlistDataDiv>)
}
