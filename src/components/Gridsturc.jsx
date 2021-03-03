import React from "react";
// redux
import Posting from "./Posting.jsx";
import Button from "@material-ui/core/Button";
import Paper from "@material-ui/core/Paper";
import Grid from "@material-ui/core/Grid";

export default function Gridsturc() {
  return (
    <div style={{ marginLeft: "10%", marginRight: "10%", marginTop: "30px" }}>
      <Grid
        container
        spacing={4}
        direction="horizenol"
        justify="center"
        alignItems="flex-start"
      >
        <Grid item xs={3}>
          <Paper style={{ height: "400px" }}>profile</Paper>
          <Paper style={{ height: "300px", marginTop: "10px" }}>profile</Paper>
        </Grid>
        <Grid item xs={6}>
          <Paper style={{ height: "710px", overflow: "auto" }}>
            <Posting style={{ margin: "10px" }}></Posting>
            <Posting style={{ margin: "10px" }}></Posting>
          </Paper>
        </Grid>
        <Grid item xs={3}>
          <Paper style={{ height: "50px" }}>
            <Button
              variant="contained"
              color="primary"
              style={{ height: "100%", width: "100%" }}
            >
              share your thoughts
            </Button>
          </Paper>
          <Paper style={{ height: "650px", marginTop: "10px" }}>profile</Paper>
        </Grid>
      </Grid>
    </div>
  );
}
