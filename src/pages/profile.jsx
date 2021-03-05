import React from "react";
import { connect } from "react-redux";
import "./style/common.css";
import Header from "../components/Header";
import Paper from "@material-ui/core/Paper";
import Grid from "@material-ui/core/Grid";
import ProfileComponent from "../components/ProfileComponent";
import PostsScroll from "../components/PostsScroll";

class ProfilePage extends React.Component {
  render() {
    return (
      <div>
        <Header></Header>
        <div
          style={{ marginLeft: "10%", marginRight: "10%", marginTop: "30px" }}
        >
          <ProfileComponent></ProfileComponent>
        </div>
        <PostsScroll></PostsScroll>
      </div>
    );
  }
}

export default ProfilePage;
