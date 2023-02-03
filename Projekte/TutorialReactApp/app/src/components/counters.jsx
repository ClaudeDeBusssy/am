import React, { Component, createContext } from "react";
import Counter from "./counter";

class Counters extends Component {
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
      <div>
        {this.state.counters.map((counters) => (
          <Counter key={counters.id} value={counters.value} />
        ))}
      </div>
    );
  }
}

export default Counters;
