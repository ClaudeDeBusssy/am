import React, { Component } from "react";
import ColorCard from "./colorCard";

class colorCards extends Component {
  render() {
    return (
      <div className="mt-5">
        {this.props.colors.map((data) => (
          <ColorCard key={data.id} data={data}></ColorCard>
        ))}
      </div>
    );
  }
}

export default colorCards;
