import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Schedule from './Schedule';
import Search from './Search';
import Main from './Main';

function App() {
  return (
      <Routes>
        <Route path="/" element={<Main />} />
        <Route path="/search" element={<Search />} />
        <Route path="/schedule/:plantId" element={<Schedule />} />
      </Routes>
  );
}

export default App;
