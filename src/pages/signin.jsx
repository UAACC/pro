import React from "react";
/*import SignInForm from "../components/signin/signin-form";*/
import axios from "axios";
import "./style/signin.css";
import Grid from "@material-ui/core/Grid";
import Button from "@material-ui/core/Button";
import { TextField } from "@material-ui/core";
import FormControlLabel from "@material-ui/core/FormControlLabel";
import Checkbox from "@material-ui/core/Checkbox";
import Link from "@material-ui/core/Link";

class SignInPage extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      username: "",
      password: "",
      loginError: "",
    };

    this.handleSubmit = this.handleSubmit.bind(this);
    this.handleChange = this.handleChange.bind(this);
  }
  handleChange(event) {
    this.setState({
      visibility: event.target.value,
    });
  }
  handleSubmit = async (event) => {
    const { username, password } = this.state;
    axios
      .post("/auth/", { username: username, password: password })
      .then((response) => {
        console.log("res from login", response);
      })
      .catch((error) => {
        console.log("login error", error);
      });
    event.preventDefault();
  };

  render() {
    return (
      <div className="login">
        <section className="content">
          <h2>Log in</h2>
          <form className="form" onSubmit={this.handleSubmit}>
            <Grid container spacing={1}>
              <Grid item xs={12}>
                <TextField
                  variant="outlined"
                  required
                  fullWidth
                  id="username"
                  label="User Name"
                  name="username"
                  value={this.state.username}
                  onChange={this.handleChange}
                />
              </Grid>
              <Grid item xs={12}>
                <TextField
                  variant="outlined"
                  required
                  fullWidth
                  style={{ marginTop: 5 }}
                  id="password"
                  label="Password"
                  name="password"
                  type="password"
                  value={this.state.password}
                  onChange={this.handleChange}
                />
              </Grid>
            </Grid>
            <FormControlLabel
              control={<Checkbox value="remember" color="primary" />}
              label="Remember me"
            />
            <Button
              type="Log in"
              fullWidth
              variant="contained"
              color="primary"
              className="submit"
              size="large"
              style={{ marginTop: 20 }}
            >
              Log in
            </Button>
            <Grid
              container
              alignItems="center"
              justify="center"
              spacing={0}
              direction="column"
              style={{ minHeight: "5vh", marginTop: 10 }}
            >
              <Grid item xs>
                <Link href="/signup" variant="body2">
                  {"Don't have an account? Sign Up"}
                </Link>
              </Grid>
            </Grid>
          </form>
        </section>
      </div>
    );
  }
}
export default SignInPage;
