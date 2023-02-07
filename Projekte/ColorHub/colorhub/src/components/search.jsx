import React, { Component } from "react";
import "./style.css";

class Search extends Component {
  state = {};
  render() {
    return (
      <div>
        <div className="input-group">
          <input
            type="text"
            className="form-control"
            placeholder="Color"
            aria-label="Recipient's username"
            aria-describedby="button-addon2"
          />
          <button
            className="btn btn-outline-primary"
            type="button"
            id="button_search"
            // onclick="onClickSearch()"
          >
            Search
          </button>
        </div>
      </div>
    );
  }
}

export default Search;
