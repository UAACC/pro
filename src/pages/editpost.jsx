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
      newpost: {
        autherID: "",
        title: "",
        description: "",
        published: "",
        format: "",
        image: "",
        status: "",
      },
    };
    this.fetchTask = this.fetchTask.bind(this);
    this.handledescription = this.handledescription.bind(this);
    this.handleFormat = this.handleFormat.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  componentWillMount() {
    this.fetchTask();
  }
  handleFormat(event) {
    var name = event.target.name;
    var value = event.target.value;
    console.log("name:", name);
    console.log("value:", value);
    this.setState({
      newpost: {
        ...this.state.newpost,
        format: value,
      },
    });
  }
  handledescription(event) {
    var name = event.target.name;
    var value = event.target.value;
    console.log("name:", name);
    console.log("value:", value);
    this.setState({
      newpost: {
        ...this.state.newpost,
        description: value,
      },
    });
  }

  handleSubmit(event) {
    event.preventDefault();
    console.log("item:", this.state.newpost);
    var url = "http://127.0.0.1:8000/api/posts/create";
    fetch(url, {
      method: "POST",
      headers: {
        "Content-type": "application/json",
      },
      body: JSON.stringify(this.state.newpost),
    })
      .then((response) => {
        this.fetchTask();
        this.setState({
          PopupImageUpload: false,
          newpost: {
            autherID: "",
            title: "",
            description: "",
            published: "",
            image: "",
            status: "",
          },
        });
      })
      .catch(function (error) {
        console.log("error", error);
      });
  }
  fetchTask() {
    console.log("fetching...");
    fetch("http://127.0.0.1:8000/api/posts/")
      .then((response) => response.json())
      .then((data) => console.log("data:", data));
  }

  render() {
    return (
      <div>
        <Header></Header>
        <div
          style={{ marginLeft: "10%", marginRight: "10%", marginTop: "30px" }}
        >
          <form>
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
                      onChange={this.handledescription}
                      id="description"
                      name="description"
                      style={{
                        marginLeft: "3%",
                        marginRight: "3%",
                        marginTop: "3%",
                        width: "94%",
                      }}
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
                      onChange={this.handleFormat}
                    >
                      <FormLabel component="legend">Format</FormLabel>
                      <RadioGroup row aria-label="visible" name="visible">
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
                      onClick={() => {
                        this.setState({ PopupImageUpload: true });
                      }}
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
                      onClick={this.handleSubmit}
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
          </form>
        </div>
      </div>
    );
  }
}

export default Editpost;
