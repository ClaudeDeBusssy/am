import React, { Component } from "react";
import "./style.css";

class colorCard extends Component {
  state = {
    colorButton: "",
  };
  render() {
    const { data } = this.props;
    const colorCardBox = {
      backgroundColor: data.hexcode,
      borderColor: data.hexcode,
    };
    const colorCardBorder = {
      borderColor: data.hexcode,
    };

    return (
      <div
        className="rounded d-flex align-items-start  mt-2 colorCardBorder"
        style={colorCardBorder}
      >
        <div className="colorCardBox" style={colorCardBox}></div>
        <div className="ms-2 align-self-center">
          <button
            type="button"
            className="btn-copy m-2"
            style={colorCardBorder}
            onClick={() => this.handleCopyName(data.name)}
          >
            <div>{data.name}</div>
          </button>
          {this.state.colorButton}
        </div>
        <div className="ms-2 align-self-center">
          <button
            type="button"
            className="btn-copy m-2"
            style={colorCardBorder}
            onClick={() => this.handleCopyName(data.hexcode)}
          >
            HEX {data.hexcode}
          </button>
        </div>
      </div>
    );
  }

  handleCopyName(text) {
    console.log("clicked");
    this.setState(
      {
        colorButton: "",
      },
      () => this.setState({ colorButton: <p className="hideMe">copied!</p> })
    );
    navigator.clipboard.writeText(text);
  }
}

export default colorCard;
