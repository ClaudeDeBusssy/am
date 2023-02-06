import React, { Component } from "react";

class Counter extends Component {
  state = {
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
        <div className="col">
          <button
            onClick={() => this.props.onDelete(this.props.counter.id)}
            className="btn btn-danger btn-sm m-2"
          >
            Delete
          </button>
          <button
            onClick={() => this.props.onIncrement(this.props.counter)}
            className="btn btn-secondary btn-sm"
          >
            +
          </button>
          <button
            onClick={() => this.props.onDecrement(this.props.counter)}
            className={this.formatDecrementButton()}
          >
            -
          </button>
          <span style={this.styles} className={this.getBadgeClasses()}>
            {this.formatCount()}
          </span>
          {/* {this.renderTags()} */}
        </div>
      </React.Fragment>
    );
  }

  formatDecrementButton() {
    let classes = "btn btn-secondary btn-sm m-2";
    let disabled = " disabled";

    if (this.props.counter.value === 0) {
      return (classes += disabled);
    } else {
      return classes;
    }
  }

  // onClickDecrement = () => {
  //   if (this.state.value > 0) {
  //     this.setState({ value: this.state.value - 1 });
  //   } else {
  //   }
  // };

  // onClickIncrement = () => {
  //   this.setState({ value: this.state.value + 1 });
  // };

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
    classes += this.props.counter.value === 0 ? "warning" : "primary";
    return classes;
  }

  formatCount() {
    const { value } = this.props.counter;
    return value === 0 ? "0" : value;
  }
}

export default Counter;
