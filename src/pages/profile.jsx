import React from "react";
import { connect } from "react-redux";
import "./style/common.css";
import Header from "../components/Header";

import PostsScroll from "../components/PostsScroll";

class ProfilePage extends React.Component {
  render() {
    return (
      <div>
        <Header></Header>
        <hr></hr>
        <hr></hr>
        <PostsScroll></PostsScroll>
      </div>
    );
  }
}

export default ProfilePage;
