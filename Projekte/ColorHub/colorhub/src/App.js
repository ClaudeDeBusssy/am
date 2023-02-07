
import './App.css';
import './components/style.css'
import Navbar from './components/navbar';
import Search from './components/search';
import ColorCards from './components/colorCards';

function App() {
  return (
    <div className='backgroundGradient'>
    <Navbar></Navbar>

    <div className="container shadow px-5 bottom">
         
        <Search ></Search>

        <ColorCards ></ColorCards>
     
      </div>
    </div>
  );
}

export default App;
