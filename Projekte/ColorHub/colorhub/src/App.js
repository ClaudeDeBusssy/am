
import './App.css';
import './components/style.css'
import Navbar from './components/navbar';
import Search from './components/search';
import ColorCards from './components/colorCards';

function App() {
  return (
    <div className='backgroundGradient pb-5'>
    <Navbar></Navbar>

    <div className="container   p-5 mt-5 bottom ">
         
        <Search ></Search>

        <ColorCards ></ColorCards>
     
      </div>
    </div>
  );
}

export default App;
