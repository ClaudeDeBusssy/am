import React, { Component } from "react";

import "./style.css";

class Navbar extends Component {
  state = {};
  render() {
    return (
      <nav className="navbar bg-light transparent">
        <div className="container-fluid">
          <a className="navbar-brand">Color Hub</a>
        </div>
      </nav>
    );
  }
}

export default Navbar;
