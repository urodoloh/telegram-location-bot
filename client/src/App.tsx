import { useState } from 'react';
import styled from 'styled-components';
import UserlistData from './components/UserlistData';
import { AppDiv } from './styles/styledComponents';
  

function App() {


  return (
    <AppDiv>
      <UserlistData/>
    </AppDiv>
  );
}

export default App;
