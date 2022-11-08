import React from 'react';


const UserRow = ({element}: any, {key}: any) => {
    if (element.games !== undefined){
        return (
            <div>
              <p key={`user-${key}`}>{element.user} | SCORE: {element.games.length}</p>
            </div>
          );
    }else{
        return (
            <div>
                <p>User not found</p>
            </div>
        )
    }
    
};

export default UserRow;