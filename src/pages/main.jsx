import React from "react";
// redux
import { connect } from "react-redux";
import "./style/common.css";
import Header from "../components/Header";
import Gridsturc from "../components/Gridsturc";

class MainPage extends React.Component {
  /*componentDidMount = () => {
    // extract user
    const user = this.props.currentUser;
  };*/
  render() {
    return (
      <div>
        <Header></Header>
        <Gridsturc></Gridsturc>
      </div>
    );
  }
}

export default MainPage;
/*
// redux
const mapStateToProps = (state) => ({
  currentUser: state.user.currentUser,
});
export default connect(mapStateToProps)(MainPage);
*/
