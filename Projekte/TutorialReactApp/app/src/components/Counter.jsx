import React, { Component } from "react";

class Counter extends Component {
  state = {
    value: this.props.value,
    tags: ["tag1", "tag2", "tag3"],
  };

  styles = {
    fontSize: 15,
    fontWeight: "bold",
  };

  // constructor () {
  //   super();
  //   this.onClickIncrement = this.onClickIncrement.bind(this);
  // }

  render() {
    return (
      <React.Fragment>
        <span style={this.styles} className={this.getBadgeClasses()}>
          {this.formatCount()}
        </span>
        <button
          onClick={this.onClickIncrement}
          className="btn btn-warning btn-sm"
        >
          Increment
        </button>

        {/* {this.renderTags()} */}
      </React.Fragment>
    );
  }

  onClickIncrement = () => {
    this.setState({ value: this.state.value + 1 });
  };

  // renderTags() {
  //   if (this.state.tags.length === 0) {
  //     return <h1>NO TAGS FOR YOU</h1>;
  //   } else {
  //     return (
  //       <ul>
  //         {this.state.tags.map((tag) => (
  //           <li key={tag}>{tag}</li>
  //         ))}
  //       </ul>
  //     );
  //   }
  // }

  getBadgeClasses() {
    let classes = "badge m-2 bg-";
    classes += this.state.value === 0 ? "warning" : "primary";
    return classes;
  }

  formatCount() {
    const { value: count } = this.state;
    return count === 0 ? "Zero" : count;
  }
}

export default Counter;
