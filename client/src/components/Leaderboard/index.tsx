import {useLeaderBoard} from './hooks';
import {S} from './styles';

export function LeaderBoard() {
 const {searchOnChangeHanler, users} = useLeaderBoard();

 return(
   <S.LeaderboardWrapper>
     <>
        <input onChange={searchOnChangeHanler} placeholder="Enter username"/>
     </>
        {users.map((user) => (
            <S.UserBlockWrapper>
               <p key={`user-${user.key}`}>{user.user} | SCORE: {user.games}</p>        
            </S.UserBlockWrapper>
        ))}       
   </S.LeaderboardWrapper>
  )
}