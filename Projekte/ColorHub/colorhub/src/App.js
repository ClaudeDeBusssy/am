
import './App.css';
import Navbar from './components/navbar';
import Search from './components/search';
import ColorCards from './components/colorCards';

function App() {
  return (
    <div>
    <Navbar></Navbar>

    <div className="container">
         
        <Search></Search>

        <ColorCards></ColorCards>
     
      </div>
    </div>
  );
}

export default App;
