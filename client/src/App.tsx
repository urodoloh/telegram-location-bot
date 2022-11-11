import { useState } from 'react';
import styled from 'styled-components';
import { LeaderBoard } from './components/Leaderboard';
import { AppDiv } from './styles/styledComponents';

function App() {


  return (
    <AppDiv>
      <LeaderBoard/>
    </AppDiv>
  );
}

export default App;
