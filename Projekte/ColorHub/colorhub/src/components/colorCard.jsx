import React, { Component } from "react";

class colorCard extends Component {
  render() {
    const { data } = this.props;
    const colorCardBox = {
      backgroundColor: data.colorCode,
      width: "10%",
      height: "50px",
      border: "1px solid",
      borderColor: data.colorCode,
      borderRadius: "4px 0px 0px 4px",
    };
    const colorCardBorder = {
      border: "1px solid",
      borderColor: data.colorCode,
    };

    return (
      <div
        className="rounded d-flex align-items-start  mt-2 p-0"
        style={colorCardBorder}
      >
        <div className="" style={colorCardBox}></div>
        <button
          type="button"
          className="btn btn-light ms-2 align-self-center"
          data-bs-toggle="tooltip"
          data-bs-placement="top"
          data-bs-title="Tooltip on top"
        >
          {data.name}
        </button>
      </div>
    );
  }
}

export default colorCard;
