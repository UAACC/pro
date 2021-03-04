import React from "react";
// redux
import Posting from "./Posting.jsx";
import Button from "@material-ui/core/Button";
import Paper from "@material-ui/core/Paper";
import Grid from "@material-ui/core/Grid";
import Profile from "./ProfileComponent.jsx";

export default function PostsScroll() {
  return (
    <div style={{ marginLeft: "10%", marginRight: "10%", marginTop: "30px" }}>
      <Grid
        container
        spacing={4}
        // direction = "column"
        direction="horizenol"
        justify="center"
        alignItems="flex-start"
      >
        <Grid item xs={6}>
            <Paper style={{ height: "900px", overflow: "auto" }}>
            <Posting style={{ margin: "10px" }}></Posting>
            <Posting style={{ margin: "100px" }}></Posting>
            <Posting style={{ margin: "10px" }}></Posting>
            </Paper> 
        </Grid>
        <Grid item xs={3}>
          <Profile></Profile>
        </Grid>
      </Grid>
    </div>
  );
}