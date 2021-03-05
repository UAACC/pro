import React from "react";
import { Route, BrowserRouter, Switch } from "react-router-dom";
import { connect } from "react-redux";
import Main from "./pages/main";
import SignIn from "./pages/signin";
import SignUp from "./pages/signup";
import Header from "./components/Header";
import Postdetail from "./pages/postdetail";
import Editpost from "./pages/editpost";
import Newpost from "./pages/newpost";
import ProfilePage from "./pages/profile";
import newpost from "./pages/newpost";

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {};
  }

  beforeunload = (e) => {
    e.preventDefault();
    e.returnValue = true;
  };

  render() {
    return (
      <BrowserRouter>
        <Switch>
          <Route exact path="/" component={Main} />
          <Route exact path="/signin" component={SignIn} />
          <Route exact path="/signup" component={SignUp} />
          <Route exact path="/editpost" component={Editpost} />
          <Route exact path="/postdetail" component={Postdetail} />
          <Route exact path="/newpost" component={Newpost} />
          <Route exact path="/profile" component={ProfilePage} />
        </Switch>
      </BrowserRouter>
    );
  }
}

export default App;
