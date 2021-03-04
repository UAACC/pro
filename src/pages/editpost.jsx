import React from "react";
import { connect } from "react-redux";
import "./style/common.css";
import Header from "../components/Header";
import Radio from "@material-ui/core/Radio";
import Paper from "@material-ui/core/Paper";
import Grid from "@material-ui/core/Grid";
import TextField from "@material-ui/core/TextField";
import RadioGroup from "@material-ui/core/RadioGroup";
import FormControlLabel from "@material-ui/core/FormControlLabel";
import FormControl from "@material-ui/core/FormControl";
import FormLabel from "@material-ui/core/FormLabel";
import { Button } from "@material-ui/core";
import ChipInput from "material-ui-chip-input";

const emptyPost = {
  value: "",
  postTitle: "",
  postContent: "",
  postImage: "",
  sharewith: [],
  visibility: "public",
  categories: [],
};

class Editpost extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      value: "",
      postTitle: "",
      postContent: "",
      postImage: "",
      postFormat: "",
      categories: "",
    };
    this.handleFormat = this.handleFormat.bind();
    this.handleChange = this.handleChange.bind();
  }

  handleChange = (event) => {
    this.setState({ [event.target.name]: event.target.value });
  };
  handleFormat = (event) => {
    this.setState({ [event.target.name]: event.target.value });
  };
  render() {
    return (
      <div>
        <Header></Header>
        <div
          style={{ marginLeft: "10%", marginRight: "10%", marginTop: "30px" }}
        >
          <Grid
            container
            spacing={4}
            direction="horizenol"
            justify="center"
            alignItems="flex-start"
          >
            <Grid item xs={10}>
              <Paper style={{ height: "710px" }}>
                <div>
                  <TextField
                    style={{
                      marginLeft: "3%",
                      marginRight: "3%",
                      marginTop: "3%",
                      width: "94%",
                    }}
                    id="outlined-multiline-static"
                    label="Multiline"
                    multiline
                    rows={6}
                    defaultValue="Default Value"
                    variant="outlined"
                  ></TextField>
                  {/*
                  <ChipInput
                    style={{
                      marginLeft: "3%",
                      marginRight: "3%",
                      marginTop: "3%",
                      width: "94%",
                    }}
                    defaultValue={["foo", "bar"]}
                    onChange={(chips) => this.handleChange(chips)}
                  />
                 
                  <FormControl
                    component="fieldset"
                    style={{
                      marginLeft: "3%",
                      marginRight: "3%",
                      marginTop: "3%",
                      width: "94%",
                    }}
                  >
                   
                    <FormLabel component="legend">Share with</FormLabel>
                    <RadioGroup
                      row
                      aria-label="visible"
                      name="visible"
                      value={this.state.visibility}
                      onChange={this.handlevisibility}
                    >
                      <FormControlLabel
                        value="public"
                        control={<Radio />}
                        label="public"
                      />
                      <FormControlLabel
                        value="friends"
                        control={<Radio />}
                        label="friends circle"
                      />
                      <FormControlLabel
                        value="specifiedprivate"
                        control={<Radio />}
                        label="private to specified friends"
                      />
                      <FormControlLabel
                        value="specifiedvisible"
                        control={<Radio />}
                        label="visible to specified friends"
                      />
                      <FormControlLabel
                        value="onlyme"
                        control={<Radio />}
                        label="only me"
                      />
                    </RadioGroup>
                  </FormControl>
                  */}
                  <FormControl
                    component="fieldset"
                    style={{
                      marginLeft: "3%",
                      marginRight: "3%",
                      marginTop: "3%",
                      width: "94%",
                    }}
                  >
                    <FormLabel component="legend">Format</FormLabel>
                    <RadioGroup
                      row
                      aria-label="visible"
                      name="visible"
                      value={this.state.postFormat}
                      onChange={this.handleFormat}
                    >
                      <FormControlLabel
                        value="plaintext"
                        control={<Radio />}
                        label="Plain Text"
                      />
                      <FormControlLabel
                        value="markdown"
                        control={<Radio />}
                        label="Markdown"
                      />
                    </RadioGroup>
                  </FormControl>
                  <Button
                    variant="outlined"
                    color="primary"
                    style={{
                      marginLeft: "3%",
                      marginTop: "3%",
                    }}
                  >
                    Upload Image
                  </Button>
                  <Button
                    variant="outlined"
                    color="primary"
                    style={{
                      marginLeft: "3%",
                      marginTop: "3%",
                    }}
                  >
                    Preview
                  </Button>
                </div>
                <div>
                  <Button
                    variant="contained"
                    color="primary"
                    style={{
                      marginLeft: "3%",
                      marginTop: "3%",
                    }}
                  >
                    Submit
                  </Button>
                </div>
              </Paper>
            </Grid>
          </Grid>
        </div>
      </div>
    );
  }
}

export default Editpost;
