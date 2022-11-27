import { LeaderBoard } from "./components/Leaderboard";
import { S } from "./styles";

function App() {
  return (
    <S.AppWrapper>
      <S.AppContent>
        <LeaderBoard />
      </S.AppContent>
    </S.AppWrapper>
  );
}

export default App;
