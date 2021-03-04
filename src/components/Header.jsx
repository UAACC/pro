import React from "react";
import Profile from "./ProfileComponent.jsx";
import { connect } from "react-redux";

class Header extends React.Component {

  // renderHeader = () => {
  //   return (

  //   );
  // }

  render() {
    return (
      <nav className="navbar navbar-expand-lg navbar-dark bg-primary">
  <div className="container-fluid">
    <a className="navbar-brand" href="/">SpongebobClone</a>
    <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span className="navbar-toggler-icon"></span>
    </button>
    <div className="collapse navbar-collapse" id="navbarSupportedContent">
      <ul className="navbar-nav me-auto mb-2 mb-lg-0">
        <li className="nav-item">
          <a className="nav-link active" aria-current="page" href="/">public</a>
        </li>
        <li className="nav-item">
          <a className="nav-link active" aria-current="/post/create" href="/">create post</a>
        </li>
        <li className="nav-item">
          <a className="nav-link active" aria-current="page" href="/profile">my profile</a>
        </li>
      </ul>
      <form className="d-flex">
        <input className="form-control me-2" type="search" placeholder="search author" aria-label="Search"></input>
        <button className="btn btn-outline-success" type="submit">search author</button>
      </form>
    </div>
  </div>
</nav>      
    );
  }
}

// const mapStateToProps = (state) => ({
//   currentUser: state.user.currentUser,
// });

// export default connect(mapStateToProps)(Header);
export default Header;