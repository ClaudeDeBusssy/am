import React, { Component } from "react";
import "./style.css";

class Search extends Component {
  constructor(props) {
    super(props);
    this.search = React.createRef();
  }

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
            ref={this.search}
          />
          <button
            className="btn btn-outline-primary"
            type="button"
            id="button_search"
            onClick={() => this.props.onSearch(this.search.current.value)}
          >
            Search
          </button>
        </div>
      </div>
    );
  }
}

export default Search;
