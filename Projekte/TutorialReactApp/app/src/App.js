import React, { Component } from 'react';
import NavBar from './components/navbar';
import './App.css';
import Counters from './components/counters'

class App extends Component {
    state = {
        counters: [
          { id: 1, value: 3 },
          { id: 2, value: 2 },
          { id: 3, value: 5 },
          { id: 4, value: 4 },
          { id: 5, value: 1 },
        ],
      };


    render() {
        return (
            <React.Fragment>
                <NavBar totalCounters={this.state.counters.filter(c=> c.value > 0).length}></NavBar>
                <div className='container' >
            	    <Counters 
                    counters={this.state.counters}
                    onReset={this.handleReset}
                    onIncrement={this.handleIncrement}
                    onDecrement={this.handleDecrement}
                    onDelete={this.handleDelete}
                    ></Counters>
                </div>
            </React.Fragment>
        )
    }

    handleReset = () => {
        const counters = this.state.counters.map((c) => {
          c.value = 1;
          return c;
        });
        this.setState({ counters });
      };
    
      handleDelete = (counterId) => {
        const counters = this.state.counters.filter((c) => c.id !== counterId);
        this.setState({ counters });
      };
    
      handleIncrement = (counter) => {
        const counters = [...this.state.counters];
        const index = counters.indexOf(counter);
        counters[index] = { ...counter };
        counters[index].value++;
        this.setState({ counters });
      };
    
      handleDecrement = (counter) => {
        const counters = [...this.state.counters];
        const index = counters.indexOf(counter);
        counters[index] = { ...counter };
        if (counters[index].value > 0) {
          counters[index].value--;
          this.setState({ counters });
        } else {
        }
      };
}

export default App