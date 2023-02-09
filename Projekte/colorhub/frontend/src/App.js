import "./App.css";
import "./components/style.css";
import Navbar from "./components/navbar";
import Search from "./components/search";
import ColorCards from "./components/colorCards";
import { Routes, Route } from "react-router-dom";
import React, { Component } from "react";

class App extends Component {
  state = {
    colors: [],
    gradient: {
      backgroundImage: "linear-gradient(to right,#D8E0DF, #D8E0DF)",
    },
  };

  render() {
    return (
      <div className="backgroundGradient pb-5" style={this.state.gradient}>
        <Routes>
          <Route
            path="/"
            element={
              <div>
                <Navbar></Navbar>

                <div className="container   p-5 mt-5 bottom ">
                  <Search onSearch={this.handleSearch}></Search>

                  <ColorCards colors={this.state.colors}></ColorCards>
                </div>
              </div>
            }
          ></Route>
        </Routes>

        {/*       
    <Navbar></Navbar>

    <div className="container   p-5 mt-5 bottom ">
         
        <Search ></Search>

        <ColorCards ></ColorCards>
     
      </div> */}
      </div>
    );
  }

  setGradiant() {
    if (this.state.colors) {
      let newgradiant = {
        backgroundImage: `linear-gradient(to right,${
          this.state.colors[
            Math.floor(Math.random() * (this.state.colors.length + 1)) + 1 - 1
          ].hexcode
        }, ${
          this.state.colors[
            Math.floor(Math.random() * (this.state.colors.length + 1)) + 1 - 1
          ].hexcode
        })`,
      };
      console.log(newgradiant);
      this.setState({ gradient: newgradiant });
    }
  }

  handleSearch = (search) => {
    fetch("http://localhost:8000/colors/?search=%22" + search + "%22")
      .then((res) => res.json())
      .then((json) => {
        this.setColors(json);
      });
  };

  componentDidMount() {
    fetch("http://localhost:8000/colors")
      .then((res) => res.json())
      .then((json) => {
        this.setColors(json);
      });
  }

  setColors(json) {
    if (json) {
      this.setState(
        {
          colors: json["data"],
        },
        () => this.setGradiant()
      );
    }
  }
}

export default App;
