import React, { Component } from "react";

class NavBar extends Component {
  render() {
    return (
      <nav className="navbar navbar-light bg-light">
        <a href="" className="navbar-brand">
          Navbar
          <span className="badge rounded-pill bg-danger">
            {this.props.totalCounters}
          </span>
        </a>
      </nav>
    );
  }
}

export default NavBar;
