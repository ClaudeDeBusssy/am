import React, { Component } from "react";

class Search extends Component {
  state = {};
  render() {
    return (
      <div className="input-group mt-5">
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
    );
  }
}

export default Search;
