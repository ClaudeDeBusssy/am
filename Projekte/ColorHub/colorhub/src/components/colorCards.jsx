import React, { Component } from "react";
import ColorCard from "./colorCard";

class colorCards extends Component {
  state = {
    colorCardData: [
      { id: 58, name: "ALFA ROMEO 814A nero vulcano", colorCode: "#312D30" },
      { id: 181, name: "BMW 355 byzanz", colorCode: "#7E4334" },
      { id: 249, name: "BMW A14,WA14 mineralsilber", colorCode: "#C2C1BA" },
      { id: 614, name: "FERRARI 523 blu nart", colorCode: "#174259" },
    ],
  };
  render() {
    return (
      <div className="mt-5">
        {this.state.colorCardData.map((data) => (
          <ColorCard key={data.id} data={data}></ColorCard>
        ))}
      </div>
    );
  }
}

export default colorCards;
